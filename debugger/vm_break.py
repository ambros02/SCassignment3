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
            "b": self._do_add_breakpoint,
            "break": self._do_add_breakpoint,
            "cb": self._do_clear_breakpoint,
            "clearbrk": self._do_clear_breakpoint,
            "w": self._do_add_watchpoint,
            "watchpoint": self._do_add_watchpoint,
            "cw": self._do_clear_watchpoint,
            "clearwpt": self._do_clear_watchpoint,
        }
    # [/init]

    # [show]
    def show(self):
        super().show()
        if self.breaks:
            self.write("-" * 6)
            for key, instruction in self.breaks.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")
    # [/show]

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
                self.ip += 1
                self.execute(op, arg0, arg1)
            elif op == OPS["wpt"]["code"]:
                addr, old_value = arg0, self.ram[arg1]
                new_value = self.ram[addr]
                if old_value != new_value:
                    self.write(f"Watchpoint hit at address {addr:o6x}")
                    self.state = VMState.FINISHED
                    self.interact(addr)
                self.ip += 1
                self.execute(op, arg0, arg1)
            else:
                if self.state == VMState.STEPPING:
                    self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)
    # [/run]

    # [add brk]
    def _do_add_breakpoint(self, addr):
        if self.ram[addr] == OPS["brk"]["code"]:
            return
        self.breaks[addr] = self.ram[addr]
        self.ram[addr] = OPS["brk"]["code"]
        return True
    # [/add brk]

    # [clear brk]
    def _do_clear_breakpoint(self, addr):
        if self.ram[addr] != OPS["brk"]["code"]:
            return
        self.ram[addr] = self.breaks[addr]
        del self.breaks[addr]
        return True
    # [/clear brk]

    # [add wpt]
    def _do_add_watchpoint(self, addr):
        if addr in self.watchpoints:
            self.write(f"Watchpoint already set at address {addr:06x}")
            return True
        original_value = self.ram[addr]
        self.watchpoints[addr] = original_value
        self.write(f"Watchpoint set at address {addr:06x}, original value: {original_value:06x}")
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
