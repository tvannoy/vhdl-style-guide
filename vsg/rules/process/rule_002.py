
from vsg.rules.process import process_rule
from vsg import fix

import re


class rule_002(process_rule):
    '''
    Process rule 002 checks there is a single space between the process
    keyword and the (.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists between the "process" \
                          keyword and the (.'
        self.phase = 2

    def analyze(self, oFile):
        fInsideProcess = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword and not re.match('^\s*.*process\s\(', oLine.lineLower):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'process')