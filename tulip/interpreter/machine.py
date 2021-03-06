# single-threaded execution

import tulip.interpreter.lang  as lang
import tulip.interpreter.rules as rules
from tulip.interpreter.state import MachineState

class MachineContext():
    """
    single-threaded tulip execution context
    wraps an AST and incrementally reduces it
    """

    def __init__(self, ast):
        self.cycle   = 0 # iteration count
        self.state = MachineState.fromProgram(ast)

    def step(self,n):
        """performs n iterations of the interpreter loop"""
        while n > 0:
            n = n - 1

    def loop(self):
        """runs the interpreter loop until program yields"""

    def run(self):
        try:
            rules.expand(0, self.state)
            rules.reduce(0, self.state)

            print ansi_green, self.state.registers[0].show()
        finally:
            print ansi_default

    def runVerbose(self):
        try:
            """evaluates some expression until it is fully reduced, temporary testing"""

            print ansi_blue + "input state: "
            self.dump()
            print

            print ansi_white, "program stdout:"

            rules.expand(0, self.state)
            rules.reduce(0, self.state)

            print
            print ansi_green, "output state:"

            self.dump()
            print

            print ansi_white + "execution finished, program returned: " + self.state.registers[0].show()
        finally:
            print ansi_default

    def halt(self):
        """prematurely stops evaluation in this context"""
        assert False, "DO NOT IMPLEMENT CONCURRENCY YET"

    def dump(self):
        """printss all context internal state for debugging """

        print self.state.program.show()

        for _,v in self.state.bindings.items():
            print v.show()

        print self.state.registers.show()

ansi_blue = "\033[94m"
ansi_green = "\033[92m"
ansi_white = "\033[97m"
ansi_default = "\033[0m"
