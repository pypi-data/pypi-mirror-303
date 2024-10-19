import json
import subprocess
from typing import List

def cell_runner(file_name: str, cell_idx: int):
    if not file_name.endswith("ipynb"):
        raise NameError("File must be a .ipynb file")
    try:
        with open(file_name) as f:
            json_data = json.load(f)
    except json.JSONDecodeError or AttributeError:
        raise ValueError("File is corrupted. Retry with a valid file.")

    code_cell_indices = get_code_cell_indices(json_data)
    if cell_idx not in code_cell_indices:
        raise ValueError("Cell index is out of range. Please check the cell index. (Index starts from 0)")

    cell_code_list = json_data["cells"][cell_idx]["source"]
    cell_code = "".join(cell_code_list)
    subprocess.run(["python", "-c", cell_code])


def get_code_cell_indices(json_var) -> List[int]:
    indices_of_code_cells = []
    for i, cell in enumerate(json_var["cells"]):
        if cell.get('cell_type') == "code":
            indices_of_code_cells.append(i)
    return indices_of_code_cells


# Add a main function for CLI use
def main():
    import argparse
    parser = argparse.ArgumentParser(description='Run a code cell from an IPython notebook.')
    parser.add_argument('file_name', type=str, help='.ipynb file path')
    parser.add_argument('cell_idx', type=int, help='Cell index to run')

    args = parser.parse_args()
    cell_runner(args.file_name, args.cell_idx)

if __name__ == "__main__":
    main()
