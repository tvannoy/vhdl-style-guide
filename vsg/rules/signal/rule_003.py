
from vsg.rules.signal import signal_rule
from vsg import fix

import re


class rule_003(signal_rule):
    '''
    Signal rule 003 checks there is a single space after the "signal" keyword.
    '''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "signal" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s*signal\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'signal')