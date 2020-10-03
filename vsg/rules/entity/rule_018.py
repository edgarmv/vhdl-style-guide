
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.interface_unknown_declaration.assignment)


class rule_018(align_tokens_in_region_between_tokens):
    '''
    Component rule 018 ensures the alignment of the colon for each generic and port in the entity declaration.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'entity', '018', lAlign, token.entity_declaration.entity_keyword, token.entity_declaration.end_keyword)
        self.solution = 'Align :.'
