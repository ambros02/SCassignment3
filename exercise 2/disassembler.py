import sys
from architecture import OPS


class Disassembler:
    def __init__(self, labels):
        self.labels = labels
        self.count = 1

    def disassemble(self, lines):
        disassembly_code = [self._compile(instr) for instr in lines]
        return disassembly_code

    def _compile(self, instruction):
        op = instruction[4:]
        fmt, code = self._get_op(op)
        arg1 = instruction[2:4]
        arg2 = instruction[0:2]

        if fmt == "--":
            return code
        elif fmt == "r-":
            reg = int(arg1, 16)
            return f"{code} R{str(reg)}"
        elif fmt == "rr":
            reg1 = int(arg1, 16)
            reg2 = int(arg2, 16)
            return f"{code} R{str(reg1)} R{str(reg2)}"
        elif fmt == "rv":
            if code == "beq" or code == "bne":
                reg = int(arg1, 16)
                pos = int(arg2, 16)
                label = "L" + str(self.count)
                self.labels[label] = pos
                self.count += 1
                return f"{code} R{str(reg)} @{label}"
            else:
                reg = int(arg1, 16)
                value = int(arg2, 16)
                return f"{code} R{str(reg)} {str(value)}"

    def _get_op(self, op):
        for name, op_info in OPS.items():
            if op_info["code"] == int(op, 16):
                return op_info["fmt"], name


def main():
    assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} input|- output|-"
    reader = open(sys.argv[1], "r") if (sys.argv[1] != "-") else sys.stdin
    writer = open(sys.argv[2], "w") if (sys.argv[2] != "-") else sys.stdout
    lines = reader.readlines()
    labels = {}
    disassembler = Disassembler(labels)
    program = disassembler.disassemble(lines)

    label = disassembler.labels.copy()
    for lab, position in label.items():
        program.insert(position, lab+":")

    for instruction in program:
        print(instruction, file=writer)


if __name__ == "__main__":
    main()
