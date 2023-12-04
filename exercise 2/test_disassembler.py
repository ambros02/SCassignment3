from disassembler import Disassembler


def test_one_instruction():
    disassembler = Disassembler(labels={})
    result = disassembler._compile("000001")
    assert result == "hlt"


def test_various_instructions():
    disassembler = Disassembler(labels={})
    lines = ["000002", "030102", "00000a", "010202", "02006", "010204"]
    result = [disassembler._compile(instr) for instr in lines]
    assert result == ["ldc R0 0", "ldc R1 3", "prr R0", "ldc R2 1", "add R0 R2", "cpy R2 R1"]


def test_one_label():
    disassembler = Disassembler(labels={})
    disassembler._compile("020209")
    label = disassembler.labels.copy()
    assert len(label) == 1


def test_various_labels():
    disassembler = Disassembler(labels={})
    lines = ["020209", "040109", "020108"]
    [disassembler._compile(instr) for instr in lines]
    label = disassembler.labels.copy()
    assert len(label) != 0


def test_no_label():
    disassembler = Disassembler(labels={})
    disassembler._compile("010202")
    label = disassembler.labels.copy()
    assert len(label) == 0


def test_label_position():
    disassembler = Disassembler(labels={})
    lines = ["000002", "010202", "020006", "020209"]
    result = [disassembler._compile(instr) for instr in lines]
    label = disassembler.labels.copy()
    for lab, position in label.items():
        result.insert(position, lab + ":")
    assert result[2] == "L1:"


def test_hex_int_conversion():
    disassembler = Disassembler(labels={})
    code = disassembler._compile("030102")
    result = code.split()
    assert int(result[2]) == 3
