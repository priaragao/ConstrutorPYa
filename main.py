# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#estrutura
#imports - bibliotecas
import pytest

#class - classes


#definitions - definicoes = metodos e funcoes

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def somar(a,b):
    return a+b

def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return 'Não divide por 0'

#Teste unitarios / Teste de unidades
# Teste da funcao somar
def test_somar_didatico():
    # 1- Configura / Prepara
    a = 8 #input
    b = 3 #input
    resultado_esperado = 11 #output

    #2- Executa
    resultado_atual = somar(a,b)

    #3- Check / Valida
    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('num1,num2,resultado',[
    #valores
    (5,4,9), #teste1
    (3,2,5), #teste2
    (10,6,16) #teste3

])

def test_somar(num1,num2,resultado):
    assert somar(num1,num2) == resultado


# TDD: Desenvolvimento Direcionado pelo Teste
# Criar o esqueleto de classes, funções e métodos logo no inicio da Sprint
# Criar pelo menos 1 teste (feliz) para todas as funcoes e metodos
# Executar todos os testes unitarios diariamente para medir o progresso

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Priscilla')

    resultado = somar(4,3)
    print(f'O resultado da soma: {resultado}')
    resultado = dividir(10, 5)
    print(f'O resultado da divisao: {resultado}')
    resultado = dividir(10, 0)
    print(f'O resultado da divisao: {resultado}')
    resultado = dividir(2, 5)
    print(f'O resultado da divisao: {resultado}')