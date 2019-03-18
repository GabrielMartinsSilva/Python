from Bio.PDB import *

parser = PDBParser()
estrutura = parser.get_structure("1BGA", "1bga.pdb")

atomo_100 = estrutura[0]['A'][100]['CA']

atomo_101 = estrutura[0]['A'][101]['CA']

#distancia euclidiana

distancia = atomo_101 - atomo_100

print(distancia)