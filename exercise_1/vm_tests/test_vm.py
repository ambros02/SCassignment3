import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from vm import VirtualMachine



@pytest.fixture
def too_big_program():
    program = []
    for x in range(257):
        program.append('000001')
    return program

def fetch_instructions(file_name):
    location = os.path.join(os.path.dirname(os.path.dirname(__file__)),'test_files',file_name)
    with open(location,"r") as f:
        lines = [line.strip() for line in f.readlines()]
    program = [int(line,16) for line in lines]
    return program


def execute_vm(instructions):
    machine = VirtualMachine()
    machine.initialize(instructions)
    machine.run()
    return machine


def test_vm_basic_operations():
    program = fetch_instructions('basic_operations.mx')
    vir = execute_vm(program)
    assert vir.ram[50] == 3, f'the value at ram[50] of the basic_operations programm should be 3 but is {vir.ram[50]}'


def test_vm_branch_not_equal():
    program = fetch_instructions('branch_not_equal.mx')
    vir = execute_vm(program)
    assert vir.ram[50] == 2, f'the value at ram[50] of the branch_not_equal programm should be 2 but is {vir.ram[50]}'


def test_memory_operations():
    program = fetch_instructions('memory_operations.mx')
    vir = execute_vm(program)
    assert vir.ram[10] == 10, f'the value at ram[10] should be 10 but is {vir.ram[10]}'


def test_branch_if_equal():
    program = fetch_instructions('branch_if_equal.mx')
    vir = execute_vm(program)
    assert vir.ram[50] == 1, f'the value at ram[50] should be 1 but is {vir.ram[50]}'


def test_out_of_memory(too_big_program):

    with pytest.raises(Exception):
        execute_vm(too_big_program)


def test_instruction_not_found():
    program = ['aaaaaa']
    with pytest.raises(Exception):
        execute_vm(program)