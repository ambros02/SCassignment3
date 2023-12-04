import sys
import os
import pytest


high_parent = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
parent_of_files = os.path.join(high_parent,'vm')
sys.path.append(parent_of_files)

from assembler import Assembler



def parent_dir():
    return os.path.dirname(os.path.dirname(__file__))

def file_path(file_name):
    #get the file path for a test file
    parent = parent_dir()
    full_path = os.path.join(parent,"test_files",file_name)
    return full_path

def assemble_basis(lines):
    #return the assembled code in a list
    asbler = Assembler()
    program = asbler.assemble(lines)
    return program




@pytest.fixture
def fetch_basic_operations():
    #get the operations from the basic_operations file 
    abs_path_file = file_path("basic_operations.as")
    with open(abs_path_file, 'r') as f:
        instructions = f.readlines()
    par = parent_dir()
    location = os.path.join(par,'test_files','basic_operations.mx')
    return instructions,location


@pytest.fixture
def fetch_branch_not_equal():
    #get the operations from the branch_not_equal file
    abs_path_file = file_path("branch_not_equal.as")
    with open(abs_path_file, 'r') as f:
        instructions = f.readlines()
    par = parent_dir()
    location = os.path.join(par,'test_files','branch_not_equal.mx')
    return instructions,location


@pytest.fixture
def fetch_memory_operations():
    #get the operations from the memory_operations file
    abs_path_file = file_path("memory_operations.as")
    with open(abs_path_file, 'r') as f:
        instructions = f.readlines()
    par = parent_dir()
    location = os.path.join(par,'test_files','memory_operations.mx')
    return instructions,location


@pytest.fixture
def fetch_branch_if_equal():
    #get the operations from the branch_if_equal file
    abs_path_file = file_path("branch_if_equal.as")
    with open(abs_path_file, 'r') as f:
        instructions = f.readlines()
    par = parent_dir()
    location = os.path.join(par,'test_files','branch_if_equal.mx')
    return instructions,location




#manually calculated output of the .as files when they're run through the assembler.

codes = {'basic_operations':['010002','020102','010006','00000a','320302','030005','000001'],
         'branch_not_equal':['010202','010002','320202','030103','000106', '000207','030209','030105','000001'],
         'memory_operations':['100102','000104','000105','00000b','000001'],
         'branch_if_equal':['000001','010101','000201','010206','030208','320202','030205']}



#tests use the respective fixture to get the contents of the file and then use the assemble basis helper function
# to get the assembled code which then is compared to the manually calculated code.




def test_basic_operations_load_constant(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0])
    mx_code = mx_codes[0].strip() 
    assert mx_code == codes['basic_operations'][0], f'{fetch_basic_operations[0][0]} should map to {codes["basic_operations"][0]} but instead results in {mx_code}'


def test_basic_operations_add(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0])
    mx_code = mx_codes[2].strip()
    assert mx_code == codes['basic_operations'][2], f'{fetch_basic_operations[0][2]} should map to {codes["basic_operations"][2]} but instead results in {mx_code}'


def test_basic_operations_print_register(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0])
    mx_code = mx_codes[3].strip()
    assert mx_code == codes['basic_operations'][3], f'{fetch_basic_operations[0][3]} should map to {codes["basic_operations"][3]} but instead results in {mx_code}'


def test_basic_operations_halt(fetch_basic_operations):
    mx_codes = assemble_basis(fetch_basic_operations[0])
    mx_code = mx_codes[6].strip()
    assert mx_code == codes['basic_operations'][6], f'{fetch_basic_operations[0][6]} should map to {codes["basic_operations"][6]} but instead results in {mx_code}'




def test_branch_not_equal(fetch_branch_not_equal):
    mx_codes = assemble_basis(fetch_branch_not_equal[0])
    mx_code = mx_codes[5].strip()
    assert mx_code == codes['branch_not_equal'][5], f'{fetch_branch_not_equal[0][8]} should map to {codes["branch_not_equal"][5]} but instead results in {mx_code}'


def test_branch_not_equal_load_register(fetch_branch_not_equal):
    mx_codes = assemble_basis(fetch_branch_not_equal[0])
    mx_code = mx_codes[3].strip()
    assert mx_code == codes['branch_not_equal'][3], f'{fetch_branch_not_equal[0][5]} should map to {codes["branch_not_equal"][3]} but instead results in {mx_code}'


def test_branch_not_equal_subtract(fetch_branch_not_equal):
    mx_codes = assemble_basis(fetch_branch_not_equal[0])
    mx_code = mx_codes[4].strip()
    assert mx_code == codes['branch_not_equal'][4], f'{fetch_branch_not_equal[0][7]} should map to {codes["branch_not_equal"][4]} but instead results in {mx_code}'




def test_memory_operations_copy_register(fetch_memory_operations):
    mx_codes = assemble_basis(fetch_memory_operations[0])
    mx_code = mx_codes[1].strip()
    assert mx_code == codes['memory_operations'][1], f'{fetch_memory_operations[0][1]} should map to {codes["memory_operations"][1]} but instead results in {mx_code}'


def test_memory_operations_store_register(fetch_memory_operations):
    mx_codes = assemble_basis(fetch_memory_operations[0])
    mx_code = mx_codes[2].strip()
    assert mx_code == codes['memory_operations'][2], f'{fetch_memory_operations[0][2]} should map to {codes["memory_operations"][2]} but instead results in {mx_code}'


def test_memory_operations_print_memory(fetch_memory_operations):
    mx_codes = assemble_basis(fetch_memory_operations[0])
    mx_code = mx_codes[3].strip()
    assert mx_code == codes['memory_operations'][3], f'{fetch_memory_operations[0][3]} should map to {codes["memory_operations"][3]} but instead results in {mx_code}'




def test_branch_if_equal(fetch_branch_if_equal):
    mx_codes = assemble_basis(fetch_branch_if_equal[0])
    mx_code = mx_codes[4].strip()
    assert mx_code == codes['branch_if_equal'][4], f'{fetch_branch_if_equal[0][5]} should map to {codes["branch_if_equal"][4]} but instead results in {mx_code}'


