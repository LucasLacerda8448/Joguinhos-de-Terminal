#CÓDIGO DESATUALIZADO

import time
import subprocess
caminho = ".\\programas\\"

def Escolha(n):
    e = 0
    l = []
    for i in range(1, n+1):
        l.append(str(i))
    while e not in l:
        print("-> ", end="")
        e = input()
    print()
    return e

print("INICIANDO PROGRAMA...")
print()
time.sleep(1.3)
while True:
    print("============== MENU DE JOGOS ==============")
    print("[1] Jogo da Velha       [2] Jogo da Memória")
    print("[3] Jogo da Sequência   [4] UNO!")
    print("[5] Connect-4           [6] Campo Minado")
    print("[7] Rolagem de Dados    [8] Sudoku")
    print("                 [9] Sair")
    print("===========================================")
    e3 = Escolha(9)
    if e3 == '9':
        print("ENCERRANDO PROGRAMA...")
        break
    else:
        print("INICIANDO O JOGO...")
        print()
        time.sleep(1.2)
        if e3 == '1':
            subprocess.run(["python", caminho + "velha.py"])
        elif e3 == '2':
            subprocess.run(["python", caminho + "memoria.py"])
        elif e3 == '3':
            subprocess.run(["python", caminho + "sequencia.py"])
        elif e3 == '4':
            subprocess.run(["python", caminho + "UNO.py"])
        elif e3 == '5':
            subprocess.run(["python", caminho + "connect.py"])
        elif e3 == '6':
            subprocess.run(["python", caminho + "mina.py"])
        elif e3 == '7':
            subprocess.run(["python", caminho + "dice.py"])
        elif e3 == '8':
            subprocess.run(["python", caminho + "sudoku.py"])    
        print()
        time.sleep(1.2)
