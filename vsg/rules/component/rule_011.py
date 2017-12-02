
from vsg.rules.component import component_rule
from vsg import fix

import re


class rule_011(component_rule):
    '''Component rule 011 checks for a single space after the "end" keyword'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Reduce spaces after "end" keyword to one.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                if re.match('^\s*end\s+\w', oLine.lineLower):
                    if not re.match('^\s*end\s\w', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'end')