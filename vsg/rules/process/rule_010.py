
from vsg.rules.process import process_rule
from vsg import line
from vsg import utilities

import re


class rule_010(process_rule):
    '''
    Process rule 010 checks the "begin" keyword is on it's own line.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Place "begin" keyword on seperate line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                if not re.match('^\s*begin', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('begin', ' '*len('begin'), oLine.line, 1, flags=re.IGNORECASE))
            oLine.isProcessBegin = False
            oFile.lines.insert(iLineNumber + 1, line.line('  begin'))
            oFile.lines[iLineNumber + 1].isProcessBegin = True
            oFile.lines[iLineNumber + 1].indentLevel = oLine.indentLevel