import sys

from architecture import OPS, VMState
from vm_extend import VirtualMachineExtend


class VirtualMachineBreak(VirtualMachineExtend):
    # [init]
    def __init__(self):
        super().__init__()
        self.breaks = {}
        self.watchpoints = {}
        self.handlers |= {
            "break": self._do_add_breakpoint,
            "clearbrk": self._do_clear_breakpoint,
            "watchpoint": self._do_add_watchpoint,
            "clearwpt": self._do_clear_watchpoint
        }
    # [/init]

    # [show]
    def show(self):
        super().show()
        if self.breaks or self.watchpoints:
            self.write("-" * 6)
            self.write("breaks")
            for key, instruction in self.breaks.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")
            self.write("-" * 6)
            self.write("watchpoints")
            for key, instruction in self.watchpoints.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")
            
    # [/show]

    def check_watchpoints(self):
        for wp in self.watchpoints:
                if self.ram[wp] != self.watchpoints[wp]:
                    self.watchpoints[wp] = self.ram[wp]
                    self.write(f"watchpoint hit at address {wp}")
                    self.interact(self.ip)

    # [run]
    def run(self):
        self.state = VMState.STEPPING
        while self.state != VMState.FINISHED:

            

            instruction = self.ram[self.ip]
            op, arg0, arg1 = self.decode(instruction)

            if op == OPS["brk"]["code"]:
                original = self.breaks[self.ip]
                op, arg0, arg1 = self.decode(original)
                self.interact(self.ip)
                self.execute(op, arg0, arg1)
                self.check_watchpoints()
                self.ip += 1

            else:
                if self.state == VMState.STEPPING:
                    self.interact(self.ip)
                self.execute(op, arg0, arg1)
                self.check_watchpoints()
                self.ip += 1
    # [/run]

    # [add brk]
    def _do_add_breakpoint(self, addr):
        if self.ram[addr] == OPS["brk"]["code"]:
            return True
        self.breaks[addr] = self.ram[addr]
        self.ram[addr] = OPS["brk"]["code"]
        return True
    # [/add brk]

    # [clear brk]
    def _do_clear_breakpoint(self, addr):
        if self.ram[addr] != OPS["brk"]["code"]:
            return True
        self.ram[addr] = self.breaks[addr]
        del self.breaks[addr]
        return True
    # [/clear brk]

    # [add wpt]
    def _do_add_watchpoint(self, addr):
        if addr in self.watchpoints:
            self.write(f"Watchpoint already set at address {addr:06x}")
            return True
        self.watchpoints[addr] = self.ram[addr]
        return True

    # [/add wpt]

    # [clear wpt]
    def _do_clear_watchpoint(self, addr):
        if addr in self.watchpoints:
            del self.watchpoints[addr]
            self.write(f"Cleared watchpoint at address {addr:06x}")
        else:
            self.write(f"No watchpoint set at address {addr:06x}")
        return True
    # [/clear wpt]


if __name__ == "__main__":
    VirtualMachineBreak.main()
