# Oscar AG - 2024

from definitions import *

import os

def ordenador_decide_jugada() -> Choices:
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    return Choices.randomize()

def usuario_decide_jugada() -> Choices:
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    while True:
        user_choice = input('\033[1;33m\033[5mElige piedra, papel o tijeras >>\033[0m ')
        try:
            return Choices(user_choice.lower())
        except:
            print("{} no es una elección valida!".format(user_choice))

def determina_ganador(user: Choices, randomized: Choices) -> State:
    if (not isinstance(user, Choices) or not isinstance(randomized, Choices)): raise TypeError
    if user == randomized:
        return State.DRAW
    elif (user == Choices.PIEDRA and randomized == Choices.TIJERAS) or (user == Choices.TIJERAS and randomized == Choices.PAPEL) or (user == Choices.PAPEL and randomized == Choices.PIEDRA):
        return State.USER
    else:
        return State.COMPUTER

def jugar():
    print('\033[4m\033[36mPIEDRA, PAPEL & TIJERAS\033[0m')
    computer = ordenador_decide_jugada()
    user = usuario_decide_jugada()
    state = determina_ganador(user, computer)
    print('Usuario: {} vs. Ordernador: {}... \033[1m\033[1;35m{}\033[0m'.format(user.value, computer.value, state.value.upper()))

def jugar_torneo():
    print('\033[4m\033[36mPIEDRA, PAPEL & TIJERAS (MODO TORNEO)\033[0m')
    (user_points, computer_points) = (0, 0)
    while (user_points != 3 and computer_points != 3):
        computer = ordenador_decide_jugada()
        user = usuario_decide_jugada()
        state = determina_ganador(user, computer)
        if state == State.USER: user_points +=1
        elif state == State.COMPUTER: computer_points += 1
        print('Usuario: {} vs. Ordernador: {}... \033[1m\033[1;35m{}\033[0m'.format(user.value, computer.value, state.value.upper()))
        print('Usuario - \033[1m{}\033[0m & Ordenador - \033[1m{}\033[0m'.format(user_points, computer_points))
    print("Tenemos ganador... Felcidades \033[1m\033[1;35m{}\033[0m".format("JUGADOR" if user_points == 3 else "ORDENADOR"))
    if user_points == 3:
        while True:
            try: os.system("say -r 200 'Has ganado!!!'")
            except KeyboardInterrupt: exit() 
    else:
        while True:
            try: os.system("say -r 200 'Has perdido!!!'")
            except KeyboardInterrupt: exit() 
