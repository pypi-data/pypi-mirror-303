# tap_consumer/__init__.py - TAP-Consumer
#
# Based on TAP.py - TAP parser
#
# A pyparsing parser to process the output of the Perl
#   "Test Anything Protocol"
#   (https://metacpan.org/pod/release/PETDANCE/TAP-1.00/TAP.pm)
# Copyright 2008, by Paul McGuire
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Modified to ignore non-TAP input and handle YAML diagnostics
# Copyright 2024, Eden Ross Duff, MSc
import sys
from typing import Mapping
from typing import TypeAlias

import yaml
from pyparsing import CaselessLiteral
from pyparsing import FollowedBy
from pyparsing import Group
from pyparsing import LineEnd
from pyparsing import LineStart
from pyparsing import Literal
from pyparsing import OneOrMore
from pyparsing import Optional
from pyparsing import ParserElement
from pyparsing import ParseResults
from pyparsing import Regex
from pyparsing import SkipTo
from pyparsing import Suppress
from pyparsing import White
from pyparsing import Word
from pyparsing import empty
from pyparsing import nums
from pyparsing import rest_of_line

if sys.version_info >= (3, 11):  # pragma: no cover
    from typing import Self  # noqa: TC002
elif sys.version_info < (3, 11):  # pragma: no cover
    from typing_extensions import Self  # noqa: TC002

__all__ = ['tap_document', 'TAPTest', 'TAPSummary']

# newlines are significant whitespace, so set default skippable
# whitespace to just spaces and tabs
ParserElement.set_default_whitespace_chars(' \t')
NL = LineEnd().suppress()  # type: ignore
INDENT = Suppress(OneOrMore(White(' ', exact=4)))
integer = Word(nums)
plan = '1..' + integer('ubound')

OK, NOT_OK = map(Literal, ['ok', 'not ok'])
test_status = OK | NOT_OK

description = Regex('[^#\n]+')
description.set_parse_action(lambda t: t[0].lstrip('- '))  # pyright: ignore

TODO, SKIP = map(CaselessLiteral, 'TODO SKIP'.split())  # noqa: T101
directive = Group(
    Suppress('#')
    + (
        TODO + rest_of_line  # noqa: T101
        | FollowedBy(SKIP) + rest_of_line.copy().set_parse_action(lambda t: ['SKIP', t[0]])
    ),
)
comment_line = Suppress('#') + empty + rest_of_line
version = Suppress('TAP version') + Word(nums[1:], nums, as_keyword=True)
yaml_end = Suppress('...')
test_line = Group(
    Optional(OneOrMore(comment_line + NL))('comments')
    + LineStart()
    + test_status('passed')
    + Optional(integer)('test_number')
    + Optional(description)('description')
    + Optional(directive)('directive')
    + Optional(
        NL
        + Group(
            Optional(INDENT)
            + Suppress('---')
            + SkipTo(yaml_end).set_parse_action(
                lambda t: yaml.safe_load(t[0])  # pyright: ignore
            )
            + yaml_end,
        )('yaml').set_parse_action(lambda t: t.as_dict()),
    ),
)
bail_line = Group(
    CaselessLiteral('Bail out!')('BAIL') + empty + Optional(rest_of_line)('reason')
)
tap_document = Optional(
    Group(Suppress(SkipTo(version)) + version)('version') + NL
) + Optional(
    Group(plan)('plan') + NL,
) & Group(
    OneOrMore((Optional(Suppress(SkipTo(test_line))) + test_line | bail_line) + NL)
)(
    'tests',
)


class TAPTest:
    """A single TAP test point."""

    def __init__(self: Self, results: ParseResults) -> None:
        """Create a test point.

        :param results: parsed TAP stream
        :type results: ParseResults
        """
        self.num = results.test_number
        self.description = results.description if results.description else None
        self.passed = results.passed == 'ok'
        self.skipped = self.todo = False
        if results.directive:
            self.skipped = results.directive[0][0] == 'SKIP'
            self.todo = results.directive[0][0] == 'TODO'  # noqa: T101
        self.yaml = results.yaml['yaml'] if results.yaml else {}  # pyright: ignore

    @classmethod
    def bailed_test(cls: type[Self], num: int) -> 'TAPTest':
        """Create a bailed test.

        :param num: the test number
        :type num: int
        :return: a bailed TAPTest object
        :rtype: TAPTest
        """
        ret = TAPTest(empty.parse_string(''))
        ret.num = num
        ret.skipped = True
        return ret


Diagnostics: TypeAlias = Mapping[
    int | str, str | list[Mapping[int | str, str]] | Mapping[int | str, str]
]


def iter_diagnostics(
    d: Diagnostics,
    text: list[str] | None = None,
) -> str:
    """Iterate through a dictionary of YAML diagnostics.

    :param d: parsed YAML
    :type d: Diagnostics
    :param text: text to populate, optional
    :type text: list[str] | None
    """
    text = [] if text is None else text
    for k, v in d.items():
        if isinstance(v, dict):
            text.append(f'{k}:')
            iter_diagnostics(v, text)
        elif isinstance(v, list):
            for i in v:
                (iter_diagnostics(i, text))
        else:
            text.append(f'{k}: {"" if v is None else v}'.strip())
    return '\n'.join(text)


class TAPSummary:
    """Summarize a parsed TAP stream."""

    def __init__(self: Self, results: ParseResults) -> None:  # noqa: C901
        """Initialize with parsed TAP data.

        :param results: A parsed TAP stream
        :type results: ParseResults
        """
        self.passed_tests: list[TAPTest] = []
        self.failed_tests: list[TAPTest] = []
        self.skipped_tests: list[TAPTest] = []
        self.todo_tests: list[TAPTest] = []
        self.bonus_tests: list[TAPTest] = []
        self.yaml_diagnostics: Diagnostics = {}
        self.bail = False
        self.version = results.version[0] if results.version else 12
        if results.plan:
            expected = list(range(1, int(results.plan.ubound) + 1))  # pyright: ignore
        else:
            expected = list(range(1, len(results.tests) + 1))
        print(results.dump())
        for i, res in enumerate(results.tests):
            # test for bail out
            if res.BAIL:  # pyright: ignore
                # ~ print "Test suite aborted: " + res.reason
                # ~ self.failed_tests += expected[i:]
                self.bail = True
                self.skipped_tests += [TAPTest.bailed_test(ii) for ii in expected[i:]]
                self.bail_reason = res.reason  # pyright: ignore
                break

            testnum = i + 1
            if res.test_number != '':  # pragma: no cover  # pyright: ignore
                if testnum != int(res.test_number):  # pyright: ignore
                    print('ERROR! test %(test_number)s out of sequence' % res)
                testnum = int(res.test_number)  # pyright: ignore
            res['test_number'] = testnum  # pyright: ignore

            test = TAPTest(res)  # pyright: ignore
            if test.yaml:
                self.yaml_diagnostics.update(
                    {testnum: [{testnum: test.description} | test.yaml[0]]}  # type: ignore
                )
            if test.passed:
                self.passed_tests.append(test)
            else:
                self.failed_tests.append(test)
            if test.skipped:
                self.skipped_tests.append(test)
            if test.todo:
                self.todo_tests.append(test)
            if test.todo and test.passed:
                self.bonus_tests.append(test)

        self.passed_suite = not self.bail and (
            set(self.failed_tests) - set(self.todo_tests) == set()
        )

    def summary(  # noqa: C901
        self: Self,
        show_passed: bool = False,
        show_all: bool = False,
    ) -> str:
        """Get the summary of a TAP stream.

        :param show_passed: show passed tests, defaults to False
        :type show_passed: bool, optional
        :param show_all: show all results, defaults to False
        :type show_all: bool, optional
        :return: a text summary of a TAP stream
        :rtype: str
        """
        test_list_str = lambda tl: '[' + ','.join(str(t.num) for t in tl) + ']'  # noqa: E731
        summary_text = []
        if show_passed or show_all:
            summary_text.append(f'PASSED: {test_list_str(self.passed_tests)}')  # type: ignore
        else:  # pragma: no cover
            pass
        if self.failed_tests or show_all:
            summary_text.append(f'FAILED: {test_list_str(self.failed_tests)}')  # type: ignore
        else:  # pragma: no cover
            pass
        if self.skipped_tests or show_all:
            summary_text.append(f'SKIPPED: {test_list_str(self.skipped_tests)}')  # type: ignore
        else:  # pragma: no cover
            pass
        if self.todo_tests or show_all:
            summary_text.append(
                f'TODO: {test_list_str(self.todo_tests)}'  # type: ignore  # noqa: T101
            )
        else:  # pragma: no cover
            pass
        if self.bonus_tests or show_all:
            summary_text.append(f'BONUS: {test_list_str(self.bonus_tests)}')  # type: ignore
        else:  # pragma: no cover
            pass
        if self.yaml_diagnostics:
            summary_text.append(iter_diagnostics(self.yaml_diagnostics))
        else:  # pragma: no cover
            pass
        if self.passed_suite:
            summary_text.append('PASSED')
        else:
            summary_text.append('FAILED')
        return '\n'.join(summary_text)


tap_document.set_parse_action(TAPSummary)
