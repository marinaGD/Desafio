import sys
import Desafios


def main():
    desaf = Desafios.ConversaDesafios()
    numeroDesafio = 0
    while numeroDesafio < 5:
        numeroDesafio = input("Escolha um numero de 1 a 4 para testar, outros valores para sair\n")
        if numeroDesafio == 1:
            desaf.respondePrimeiroDesafio()
        elif numeroDesafio == 2:
            desaf.respondeSegundoDesafio()
        elif numeroDesafio==3:
            desaf.respondeTerceiroDesafio()
        elif numeroDesafio == 4:
            desaf.respondeQuartoDesafio()


if __name__ == "__main__":
    main()