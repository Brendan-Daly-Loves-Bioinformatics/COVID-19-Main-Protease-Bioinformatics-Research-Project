from modeller import environ

env = environ()
print("Modeller successfully imported in PyCharm!")

from modeller import environ
from modeller.automodel import automodel

env = environ()
env.io.atom_files_directory = ['.']  # current directory

a = automodel(env,
              alnfile='alignment.ali',
              knowns='WT_clean',          # name in alignment
              sequence='Mut_clean',    # mutant target
              assess_methods=None)

a.starting_model = 1
a.ending_model = 1

a.make()
print("Modeling complete! Check mutant.B99990001.pdb")
