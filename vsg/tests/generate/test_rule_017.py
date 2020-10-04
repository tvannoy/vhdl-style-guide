
import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = utils.read_vhdlfile(os.path.join(sTestDir,'rule_017_test_input.vhd'))


class test_generate_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_017(self):
        oRule = generate.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '017')

        lExpected = [20, 24, 28]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
