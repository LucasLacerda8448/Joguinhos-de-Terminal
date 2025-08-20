import os
import random
import time
#os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    purple = '\033[95m'
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

def EntregaCarta(ci, l):
    for i in range(9):
        l.append([])
        e = random.choice(ci)
        l[i].append(e)
        ci.remove(e)
        if e == 'X_X':
            l[i].append('M')
        else:
            l[i].append('N')
    return ci, l

def ImprimeCarta(l, n, ca):
    for i in range(n):
        print("[", end="")
        if l[0] == '#':
            print("#", end="")
        elif l[i][1] == 'N':
            print(colors.purple + "%s" %(l[i][0]) + colors.fim, end="")
        else:
            print(colors.red + "%s" %(l[i][0]) + colors.fim, end="")
        print("] ", end="")
        if (i + 1) % 5 == 0:
            print()
        if ca == 1:
            print("[" + colors.purple + "%s" %(l[i][0]) + colors.fim + "] ", end="")
    if n % 5 != 0:
        print()

def ImprimeCarta2(n):
    print("Escolha qual carta deseja pegar:")
    for i in range(n):
        print("%d:[#]  " %i, end="")
        if (i + 1) % 5 == 0:
            print()
    if n % 5 != 0:
        print()

def RemoverCarta(l, co, no, write, ce):
    if write == 0:
        l.append(co[ce])
        co[ce] = ['A', 'A']
        co.remove(['A', 'A'])
    else:
        if write == 1:
            ImprimeCarta2(no)
            while True:
                print("-> ", end="")
                e = input()
                e2 = 0
                for i in e:
                    if 48 <= ord(i) <= 57:
                        e2 = 1
                    else:
                        e2 = 0
                        break
                if e2 == 1:
                    e = int(e)
                    if e > no-1:
                        print("Número inválido.")
                    else:
                        print()
                        l.append(co[e])
                        co[e] = ['A', 'A']
                        co.remove(['A', 'A'])
                        break
        else:
            l.append(co[ce])
            co[ce] = ['A', 'A']
            co.remove(['A', 'A'])

    print(colors.yellow + "Carta Escolhida: " + colors.fim, end="")
    print("[", end="")
    if write == 0:
        print("#", end="")
    else:    
        if l[-1][1] == 'N':
            print(colors.purple + "%s" %(l[-1][0]) + colors.fim, end="")
        else:
            print(colors.red + "%s" %(l[-1][0]) + colors.fim, end="")
    print("]")
    print()
    time.sleep(1)

def AnalisaCarta(ca, l):
    n = len(l)
    l2 = []
    p = []
    for i in range(n):
        if l[i] in ca:
            continue
        c = 0
        l2.append(l[i])
        for j in range(n-i):
            if l[j+i][0] == l[i][0]:
                c += 1
                if c == 2:
                    break
        if c == 2:
            p.append(l[i])
            ca.append(l[i])
            l2.remove(l[i])
    
    if len(p) > 0:
        print(colors.yellow + "Pares Formados: " + colors.fim, end="")
        for i in p:
            print("[" + colors.purple + "%s" %i[0] + colors.fim + "] ", end="")
            print("[" + colors.purple + "%s" %i[0] + colors.fim + "] ", end="")
        print()
        print()

    return ca, l2

def TelaJogo(cc1, cc2, cj, ca):
    nc1 = len(cc1)
    nc2 = len(cc2)
    nj = len(cj)
    np = len(ca)
    cc3 = ['#']
    print("Pares Formados: ")
    ImprimeCarta(ca, np, 1)
    print()
    print(colors.green + "Cartas do Computador 1: " + colors.fim + "(%d)" %nc1)
    if nc1 != 0:
        ImprimeCarta(cc3, nc1, 0)
    print()
    print(colors.blue + "Cartas do Computador 2: " + colors.fim + "(%d)" %nc2)
    if nc2 != 0:
        ImprimeCarta(cc3, nc2, 0)
    print()
    print(colors.red + "Suas Cartas: " + colors.fim + "(%d)" %nj)
    if nj != 0:
        ImprimeCarta(cj, nj, 0)

def VezJogador(cc1, cc2, cj, ca, v, g, p):
    TelaJogo(cc1, cc2, cj, ca)
    print()
    nc1 = len(cc1)
    nc2 = len(cc2)
    if nc1 > 0 and nc2 > 0:
        print("Deseja pegar uma carta do Computador 1 ou 2?")
        print("[1] Computador 1       [2] Computador 2")
        if Escolha(2) == '1':
            RemoverCarta(cj, cc1, nc1, 1, -1)
        else:
            RemoverCarta(cj, cc2, nc2, 1, -1)
    elif nc1 > 0:
        print(colors.yellow + "O Computador 2 não possui mais cartas. Portanto, pegue as cartas do Computador 1." + colors.fim)
        RemoverCarta(cj, cc1, nc1, 1, -1)
    else:
        print(colors.yellow + "O Computador 1 não possui mais cartas. Portanto, pegue as cartas do Computador 2." + colors.fim)
        RemoverCarta(cj, cc2, nc2, 1, -1)

    nc1 = len(cc1)
    nc2 = len(cc2)
    if nc1 == 0:
        if g == 3:
            g = 1
        elif g != 1:
            p = 0
            v = 3
    if nc2 == 0:
        if g == 3:
            g = 2
        elif g != 2:
            p = 0
            v = 3

    ca, cj = AnalisaCarta(ca, cj)
    nj = len(cj)
    if nj == 0:
        if g == 3:
            g = 0
            v = 1
        elif g == 1:
            p = 2
            v = 3
        else:
            p = 1
            v = 3
    else:
        if nc1 != 0 and nc2 != 0:
            v = 1
        elif nc1 != 0:
            v = 1
        elif nc2 != 0:
            v = 2

    print("Aperte Enter para continuar...")
    cont = input()
    if v == 1:
        print(colors.green + "VEZ DO COMPUTADOR 1." + colors.fim)
        print()
        time.sleep(1.2)
    elif v == 2:
        print(colors.blue + "VEZ DO COMPUTADOR 2." + colors.fim)
        print()
        time.sleep(1.2)
    return cc1, cc2, cj, v, g, p

def VezComputador(cc1, cc2, cj, ca, v, g, p):
    TelaJogo(cc1, cc2, cj, ca)
    print()
    if v == 1:
        nj = len(cj)
        nc2 = len(cc2)
        if nj > 0 and nc2 > 0:
            e = random.randint(1, 2)
            if e == 1:
                print(colors.green + "O Computador 1 irá pegar uma carta do Jogador." + colors.fim)
                r = random.randint(0, nj-1)
                RemoverCarta(cc1, cj, nj, 2, r)
            else:
                print(colors.green + "O Computador 1 irá pegar uma carta do Computador 2." + colors.fim)
                r = random.randint(0, nc2-1)
                RemoverCarta(cc1, cc2, nc2, 0, r)
        elif nj > 0:
            print(colors.green + "O Computador 1 irá pegar uma carta do Jogador." + colors.fim)
            r = random.randint(0, nj-1)
            RemoverCarta(cc1, cj, nj, 2, r)
        else:
            print(colors.green + "O Computador 1 irá pegar uma carta do Computador 2." + colors.fim)
            r = random.randint(0, nc2-1)
            RemoverCarta(cc1, cc2, nc2, 0, r)

        nj = len(cj)
        nc2 = len(cc2)
        if nj == 0:
            if g == 3:
                g = 0
            elif g != 0:
                p = 1
                v = 3
        if nc2 == 0:
            if g == 3:
                g = 2
            elif g != 2:
                p = 1
                v = 3

        ca, cc1 = AnalisaCarta(ca, cc1)
        nc1 = len(cc1)
        if nc1 == 0:
            if g == 3:
                g = 1
                v = 2
            elif g == 0:
                p = 2
                v = 3
            else:
                p = 0
                v = 3
        else:
            if nj != 0 and nc2 != 0:
                v = 2
            elif nc2 != 0:
                v = 2
            elif nj != 0:
                v = 0

        print("Aperte Enter para continuar...")
        cont = input()
        if v == 0:
            print(colors.red + "VEZ DO JOGADOR." + colors.fim)
            print()
            time.sleep(1)
        elif v == 2:
            print(colors.blue + "VEZ DO COMPUTADOR 2." + colors.fim)
            print()
            time.sleep(1.2)

    elif v == 2:
        nj = len(cj)
        nc1 = len(cc1)
        if nj > 0 and nc1 > 0:
            e = random.randint(1, 2)
            if e == 1:
                print(colors.blue + "O Computador 2 irá pegar uma carta do Jogador." + colors.fim)
                r = random.randint(0, nj-1)
                RemoverCarta(cc2, cj, nj, 2, r)
            else:
                print(colors.blue + "O Computador 2 irá pegar uma carta do Computador 1." + colors.fim)
                r = random.randint(0, nc1-1)
                RemoverCarta(cc2, cc1, nc1, 0, r)
        elif nj > 0:
            print(colors.blue + "O Computador 2 irá pegar uma carta do Jogador." + colors.fim)
            r = random.randint(0, nj-1)
            RemoverCarta(cc2, cj, nj, 2, r)
        else:
            print(colors.blue + "O Computador 2 irá pegar uma carta do Computador 1." + colors.fim)
            r = random.randint(0, nc1-1)
            RemoverCarta(cc2, cc1, nc1, 0, r)

        nj = len(cj)
        nc1 = len(cc1)
        if nj == 0:
            if g == 3:
                g = 0
            elif g != 0:
                p = 2
                v = 3
        if nc1 == 0:
            if g == 3:
                g = 1
            elif g != 1:
                p = 2
                v = 3

        ca, cc2 = AnalisaCarta(ca, cc2)
        nc2 = len(cc2)
        if nc2 == 0:
            if g == 3:
                g = 2
                v = 0
            elif g == 0:
                p = 1
                v = 3
            else:
                p = 0
                v = 3
        else:
            if nj != 0 and nc1 != 0:
                v = 0
            elif nj != 0:
                v = 0
            elif nc1 != 0:
                v = 1

        print("Aperte Enter para continuar...")
        cont = input()
        if v == 0:
            print(colors.red + "VEZ DO JOGADOR." + colors.fim)
            print()
            time.sleep(1)
        elif v == 1:
            print(colors.green + "VEZ DO COMPUTADOR 1." + colors.fim)
            print()
            time.sleep(1)

    return cc1, cc2, cj, v, g, p

def main():
    print("----- JOGO DOS EMOJIS -----")
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
            print(colors.yellow + "DISTRIBUINDO AS CARTAS..." + colors.fim)
            print()
            time.sleep(1.2)
            ci = ['X_X', ':)', ':)', ':(', ':(', 'UwU', 'UwU', 'OwO', 'OwO', ':3', ':3', '-_-', '-_-', ':O',
                  ':O', '._.', '._.', '^-^', '^-^', 'Ò_Ó', 'Ò_Ó', '>_<', '>_<', ':D', ':D', 'B)', 'B)']
            cc1 = []
            cc2 = []
            cj = []
            ca = []
            ci, cj = EntregaCarta(ci, cj)
            ci, cc1 = EntregaCarta(ci, cc1)
            ci, cc2 = EntregaCarta(ci, cc2)
            v = 0
            p = 3
            g = 3
            TelaJogo(cc1, cc2, cj, ca)
            print()
            print(colors.yellow + "RETIRANDO OS PARES JÁ FORMADOS..." + colors.fim)
            print()
            time.sleep(1.2)
            ca, cj = AnalisaCarta(ca, cj)
            ca, cc1 = AnalisaCarta(ca, cc1)
            ca, cc2 = AnalisaCarta(ca, cc2)
            print("Aperte Enter para continuar...")
            cont = input()
            print(colors.red + "O JOGADOR COMEÇA." + colors.fim)
            print()
            while p == 3:
                if v == 0:
                    cc1, cc2, cj, v, g, p = VezJogador(cc1, cc2, cj, ca, v, g, p)
                elif v == 1:
                    cc1, cc2, cj, v, g, p = VezComputador(cc1, cc2, cj, ca, v, g, p)
                elif v == 2:
                    cc1, cc2, cj, v, g, p = VezComputador(cc1, cc2, cj, ca, v, g, p)
            print(colors.yellow + "FIM DE JOGO!" + colors.fim)
            print()
            TelaJogo(cc1, cc2, cj, ca)
            print()
            if g == 0:
                print(colors.red + "O JOGADOR VENCEU." + colors.fim)
            elif g == 1:
                print(colors.green + "O COMPUTADOR 1 VENCEU." + colors.fim)
            elif g == 2:
                print(colors.blue + "O COMPUTADOR 2 VENCEU." + colors.fim)
            if p == 0:
                print(colors.red + "E O JOGADOR PERDEU." + colors.fim)
            elif p == 1:
                print(colors.green + "E O COMPUTADOR 1 PERDEU." + colors.fim)
            elif p == 2:
                print(colors.blue + "E O COMPUTADOR 2 PERDEU." + colors.fim)
            print()
            time.sleep(1)
            
            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()
            
main()
