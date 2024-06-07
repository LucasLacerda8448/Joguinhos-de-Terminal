import os
import random
import time
#os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    fim = '\033[0m'

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

def Posicionar(pf):
    lista = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
    print("Frota:")
    print("[1] 1x Porta-avião (X X X X X)    [4] 3x Navios Comuns (X X)")
    print("[2] 1x Navio-tanque (X X X X)     [5] 4x Submarinos (X)")
    print("[3] 2x Contratorpedeiros (X X X)")
    print()
    print("  A B C D E F G H I J")
    for i in range(10):
        print("%d " %i, end="")
        pf.append([])
        for j in range(10):
            pf[i].append('*')
            print("%s " %pf[i][j], end="")
        print()
    print()

def main():
    print("------ BATALHA NAVAL ------")
    print()
    while True:
        print("========= OPÇÕES =========")
        print("[1] Jogar   [2] Instruções")
        print("        [3] Sair")
        e = Escolha(3)
        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        elif e == '2':
            print("========== INSTRUÇÕES ==========")
            print()
            print("- Neste jogo de UNO algumas das cartas podem ter símbolos diferentes do habitual.")
            print("- Aqui está uma explicação de cada uma:")
            print("  [0-9]: Cartas númericas comuns, vão de 0 a 9;")
            print("  [+2]: Carta +2, faz o próximo jogar comprar 2 cartas;")
            print("  [X]: Carta de Bloqueio, bloqueia a vez do próximo jogador;")
            print("  [+4]: Carta +4, o jogador escolhe a próxima cor a jogarem e faz o próximo jogador")
            print("  comprar 4 cartas;")
            print("  [////]: Carta de Troca de Cor, o jogador escolhe a próxima cor a jogarem;")
            print("- A carta que inverte a ordem do jogo não foi implementada, pois ela teria o mesmo")
            print("  efeito que uma carta de bloqueio;")
            print("- Quando for escolher a próxima carta a jogar, escolha o número ao lado dela, invés do símbolo;")
            print("- Caso o jogador esteja de UNO, ele não poderá finalizar um jogo com cartas coringa,")
            print("  isto é, [+4] ou [////];")
            print()
        elif e == '1':
            f1 = []
            f2 = []
            jg1 = []
            jg2 = []
            for i in range(10):
                jg1.append([])
                jg2.append([])
                for j in range(10):
                    jg1[i].append('*')
                    jg2[i].append('*')
            print(colors.yellow + "JOGADOR 1 POSICIONE SUA FROTA" + colors.fim)
            print()
            time.sleep(1)
            Posicionar(f1)

            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()
