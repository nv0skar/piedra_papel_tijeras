# Oscar AG - 2024

from definitions import *

from piedra_papel_tijeras import *

if __name__ == '__main__': 
    if input("Torneo? (Si) ").lower() == "si": jugar_torneo()
    else: jugar()
