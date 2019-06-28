import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import after
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'after_test_input.vhd'))

class testRuleAfterMethods(unittest.TestCase):

    def setUp(self):
       self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = after.rule_001()
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[33].line,'       b <= c after 1 ns;')
        self.assertEqual(self.oFile.lines[34].line,'       c <= d after 1 ns;')

        lExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)
