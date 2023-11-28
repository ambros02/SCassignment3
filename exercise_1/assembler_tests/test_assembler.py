import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from assembler import Assembler




@pytest.fixture
def fetch_basic_operations():
    with open('test_files\\basic_operations.as', 'r') as f:
        instructions = f.readlines()
    location = os.path.join(os.path.dirname(os.path.dirname(__file__)),'test_files','basic_operations.mx')
    return instructions,location


@pytest.fixture
def fetch_branch_not_equal():
    with open('test_files\\branch_not_equal.as', 'r') as f:
        instructions = f.readlines()
    location = os.path.join(os.path.dirname(os.path.dirname(__file__)),'test_files','branch_not_equal.mx')
    return instructions,location


@pytest.fixture
def fetch_memory_operations():
    with open('test_files\\memory_operations.as', 'r') as f:
        instructions = f.readlines()
    location = os.path.join(os.path.dirname(os.path.dirname(__file__)),'test_files','memory_operations.mx')
    return instructions,location


@pytest.fixture
def fetch_branch_if_equal():
    with open('test_files\\branch_if_equal.as', 'r') as f:
        instructions = f.readlines()
    location = os.path.join(os.path.dirname(os.path.dirname(__file__)),'test_files','branch_if_equal.mx')
    return instructions,location


def assemble_basis(lines,out):
    asbler = Assembler()

    program = asbler.assemble(lines)
    with open(out,'w') as out_file:

        for line in program:
            print(line, file=out_file)

    return program



codes = {'basic_operations':['010002','020102','010006','00000a','320302','030005','000001'],
         'branch_not_equal':['010202','010002','320202','030103','000106', '000207','030209','030105','000001'],
         'memory_operations':['100102','000104','000105','00000b','000001'],
         'branch_if_equal':['000001','010101','000201','010206','030208','320202','030205']}






def test_basic_operations_load_constant(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0],fetch_basic_operations[1])
    mx_code = mx_codes[0].strip() 
    assert mx_code == codes['basic_operations'][0], f'{fetch_basic_operations[0][0]} should map to {codes["basic_operations"][0]} but instead results in {mx_code}'


def test_basic_operations_add(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0],fetch_basic_operations[1])
    mx_code = mx_codes[2].strip()
    assert mx_code == codes['basic_operations'][2], f'{fetch_basic_operations[0][2]} should map to {codes["basic_operations"][2]} but instead results in {mx_code}'


def test_basic_operations_print_register(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0],fetch_basic_operations[1])
    mx_code = mx_codes[3].strip()
    assert mx_code == codes['basic_operations'][3], f'{fetch_basic_operations[0][3]} should map to {codes["basic_operations"][3]} but instead results in {mx_code}'


def test_basic_operations_halt(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0],fetch_basic_operations[1])
    mx_code = mx_codes[6].strip()
    assert mx_code == codes['basic_operations'][6], f'{fetch_basic_operations[0][6]} should map to {codes["basic_operations"][6]} but instead results in {mx_code}'



def test_branch_not_equal(fetch_branch_not_equal):
    mx_codes = assemble_basis(fetch_branch_not_equal[0],fetch_branch_not_equal[1])
    mx_code = mx_codes[5].strip()
    assert mx_code == codes['branch_not_equal'][5], f'{fetch_branch_not_equal[0][8]} should map to {codes["branch_not_equal"][5]} but instead results in {mx_code}'


def test_branch_not_equal_load_register(fetch_branch_not_equal):
    mx_codes = assemble_basis(fetch_branch_not_equal[0],fetch_branch_not_equal[1])
    mx_code = mx_codes[3].strip()
    assert mx_code == codes['branch_not_equal'][3], f'{fetch_branch_not_equal[0][5]} should map to {codes["branch_not_equal"][3]} but instead results in {mx_code}'


def test_branch_not_equal_subtract(fetch_branch_not_equal):
    mx_codes = assemble_basis(fetch_branch_not_equal[0],fetch_branch_not_equal[1])
    mx_code = mx_codes[4].strip()
    assert mx_code == codes['branch_not_equal'][4], f'{fetch_branch_not_equal[0][7]} should map to {codes["branch_not_equal"][4]} but instead results in {mx_code}'


def test_memory_operations_copy_register(fetch_memory_operations):
    mx_codes = assemble_basis(fetch_memory_operations[0],fetch_memory_operations[1])
    mx_code = mx_codes[1].strip()
    assert mx_code == codes['memory_operations'][1], f'{fetch_memory_operations[0][1]} should map to {codes["memory_operations"][1]} but instead results in {mx_code}'


def test_memory_operations_store_register(fetch_memory_operations):
    mx_codes = assemble_basis(fetch_memory_operations[0],fetch_memory_operations[1])
    mx_code = mx_codes[2].strip()
    assert mx_code == codes['memory_operations'][2], f'{fetch_memory_operations[0][2]} should map to {codes["memory_operations"][2]} but instead results in {mx_code}'


def test_memory_operations_print_memory(fetch_memory_operations):
    mx_codes = assemble_basis(fetch_memory_operations[0],fetch_memory_operations[1])
    mx_code = mx_codes[3].strip()
    assert mx_code == codes['memory_operations'][3], f'{fetch_memory_operations[0][3]} should map to {codes["memory_operations"][3]} but instead results in {mx_code}'


def test_branch_if_equal(fetch_branch_if_equal):
    mx_codes = assemble_basis(fetch_branch_if_equal[0],fetch_branch_if_equal[1])
    mx_code = mx_codes[4].strip()
    assert mx_code == codes['branch_if_equal'][4], f'{fetch_branch_if_equal[0][5]} should map to {codes["branch_if_equal"][4]} but instead results in {mx_code}'