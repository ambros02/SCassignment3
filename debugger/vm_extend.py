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
            "step": self._do_step,
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
        self.show()
        return True
    # [/memory]

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
