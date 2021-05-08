"""
3D alignment of multiple structure using Kabsh algorithm. All PDB structures must be in the separate files in single directory.

usage:
chimera --nogui --script "~/bin/misc/chimera_match.py /absolute/path/with/trailing/slash/"
"""

from chimera import openModels
from chimera import runCommand as rc
from Midas import match, write
import sys
from os import listdir
from os.path import isfile, join


path = sys.argv[1]

onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) if f.endswith('.pdb')]
onlyfiles.sort()
ref_filename = path + onlyfiles[0]
ref = openModels.open(ref_filename)[0]

for i in onlyfiles[1:]:
    filename = path + i
    model = openModels.open(filename)[0]
    _, _ , rmsd, _ = match(model.atoms, ref.atoms)
    write(model, ref, filename)
    rc('close #1')

