# Oscar AG - 2024

from enum import Enum

import random

class Choices(Enum):
    PIEDRA = 'piedra'
    PAPEL = 'papel'
    TIJERAS = 'tijeras'

    def randomize():
        '''
        Covertir `Choices` a una lista y elegir un valor aleatorio de la lista 
        '''
        return random.choice(list(Choices))
    
class State(Enum):
    USER = 'Ganaste'
    COMPUTER = 'Perdiste'
    DRAW = 'Empate'