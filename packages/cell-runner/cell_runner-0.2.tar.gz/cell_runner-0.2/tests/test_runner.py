import pytest
import json
import io
from cell_runner.runner import cell_runner, get_code_cell_indices

# Test for checking if the file is not a Jupyter notebook
def test_invalid_file_type():
    with pytest.raises(NameError, match="File must be a .ipynb file"):
        cell_runner("example.txt", 0)


# Test for checking cell index out of range
def test_cell_index_out_of_range():
    # Ensure valid.ipynb exists in the root directory
    valid_json_data = {
        "cells": [
            {"cell_type": "code", "source": ["print('Cell 1')"]},
            {"cell_type": "code", "source": ["print('Cell 2')"]}
        ]
    }
    
    # You may want to write this data to a file before running the test
    with open("valid.ipynb", "w") as f:
        json.dump(valid_json_data, f)

    with pytest.raises(ValueError, match="Cell index is out of range"):
        cell_runner("valid.ipynb", 3)


# Test for getting code cell indices
def test_get_code_cell_indices():
    notebook_data = {
        "cells": [
            {"cell_type": "code", "source": ["print('Hello World')"]},
            {"cell_type": "markdown", "source": ["# This is a markdown"]},
            {"cell_type": "code", "source": ["print('Another code cell')"]}
        ]
    }
    indices = get_code_cell_indices(notebook_data)
    assert indices == [0, 2]  # Code cells are at index 0 and 2
