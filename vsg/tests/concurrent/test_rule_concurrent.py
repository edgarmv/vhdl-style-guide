import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleConcurrentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = concurrent.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([7,11,24,32,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = concurrent.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '002')
        dExpected = utils.add_violation_list([7,8,24,32,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = concurrent.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [28,29,30]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = concurrent.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([7,8,32,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = concurrent.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [{'lineNumber': 32, 'label': 'label'},
                     {'lineNumber': 33, 'label': 'label'},
                     {'lineNumber': 34, 'label': 'label'},
                     {'lineNumber': 35, 'label': 'label'}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = concurrent.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [{'lines': [{'number': 6, 'keyword_column': 16},
                                {'number': 7, 'keyword_column': 2},
                                {'number': 8, 'keyword_column': 3},
                                {'number': 9, 'keyword_column': 4},
                                {'number': 11, 'keyword_column': 6}], 'max_keyword_column': 16},
                     {'lines': [{'number': 23, 'keyword_column': 4},
                                {'number': 24, 'keyword_column': 3}], 'max_keyword_column': 4},
                     {'lines': [{'number': 32, 'keyword_column': 7},
                                {'number': 33, 'keyword_column': 9},
                                {'number': 34, 'keyword_column': 12},
                                {'number': 35, 'keyword_column': 12}], 'max_keyword_column': 12},
                     {'lines': [{'number': 50, 'keyword_column': 4},
                                {'number': 52, 'keyword_column': 16}], 'max_keyword_column': 16}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = concurrent.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [{'lineNumber': 44, 'slice_index': [26]},
                     {'lineNumber': 48, 'slice_index': [26]}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = concurrent.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [{'lines': [{'number': 6, 'keyword_column': 27},
                                {'number': 7, 'keyword_column': 19},
                                {'number': 8, 'keyword_column': 14},
                                {'number': 9, 'keyword_column': 23},
                                {'number': 11, 'keyword_column': 18}], 'max_keyword_column': 27}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
