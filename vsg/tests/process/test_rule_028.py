
import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_028_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_028_test_input.fixed.vhd'), lExpected)


class test_process_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_028(self):
        oRule = process.rule_028()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '028')
        self.assertEqual(oRule.groups, ['alignment'])

        lExpected = [19, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_028(self):
        oRule = process.rule_028()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
