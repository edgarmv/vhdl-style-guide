
from vsg.rules.architecture import architecture_rule
from vsg import check
from vsg import fix


class rule_008(architecture_rule):
    '''Architecture rule 008 checks for spaces at the beginning of the line for the "end architecture" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndArchitecture:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])