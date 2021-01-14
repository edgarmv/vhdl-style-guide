
import os
import unittest

from vsg.rules import block
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_203_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_203_test_input.fixed.vhd'), lExpected, False)


class test_block_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_203(self):
        oRule = block.rule_203()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'block')
        self.assertEqual(oRule.identifier, '203')

        lExpected = [15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_203(self):
        oRule = block.rule_203()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
