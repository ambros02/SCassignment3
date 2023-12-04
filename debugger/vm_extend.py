import sys

from architecture import VMState
from vm_step import VirtualMachineStep


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)

        #handlers only as full name since interact will take care of the rest.
        self.handlers = {
            "disassemble": self._do_disassemble,
            "ip": self._do_ip,
            "memory": self._do_memory,
            "quit": self._do_quit,
            "run": self._do_run,
            "step": self._do_step
        }
    # [/init]

    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        while interacting:
            try:
                command = self.read(f"{addr:06x} [{prompt}]> ")
                if not command:
                    continue
                
                else:
                    #find possible matches for the command and split it from ids
                    com, *ip_spec = command.split(" ") 
                    possibilities = [handler for handler in self.handlers if handler.startswith(com)]

                    if len(possibilities) == 0:
                        self.write(f"Unknown command {command}")

                    elif len(possibilities) > 1 and command not in possibilities:
                        self.write(f"{command} is not unique identifying: options are: {possibilities}")

                    else:
                        if len(possibilities) > 1:
                            possibilities = [command]
                        if ip_spec:
                            ip_spec = [int(ip) for ip in ip_spec]
                            for ip_s in ip_spec:
                                interacting = self.handlers[possibilities[0]](ip_s)
                        else:
                            interacting = self.handlers[possibilities[0]](self.ip)
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]

    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, addr):
        args = self.read("Enter one or two addresses (hex): ").split()
        if not args:
            self.show()
            return True
        if len(args) == 1:
            address = int(args[0], 16)
            self.show_memory_at_address(address)
        elif len(args) == 2:
            start_address = int(args[0], 16)
            end_address = int(args[1], 16)
            self.show_memory_range(start_address, end_address)
        else:
            self.write("Invalid number of arguments. Please provide one or two addresses.")

        return True
    # [/memory]
    def show_memory_at_address(self, address):
        if 0 <= address < len(self.ram):
            self.write(f"{address:06x}: {self.ram[address]:06x}")
        else:
            self.write(f"Invalid address: {address:06x}")

    def show_memory_range(self, start_address, end_address):
        if 0 <= start_address < len(self.ram) and 0 <= end_address < len(self.ram):
            for addr in range(start_address, end_address + 1):
                self.write(f"{addr:06x}: {self.ram[addr]:06x}")
        else:
            self.write("Invalid start or end address.")
    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    # [step]
    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
    # [/step]


if __name__ == "__main__":
    VirtualMachineExtend.main()
