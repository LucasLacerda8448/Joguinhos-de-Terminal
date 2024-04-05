import os
import random
import time
os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    fim = '\033[0m'

def EntregaCarta(l, n, inicio):
    lc = ['0', '1', '+2', '2', '3', '+4', '4', '5', 'X', '6', '7', '////', '8', '9']
    c = ['R', 'G', 'Y', 'B']
    t = len(l)
    compra = []
    for i in range(n):
        l.append([])
        e = random.choice(lc)
        l[i + t].append(e)
        if '////' != e != '+4':
            l[i + t].append(random.choice(c))
        elif e == '////':
            l[i + t].append('M')
        else:
            l[i + t].append('N')
        compra.append(l[i + t])
    if inicio == 0:
        print("Cartas compradas: ", end="")
        ImprimeCarta(compra, n)
        print()
    return l

def ImprimeCarta(l, n):
    for i in range(n):
        print("[", end="")
        if l[0] == '#':
            print("#", end="")
        elif l[i][1] == 'M':
            print(colors.red + "/" + colors.blue + "/" + colors.green + "/" + colors.yellow + "/" + colors.fim, end="")
        elif l[i][1] == 'N':
            print("%s" %(l[i][0]), end="")
        else:
            if l[i][1] == 'R':
                print(colors.red, end="")
            elif l[i][1] == 'G':
                print(colors.green, end="")
            elif l[i][1] == 'Y':
                print(colors.yellow, end="")
            elif l[i][1] == 'B':
                print(colors.blue, end="")
            print("%s" %(l[i][0]) + colors.fim, end="")
        print("] ", end="")
        if (i + 1) % 7 == 0:
            print()
    if n % 7 != 0:
        print()

def ImprimeCarta2(l, n):
    for i in range(n):
        print("%d:[" %i, end="")
        if l[i][1] == 'M':
            print(colors.red + "/" + colors.blue + "/" + colors.green + "/" + colors.yellow + "/" + colors.fim, end="")
        elif l[i][1] == 'N':
            print("%s" %(l[i][0]), end="")
        else:
            if l[i][1] == 'R':
                print(colors.red, end="")
            elif l[i][1] == 'G':
                print(colors.green, end="")
            elif l[i][1] == 'Y':
                print(colors.yellow, end="")
            elif l[i][1] == 'B':
                print(colors.blue, end="")
            print("%s" %(l[i][0]) + colors.fim, end="")
        print("]  ", end="")
        if (i + 1) % 7 == 0:
            print()
    if n % 7 != 0:
        print()

def ImprimeCarta3(l, n, ca):
    filtro = []
    for i in range(n):
        if ca[0][0] == l[i][0]:
            filtro.append(i)
            print("%d:[" %i, end="")
            if l[i][1] == 'N':
                print("%s" %(l[i][0]), end="")
            else:
                if l[i][1] == 'R':
                    print(colors.red, end="")
                elif l[i][1] == 'G':
                    print(colors.green, end="")
                elif l[i][1] == 'Y':
                    print(colors.yellow, end="")
                elif l[i][1] == 'B':
                    print(colors.blue, end="")
                print("%s" %(l[i][0]) + colors.fim, end="")
            print("]  ", end="")
    print()
    return filtro

def RemoverCarta(l, ca, write):
    n = len(l)
    if write == 1:
        print("Qual carta jogar?")
        print("(digite o número ao lado da carta invés do símbolo na carta.)")
        ImprimeCarta2(l, n)
        while True:
            print("-> ", end="")
            e = int(input())
            if 0 > e or e >= n:
                print("Número inválido.")
            else:
                if l[e][0] == ca[0][0] or l[e][1] == ca[0][1] or l[e][1] == 'M' or l[e][1] == 'N':
                    ca[0] = l[e]
                    l.remove(l[e])
                    break
                else:
                    print("Essa carta não pode ser jogada agora.")
    else:
        ca[0] = l[-1]
        l.remove(l[-1])

def TelaJogo(cc, cj, ca):
    nc = len(cc)
    nj = len(cj)
    cc2 = ['#']
    print("Cartas do Computador:")
    ImprimeCarta(cc2, nc)
    print("Carta Atual:")
    print()
    print("            ", end="")
    ImprimeCarta(ca, 1)
    print()
    print("Suas Cartas:")
    ImprimeCarta(cj, nj)

def main():
    print("---------- UNO! -----------") 
    print()
    ln = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    c = ['R', 'G', 'Y', 'B']
    while True:
        print("========= OPÇÕES =========")
        print("[1] Jogar   [2] Instruções")
        print("        [3] Sair")
        e = 0
        while '1' != e != '2' and e != '3':
            print("-> ", end="")
            e = input()
        print()
        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        elif e == '2':
            print("========== INSTRUÇÕES ==========")
            print()
            print("IMPLEMENTAR")
            print()
        elif e == '1':
            cc = []
            cj = []
            ca = []
            EntregaCarta(cc, 7, 1)
            EntregaCarta(cj, 7, 1)
            v = 1
            pc = 1
            corM = 0
            debt = 0
            print("O jogador começa.")
            print()
            ca.append([])
            ca[0].append(random.choice(ln))
            ca[0].append(random.choice(c))
            while True:
                TelaJogo(cc, cj, ca)
                print()
                nj = len(cj)
                p = 0
                if ca[0][0] in ln or ca[0][0] == 'X' or pc == 0 or corM == 1:
                    for i in range(nj):
                        if ca[0][0] == cj[i][0] or ca[0][1] == cj[i][1] or cj[i][1] == 'M' or cj[i][1] == 'N':
                            p = 1
                    if p == 1:
                        print("[1] Jogar carta   [2] Comprar carta")
                        J = 0
                        while '1' != J != '2':
                            print("-> ", end="")
                            J = input()
                        print()
                        if J == '2':
                            print("COMPRANDO CARTA...")
                            time.sleep(0.7)
                            EntregaCarta(cj, 1, 0)
                            if cj[-1][0] == ca[0][0] or cj[-1][1] == ca[0][1] or cj[-1][1] == 'M' or cj[-1][1] == 'N':
                                J2 = '/'
                                while 's' != J2 != 'n':
                                    print("Jogar a Carta? (s/n)")
                                    print("-> ", end="")
                                    J2= input()
                                    print()
                                if J2 == 's':
                                    if cj[-1][0] == '+2' or cj[-1][0] == '+4':
                                        pc = 1
                                        if cj[-1][0] == '+2':
                                            debt = debt + 2
                                        if cj[-1][0] == '+4':
                                            debt = debt + 4
                                            print("Escolha a próxima cor a ser jogada:")
                                            print("[1] Vermelho  [2] Verde  [3] Amarelo  [4] Azul")
                                            J3 = 0
                                            while '1' != J3 != '2' and '3' != J3 != '4':
                                                print("-> ", end="")
                                                J3 = input()
                                            print()
                                            if J3 == '1':
                                                cj[-1][1] = 'R'
                                            elif J3 == '2':
                                                cj[-1][1] = 'G'
                                            elif J3 == '3':
                                                cj[-1][1] = 'Y'
                                            elif J3 == '4':
                                                cj[-1][1] = 'B'
                                    RemoverCarta(cj, ca, 0)
                        elif J == '1':
                            RemoverCarta(cj, ca, 1)
                            if ca[0][0] == '+2' or ca[0][0] == '+4':
                                pc = 1
                                if ca[0][0] == '+2':
                                    debt = debt + 2
                                if ca[0][0] == '+4':
                                    debt = debt + 4
                                    print("Escolha a próxima cor a ser jogada:")
                                    print("[1] Vermelho  [2] Verde  [3] Amarelo  [4] Azul")
                                    J3 = 0
                                    while '1' != J3 != '2' and '3' != J3 != '4':
                                        print("-> ", end="")
                                        J3 = input()
                                    print()
                                    if J3 == '1':
                                        ca[0][1] = 'R'
                                    elif J3 == '2':
                                        ca[0][1] = 'G'
                                    elif J3 == '3':
                                        ca[0][1] = 'Y'
                                    elif J3 == '4':
                                        ca[0][1] = 'B'
                    else:
                        time.sleep(0.7)
                        print("O jogador não possui uma carta disponível para jogar.")
                        print("COMPRANDO CARTA...")
                        time.sleep(0.7)
                        EntregaCarta(cj, 1, 0)
                        if cj[-1][0] == ca[0][0] or cj[-1][1] == ca[0][1] or cj[-1][1] == 'M' or cj[-1][1] == 'N':
                            J2 = '/'
                            while 's' != J2 != 'n':
                                print("Jogar a Carta? (s/n)")
                                print("-> ", end="")
                                J2= input()
                                print()
                            if J2 == 's':
                                if cj[-1][0] == '+2' or cj[-1][0] == '+4':
                                    pc = 1
                                    if cj[-1][0] == '+2':
                                        debt = debt + 2
                                    if cj[-1][0] == '+4':
                                        debt = debt + 4
                                        print("Escolha a próxima cor a ser jogada:")
                                        print("[1] Vermelho  [2] Verde  [3] Amarelo  [4] Azul")
                                        J3 = 0
                                        while '1' != J3 != '2' and '3' != J3 != '4':
                                            print("-> ", end="")
                                            J3 = input()
                                        print()
                                        if J3 == '1':
                                            cj[-1][1] = 'R'
                                        elif J3 == '2':
                                            cj[-1][1] = 'G'
                                        elif J3 == '3':
                                            cj[-1][1] = 'Y'
                                        elif J3 == '4':
                                            cj[-1][1] = 'B'
                                RemoverCarta(cj, ca, 0)
                elif pc == 1:
                    for i in range(nj):
                        if ca[0][0] == cj[i][0]:
                            p = 1
                    if p == 1:
                        print("[1] Jogar carta   [2] Comprar carta")
                        J = 0
                        while '1' != J != '2':
                            print("-> ", end="")
                            J = input()
                        print()
                        if J == '2':
                            print("COMPRANDO CARTA...")
                            time.sleep(0.7)
                            EntregaCarta(cj, debt, 0)
                            pc = 0
                            debt = 0
                        elif J == '1':
                            print("Qual carta jogar?")
                            print("(digite o número ao lado da carta invés do símbolo na carta.)")
                            filtro = ImprimeCarta3(cj, nj, ca)
                            while True:
                                print("-> ", end="")
                                e = int(input())
                                if e not in filtro:
                                    print("Número inválido.")
                                else:
                                    if ca[0][0] == '+2':
                                        debt = debt + 2
                                    if ca[0][0] == '+4':
                                        debt = debt + 4
                                    ca[0] = cj[e]
                                    cj.remove(cj[e])
                                    break
                    else:
                        time.sleep(0.7)
                        print("O jogador não possui uma carta para se defender.")
                        print("COMPRANDO CARTAS...")
                        time.sleep(0.7)
                        EntregaCarta(cj, debt, 0)
                        pc = 0
                        debt = 0
                elif ca[0][1] == 'M':
                    s = 2
                else:
                    break    
            break
main()
