import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','signal','signal_test_input.vhd'))

class testFixRuleSignalMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = signal.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])


if __name__ == '__main__':
    unittest.main()
