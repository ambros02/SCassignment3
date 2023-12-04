import sys
from architecture import OPS, VMState
from vm_extend import VirtualMachineExtend


class VirtualMachineWatch(VirtualMachineExtend):
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.watchpoints = {}

    def execute(self, op, arg0, arg1):
        if op == OPS["wp"]["code"]:
            self.assert_is_address(arg0)
            # set watchpoint
            if arg1:
                self.watchpoints[arg0] = self.ram[arg0]
            # clear watchpoint
            else:
                if arg0 in self.watchpoints:
                    del self.watchpoints[arg0]
        else:
            super().execute(op, arg0, arg1)

    def run(self):
        self.state = VMState.STEPPING
        while self.state != VMState.FINISHED:
            instruction = self.ram[self.ip]
            op, arg0, arg1 = self.decode(instruction)

            if op == OPS["wp"]["code"] and arg1:
                if arg0 in self.watchpoints and self.ram[arg0] != self.watchpoints[arg0]:
                    self.state = VMState.FINISHED
            else:
                if self.state == VMState.STEPPING:
                    self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)

    if __name__ == "__main__":
        VirtualMachineWatch.main()
