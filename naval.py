import os
import random
import time
#os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    grey = '\033[90m'
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

def Posicao(jg, f, v):
    while True:
        print("-> ", end="")
        p1 = input()
        p = []
        for i in range(len(p1)):
            p.append(p1[i])
        if len(p) == 2:
            if 65 <= ord(p[0]) <= 74 and 48 <= ord(p[1]) <= 57:
                col = p[0]
                p.remove(col)
                col = ord(col)
                col -= 65
                p1 = p[0]
                p1 = int(p1)
                if jg[p1][col] == '*':
                    reg = p1 + 1
                    reg2 = col + 1
                    if f == '1':
                        if v == 0:
                            for i in range(4):
                                if jg[p1][reg2] == '*':
                                    reg2 += 1
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                                    break
                            if (reg2 - col) == 5:
                                break
                        else:
                            for i in range(4):
                                if jg[reg][col] == '*':
                                    reg += 1
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                                    break
                            if (reg - p1) == 5:
                                break 
                    elif f == '2':
                        if v == 0:
                            for i in range(3):
                                if jg[p1][reg2] == '*':
                                    reg2 += 1
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                                    break
                            if (reg2 - col) == 4:
                                break
                        else:
                            for i in range(3):
                                if jg[reg][col] == '*':
                                    reg += 1
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                                    break
                            if (reg - p1) == 4:
                                break 
                    elif f == '3':
                        if v == 0:
                            for i in range(2):
                                if jg[p1][reg2] == '*':
                                    reg2 += 1
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                                    break
                            if (reg2 - col) == 3:
                                break
                        else:
                            for i in range(2):
                                if jg[reg][col] == '*':
                                    reg += 1
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                                    break
                            if (reg - p1) == 3:
                                break 
                    elif f == '4':
                        if v == 0:
                            if jg[p1][reg2] == '*':
                                break
                            else:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                        else:
                            if jg[reg][col] == '*':
                                break
                            else:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                    else:
                        break
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            print("Insira a coordenada corretamente.")
    return col, p1

def Posicionar(pf):
    lista = [1, 1, 2, 3, 4]
    for i in range(11):
        v = 0
        c = 0
        print("  A B C D E F G H I J")
        for i in range(10):
            print("%d " %i, end="")
            for j in range(10):
                print("%s " %pf[i][j], end="")
            print()
        print()
        print("Frota:")
        if lista[0] == 0:
            print(colors.grey + "[1] %dx Porta-avião (X X X X X)" %lista[0], end="")
        else:
            print("[1] %dx Porta-avião (X X X X X)" %lista[0], end="")
        if lista[3] == 0:
            print(colors.grey + "    [4] %dx Navios Comuns (X X)" %lista[3] + colors.fim) 
        else:
            print(colors.fim + "    [4] %dx Navios Comuns (X X)" %lista[3])

        if lista[1] == 0:
            print(colors.grey + "[2] %dx Navio-tanque (X X X X)" %lista[1], end="")
        else:
            print("[2] %dx Navio-tanque (X X X X)" %lista[1], end="")
        if lista[4] == 0:
            print(colors.grey + "     [5] %dx Submarinos (X)" %lista[4] + colors.fim) 
        else:
            print(colors.fim + "     [5] %dx Submarinos (X)" %lista[4]) 

        if lista[2] == 0:
            print(colors.grey + "[3] %dx Contratorpedeiros (X X X)" %lista[2] + colors.fim)
        else:
            print("[3] %dx Contratorpedeiros (X X X)" %lista[2])
        print()
        print("Selecione qual unidade posicionar")
        while True:
            fe = Escolha(5)
            if lista[fe-1] == 0:
                print("Você não possui mais esta unidade para posicionar, escolha outra")
            else:
                lista[fe-1] -= 1
                break
        while True:
            print("Como deseja posicionar sua unidade?")
            print("[1] Verticalmente  [2] Horizontalmente")
            if Escolha(2) == '1':
                v = 1
            print("Informe as coordenadas que deseja posicionar: (letra primeiro, depois o número)")
            col, lin = Posicao(pf, fe, v)
            x = lin
            y = col
            c = 6 - fe
            print("  A B C D E F G H I J")
            for i in range(10):
                print("%d " %i, end="")
                for j in range(10):
                    if i == x and j == y:
                        print(colors.yellow + "X " + colors.fim, end="")
                        c -= 1
                        if v == 0 and c != 0:
                            y += 1
                        elif v == 1 and c != 0:
                            x += 1
                    else:
                        print("%s " %pf[i][j], end="")
                print()
            print()
            print("A posição escolhida esta correta?")
            print("   [1] Sim          [2] Não")
            if Escolha(2) == '1':
                c = 6 - fe
                for i in range(10):
                    for j in range(10):
                        if i == lin and j == col:
                            pf[lin][col] = 'X'
                            c -= 1
                            if v == 0 and c != 0:
                                col += 1
                            elif v == 1 and c != 0:
                                lin += 1
                break
    

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
                f1.append([])
                f2.append([])
                jg1.append([])
                jg2.append([])
                for j in range(10):
                    f1[i].append('*')
                    f2[i].append('*')
                    jg1[i].append('*')
                    jg2[i].append('*')
            print(colors.yellow + "JOGADOR 1 POSICIONE SUA FROTA" + colors.fim)
            print()
            time.sleep(1)
            Posicionar(f1)
            #continuar pro jogador 2

            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()
