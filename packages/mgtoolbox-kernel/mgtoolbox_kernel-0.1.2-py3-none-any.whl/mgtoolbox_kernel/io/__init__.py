from pathlib import Path
from typing import Dict, List, Union
from mgtoolbox_kernel.io.cif import CifFileParse
from mgtoolbox_kernel.io.vasp.poscar import PoscarParse



def read_structure_file(
    filename:Union[str,Path]
) -> Union[Dict[str, Union[str, float]], List[Dict[str, Union[str, float]]]]:
    path = Path(filename)
    if path.suffix == '.cif':
        cifparse = CifFileParse()
        cifparse.read_file(str(path))
        return cifparse.get_structures()
    elif path.suffix == '.vasp' or path.name == 'POSCAR':
        structs = []
        structs.append(PoscarParse(str(path)).get_structure())
        return structs
    structs = []
    structs.append(PoscarParse(filename).get_structure())
    return structs

def read_structure_data(file_data):
    cifparse = CifFileParse()
    cifparse.read_file(file_data)
    return cifparse.get_structures()
