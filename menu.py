import time
import subprocess
caminho = ".\\programas\\"

print("INICIANDO PROGRAMA...")
print()
time.sleep(1.3)
while True:
    print("============== MENU DE JOGOS ==============")
    print("[1] Jogo da Velha       [2] Jogo da Memória")
    print("[3] Jogo da Sequência   [4] UNO!")
    print("[5] Connect-4           [6] Sair")
    print("===========================================")
    e3 = 0
    while '1' != e3 != '2' and '3' != e3 != '4' and '5' != e3 != '6':
        print("-> ", end="")
        e3 = input()
    print()
    if e3 == '6':
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
        print()
        time.sleep(1.2)
