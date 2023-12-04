import sys
import os
import pytest

same_parent = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
parent_of_files = os.path.join(same_parent,'vm')
sys.path.append(parent_of_files)

from vm import VirtualMachine
from assembler import Assembler




def assemble_file(file_name):
    parent_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test_files")
    asbler = Assembler()


    file_p = os.path.join(parent_path,file_name)
    with open(file_p,"r") as f:
        lines = f.readlines()
    program = asbler.assemble(lines)
    new_name = file_name.replace(".as",".mx")
    new_p = os.path.join(parent_path,new_name)
    with open(new_p,"w") as f:
        for p in program:
            print(p,file=f)

def remove_file(file_name):
    parent_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test_files")
    file_p = os.path.join(parent_path,file_name)
    os.remove(file_p)



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
    assemble_file("basic_operations.as")
    program = fetch_instructions('basic_operations.mx')
    vir = execute_vm(program)
    remove_file("basic_operations.mx")
    assert vir.ram[50] == 3, f'the value at ram[50] of the basic_operations programm should be 3 but is {vir.ram[50]}'


def test_vm_branch_not_equal():
    assemble_file("branch_not_equal.as")
    program = fetch_instructions('branch_not_equal.mx')
    vir = execute_vm(program)
    remove_file("branch_not_equal.mx")
    assert vir.ram[50] == 2, f'the value at ram[50] of the branch_not_equal programm should be 2 but is {vir.ram[50]}'


def test_memory_operations():
    assemble_file("memory_operations.as")
    program = fetch_instructions('memory_operations.mx')
    vir = execute_vm(program)
    remove_file("memory_operations.mx")
    assert vir.ram[10] == 10, f'the value at ram[10] should be 10 but is {vir.ram[10]}'


def test_branch_if_equal():
    assemble_file("branch_if_equal.as")
    program = fetch_instructions('branch_if_equal.mx')
    vir = execute_vm(program)
    remove_file("branch_if_equal.mx")
    assert vir.ram[50] == 1, f'the value at ram[50] should be 1 but is {vir.ram[50]}'


def test_out_of_memory():

    program = []
    for x in range(257):
        program.append('000001')
    with pytest.raises(Exception):
        execute_vm(program)


def test_instruction_not_found():
    program = ['161616']
    program = [int(line,16) for line in program]
    with pytest.raises(Exception):
        execute_vm(program)