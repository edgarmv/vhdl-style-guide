
from vsg.rules import keyword_alignment_rule


class rule_009(keyword_alignment_rule):
    '''
    Constant rule 009 checks the colons are in the same column for all constants.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self)
        self.name = 'constant'
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isArchitectureKeyword'
        self.sEndGroupTrigger = 'isEndArchitecture'
        self.sLineTrigger = 'isConstant'
