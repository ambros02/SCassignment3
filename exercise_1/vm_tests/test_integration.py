


import sys
import os
from unittest.mock import patch
from io import StringIO
import pytest


same_parent = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
parent_of_files = os.path.join(same_parent,'vm')
sys.path.append(parent_of_files)

import vm
import assembler



@pytest.fixture
def parent_dir():
    return os.path.dirname(os.path.dirname(__file__))



def test_integration_assembler(parent_dir):

    output = StringIO()
    original_flow = sys.stdout
    sys.stdout = output
    with patch("sys.argv",["file.py",os.path.join(parent_dir,"test_files","integration.as"),"-"]):
        assembler.main(assembler.Assembler)
        
    sys.stdout = original_flow
    
    with open(os.path.join(parent_dir,"test_files","integration.mx")) as f:
        assert "".join(f.readlines()) == output.getvalue()





def test_integration_vm(parent_dir):
    #will print the show and reg to the file
    expected = ["R000000 = 000003","R000001 = 000002","R000002 = 000000","R000003 = 000000","000000:   010002  020102  010006  00000a","000004:   000001  000000  000000  000000"]
    location = os.path.join(parent_dir,"test_files","results.txt")

    with patch("sys.argv",["file.py",os.path.join(parent_dir,"test_files","integration.mx"),location]):    
        vm.main(vm.VirtualMachine)
    
    with open(location) as f:
        result = f.read()
    os.remove(location)
    assert result.strip() == "\n".join(expected)

