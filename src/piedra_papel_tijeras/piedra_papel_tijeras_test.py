# Oscar AG - 2024

from definitions import *

from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    '''
    Test para la función ordenador_decide_jugada.
    '''
    print("Testeando ordenador_decide_jugada...")
    eleccion = ordenador_decide_jugada()
    print("El ordenador eligió: {}".format(eleccion))

def test_usuario_decide_jugada():
    '''
    Test para la función usuario_decide_jugada.
    '''
    print("Testeando usuario_decide_jugada...")
    eleccion = usuario_decide_jugada()
    print("El usuario eligió: {}".format(eleccion))

def test_determina_ganador(user: Choices, computer: Choices):
    '''
    Test para la función determina_ganador.
    '''
    print("Testeando determina_ganador...")
    print("Jugador: {}, vs. Ordenador: {}".format(user, computer))
    resultado = determina_ganador(user, computer)
    print("Resultado: {}\n".format(resultado))
    print()

if __name__ == "__main__":
    test_ordenador_decide_jugada()
    test_usuario_decide_jugada()
    test_determina_ganador(Choices.PIEDRA, Choices.TIJERAS)
    test_determina_ganador(Choices.PIEDRA, Choices.PAPEL)
    test_determina_ganador(Choices.PIEDRA, Choices.PIEDRA)
    test_determina_ganador(Choices.TIJERAS, Choices.TIJERAS)
    test_determina_ganador(Choices.TIJERAS, Choices.PAPEL)
    test_determina_ganador(Choices.TIJERAS, Choices.PIEDRA)
    test_determina_ganador(Choices.PAPEL, Choices.TIJERAS)
    test_determina_ganador(Choices.PAPEL,Choices.PAPEL)
    test_determina_ganador(Choices.PAPEL, Choices.PIEDRA)