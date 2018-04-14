# -*- coding: utf-8 -*-
from random import randint
import sys
import StringIO
from math import sqrt

class FuncoesDesafios(object):

    def encontraValorNaLista(self, valor, listadevalores, posicaoLista):
        meio = int(round(len(listadevalores))/2)
        if valor > listadevalores[len(listadevalores)-1] or valor < listadevalores[0]:
            return "O numero nao existe na lista"
        if listadevalores[meio] == valor:
            return posicaoLista + meio
        elif (listadevalores[meio]) > valor:
            return self.encontraValorNaLista(valor, listadevalores[:meio], posicaoLista + 0)
        elif (listadevalores[meio]) < valor:
            return self.encontraValorNaLista(valor, listadevalores[meio:len(listadevalores)], posicaoLista + meio)

    def encontraValoresEmComum(self):
        listaMenor = set(randint(0, 5000000) for x in range(500))
        listaMaior = set(randint(0, 5000000) for x in range(50000))
        listaIntersec = listaMaior.intersection(listaMenor)
        return listaIntersec

    def encontraPrimos(self, valor):
        listaPrimos = [2, ]
        for numero in xrange(3, valor + 1, 2):
            ehprimo = 1
            for i in listaPrimos:
                if numero % i == 0:
                    ehprimo = 0
                    break
                if i > sqrt(numero):
                    break
            if (ehprimo):
                listaPrimos.append(numero)
        return listaPrimos

    def isPalavraPrima(self, palavra):
        numeroDaPalavra = self.getNumeroDaPalavra(palavra)
        if self.ehPrimo(numeroDaPalavra) == 0:
            return "A palavra nao eh prima"
        else:
            return "A palavra eh prima"

    def getNumeroDaPalavra(self, palavra):
        global numero
        numero = 0
        char2numero = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
                       'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
                       'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 25, 'B': 28, 'C': 29, 'D': 30, 'E': 31,
                       'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41,
                       'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51,
                       'Z': 52}
        for char in palavra:
            if char2numero.has_key(char):
                numero = numero + int(char2numero.get(char))
        return numero

    def ehPrimo(self, numero):
        ehPrimo = 1
        if numero < 2:
            ehPrimo = 0
        else:
            for i in xrange(3, int(sqrt(numero)), 2):
                if numero % i == 0:
                    ehPrimo = 0
                    break
        return ehPrimo


class ConversaDesafios(object):
    global funcoesD
    funcoesD = FuncoesDesafios()

    def respondePrimeiroDesafio(self):
        lista = [randint(0, 100) for x in range(300)]
        lista.sort()
        numero = input("Escreva o numero a ser encontrado\n")
        posicao = funcoesD.encontraValorNaLista(numero, lista, 0)
        print("A primeira ocorrencia do numero eh no indice: " + str(posicao))

    def respondeSegundoDesafio(self):
        numero = input("Escreva um numero, serao retornados todos os primos ate ele\n")
        lista = funcoesD.encontraPrimos(numero)
        print(lista)

    def respondeTerceiroDesafio(self):
        print list(funcoesD.encontraValoresEmComum())

    def respondeQuartoDesafio(self):
        print("Escreva uma palavra para saber se ela é prima\n")
        print(funcoesD.isPalavraPrima(raw_input()))

