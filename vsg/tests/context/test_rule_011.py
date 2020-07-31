
import os
import unittest

from vsg.rules import context
from vsg import vhdlFile
from vsg.tests import utils
from vsg import parser

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_011_test_input.vhd'))
lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_011_test_input.fixed.vhd'), lExpected)


class test_context_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_011(self):
        self.maxDiff = None
        oRule = context.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'context')
        self.assertEqual(oRule.identifier, '011')

        lExpected = []
        
        dViolation = utils.add_violation(10)
        dViolation['iLeftLineNumber'] = 9
        dViolation['solution'] = 'Move ";" to the right of "c1" on line 9'
        dViolation['left'] = parser.context_end_identifier
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['iLeftLineNumber'] = 19
        dViolation['solution'] = 'Move ";" to the right of "c1" on line 19'
        dViolation['left'] = parser.context_end_identifier
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['iLeftLineNumber'] = 26
        dViolation['solution'] = 'Move ";" to the right of "c1" on line 26'
        dViolation['left'] = parser.context_end_identifier
        lExpected.append(dViolation)

        dViolation = utils.add_violation(40)
        dViolation['iLeftLineNumber'] = 38
        dViolation['solution'] = 'Move ";" to the right of "c1" on line 38'
        dViolation['left'] = parser.context_end_identifier
        lExpected.append(dViolation)

        dViolation = utils.add_violation(47)
        dViolation['iLeftLineNumber'] = 46
        dViolation['solution'] = 'Move ";" to the right of "end" on line 46'
        dViolation['left'] = parser.context_end_keyword
        lExpected.append(dViolation)

        dViolation = utils.add_violation(52)
        dViolation['iLeftLineNumber'] = 51
        dViolation['solution'] = 'Move ";" to the right of "context" on line 51'
        dViolation['left'] = parser.context_end_context_keyword
        lExpected.append(dViolation)

        dViolation = utils.add_violation(57)
        dViolation['iLeftLineNumber'] = 56
        dViolation['solution'] = 'Move ";" to the right of "c1" on line 56'
        dViolation['left'] = parser.context_end_identifier
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_011(self):
        self.maxDiff = None
        oRule = context.rule_011()

        oRule.fix(self.oFile)

        lActual = []
        for oLine in self.oFile.lines:
            lActual.append(oLine.line)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

