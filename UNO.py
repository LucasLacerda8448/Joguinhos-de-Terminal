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

def ImprimeCarta2(l, n, ca, pc):
    filtro = []
    for i in range(n):
        if pc == 1:
            if ca[0][0] == l[i][0]:
                filtro.append(i)
                print("%d:[" %i, end="")
                if l[i][1] == 'N':
                    print("%s" %(l[i][0]), end="")
                elif l[i][0] == '+2':
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
                n = len(filtro)
                if (n) % 7 == 0:
                    print()
        else:
            if ca[0][0] == l[i][0] or ca[0][1] == l[i][1] or l[i][1] == 'M' or l[i][1] == 'N':
                filtro.append(i)
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
                n = len(filtro)
                if (n) % 7 == 0:
                    print()
    n = len(filtro)
    if n % 7 != 0:
        print()
    return filtro

def RemoverCarta(l, ca, ce, write, pc):
    n = len(l)
    if write == 1:
        print("Qual carta jogar?")
        if pc == 1:
            filtro = ImprimeCarta2(l, n, ca, 1)
        else:
            filtro = ImprimeCarta2(l, n, ca, 0)
        while True:
            print("-> ", end="")
            e = int(input())
            if e not in filtro:
                print("Número inválido.")
            else:
                print()
                ca[0] = l[e]
                l.remove(l[e])
                break
    else:
        ca[0] = ce
        l.remove(ce)

def AnalisaCarta(ca, pc, debt, v, comp):
    if ca[0][0] != 'X':
        if ca[0][1] == 'M' or ca[0][1] == 'N':
            if ca[0][1] == 'N':
                pc = 1
                debt = debt + 4
            if comp == 1:
                e = str(random.randint(1, 4))
            else:
                print("Escolha a próxima cor a ser jogada:")
                print("[1] Vermelho  [2] Verde  [3] Amarelo  [4] Azul")
                e = Escolha(4)
            if e == '1':
                ca[0][1] = 'R'
            elif e == '2':
                ca[0][1] = 'G'
            elif e == '3':
                ca[0][1] = 'Y'
            elif e == '4':
                ca[0][1] = 'B'
        elif ca[0][0] == '+2':
            pc = 1
            debt = debt + 2
        if v == 1:
            v = 0
        else:
            v = 1
    return v, pc, debt

def TelaJogo(cc, cj, ca, pc, debt):
    nc = len(cc)
    nj = len(cj)
    cc2 = ['#']
    print("Cartas do Computador: (%d)" %nc)
    #ImprimeCarta(cc2, nc)
    ImprimeCarta(cc, nc)
    print("Carta Atual:")
    print()
    print("            ", end="")
    if pc == 1:
        print("[", end="")
        if ca[0][1] == 'R':
            print(colors.red, end="")
        elif ca[0][1] == 'G':
            print(colors.green, end="")
        elif ca[0][1] == 'Y':
            print(colors.yellow, end="")
        elif ca[0][1] == 'B':
            print(colors.blue, end="")
        print("%s" %(ca[0][0]) + colors.fim, end="")
        print("]  (+%d)" %debt)
    else:
        ImprimeCarta(ca, 1)
    print()
    print("Suas Cartas: (%d)" %nj)
    ImprimeCarta(cj, nj)

def VezJogador(cc, cj, ca, v, debt, pc):
    while v == 1:
        TelaJogo(cc, cj, ca, pc, debt)
        print()
        nj = len(cj)
        if nj == 1:
            UNO = 1
        else:
            UNO = 0
        p = 0
        if pc == 0 and UNO == 0:
            for i in range(nj):
                if ca[0][0] == cj[i][0] or ca[0][1] == cj[i][1] or cj[i][1] == 'M' or cj[i][1] == 'N':
                    p = 1
            if p == 1:
                print("[1] Jogar carta   [2] Comprar carta")
                if Escolha(2) == '2':
                    print("COMPRANDO CARTA...")
                    time.sleep(1)
                    EntregaCarta(cj, 1, 0)
                    if cj[-1][0] == ca[0][0] or cj[-1][1] == ca[0][1] or cj[-1][1] == 'M' or cj[-1][1] == 'N':
                        print("[1] Jogar carta   [2] Guardar carta")
                        if Escolha(2) == '1':
                            RemoverCarta(cj, ca, cj[-1], 0, pc)
                            v, pc, debt = AnalisaCarta(ca, pc, debt, v, 0)
                        else:
                            v = 0
                    else:
                        v = 0
                else:
                    RemoverCarta(cj, ca, 0, 1, pc)
                    v, pc, debt = AnalisaCarta(ca, pc, debt, v, 0)
            else:
                time.sleep(1)
                print("O jogador não possui uma carta disponível para jogar.")
                print("COMPRANDO CARTA...")
                time.sleep(1)
                EntregaCarta(cj, 1, 0)
                if cj[-1][0] == ca[0][0] or cj[-1][1] == ca[0][1] or cj[-1][1] == 'M' or cj[-1][1] == 'N':
                    print("[1] Jogar carta   [2] Guardar carta")
                    if Escolha(2) == '1':
                        RemoverCarta(cj, ca, cj[-1], 0, pc)
                        v, pc, debt = AnalisaCarta(ca, pc, debt, v, 0)
                    else:
                        v = 0
                else:
                    v = 0
        elif pc == 1:
            for i in range(nj):
                if ca[0][0] == cj[i][0]:
                    p = 1
            if p == 1:
                print("[1] Jogar carta   [2] Comprar carta")
                if Escolha(2) == '2':
                    print("COMPRANDO CARTA...")
                    time.sleep(1)
                    EntregaCarta(cj, debt, 0)
                    pc = 0
                    debt = 0
                    v = 0
                else:
                    RemoverCarta(cj, ca, 0, 1, pc)
                    v, pc, debt = AnalisaCarta(ca, pc, debt, v, 0)
                    if UNO == 1:
                        if ca[0][0] == '+4':
                            print("Você não pode finalizar com uma carta coringa!")
                            print("COMPRANDO CARTA SUBSTITUTA...")
                            time.sleep(1)
                            EntregaCarta(cj, 1, 0)
                        else:
                            v = 2
            else:
                time.sleep(1)
                print("O jogador não possui uma carta para se defender.")
                print("COMPRANDO CARTAS...")
                time.sleep(1)
                EntregaCarta(cj, debt, 0)
                pc = 0
                debt = 0
                v = 0
        elif UNO == 1:
            if ca[0][0] == cj[0][0] or ca[0][1] == cj[0][1] or cj[0][1] == 'M' or cj[0][1] == 'N':
                p = 1
            if p == 1:
                print("[1] Jogar carta   [2] Comprar carta")
                if Escolha(2) == '2':
                    print("COMPRANDO CARTA...")
                    time.sleep(1)
                    EntregaCarta(cj, 1, 0)
                    if cj[-1][0] == ca[0][0] or cj[-1][1] == ca[0][1] or cj[-1][1] == 'M' or cj[-1][1] == 'N':
                        print("[1] Jogar carta   [2] Guardar carta")
                        if Escolha(2) == '1':
                            RemoverCarta(cj, ca, cj[-1], 0, pc)
                            v, pc, debt = AnalisaCarta(ca, pc, debt, v, 0)
                        else:
                            UNO = 0
                            v = 0
                    else:
                        UNO = 0
                        v = 0
                else:
                    RemoverCarta(cj, ca, 0, 1, pc)
                    v, pc, debt = AnalisaCarta(ca, pc, debt, v, 0)
                    if ca[0][0] == '+4' or ca[0][0] == '////':
                        print("Você não pode finalizar com uma carta coringa!")
                        print("COMPRANDO CARTA SUBSTITUTA...")
                        time.sleep(1)
                        EntregaCarta(cj, 1, 0)
                    else:
                        v = 2
            else:
                time.sleep(1)
                print("O jogador não possui uma carta disponível para jogar.")
                print("COMPRANDO CARTA...")
                time.sleep(1)
                EntregaCarta(cj, 1, 0)
                if cj[-1][0] == ca[0][0] or cj[-1][1] == ca[0][1] or cj[-1][1] == 'M' or cj[-1][1] == 'N':
                    print("[1] Jogar carta   [2] Guardar carta")
                    if Escolha(2) == '1':
                        RemoverCarta(cj, ca, cj[-1], 0, pc)
                        v, pc, debt = AnalisaCarta(ca, pc, debt, v, 0)
                    else:
                        UNO = 0
                        v = 0
                else:
                    UNO = 0
                    v = 0

        if v == 1:
            print("VEZ DO JOGADOR NOVAMENTE.")
            print()
            time.sleep(1)
        elif v == 0:
            print("VEZ DO COMPUTADOR.")
            print()
            time.sleep(1)
    return v, debt, pc

def VezComputador(cc, cj, ca, v, debt, pc):
    while v == 0:
        TelaJogo(cc, cj, ca, pc, debt)
        print()
        nc = len(cc)
        if nc == 1:
            UNO = 1
        else:
            UNO = 0
        p = 0
        filtro2 = []
        if pc == 0 and UNO == 0:
            for i in range(nc):
                if ca[0][0] == cc[i][0] or ca[0][1] == cc[i][1] or cc[i][1] == 'M' or cc[i][1] == 'N':
                    filtro2.append(i)
                    p = 1
            time.sleep(1)
            if p == 1:
                r = random.choice(filtro2)
                RemoverCarta(cc, ca, cc[r], 0, pc)
                v, pc, debt = AnalisaCarta(ca, pc, debt, v, 1)
                print("Carta jogada: ", end="")
                ImprimeCarta(ca, 1)
                print()
                time.sleep(1)
            else:
                print("O computador não possui uma carta disponível para jogar.")
                print("COMPRANDO CARTA...")
                time.sleep(1)
                EntregaCarta(cc, 1, 0)
                #EntregaCarta(cc, 1, 1)
                #print("1 carta comprada")
                #print()
                if cc[-1][0] == ca[0][0] or cc[-1][1] == ca[0][1] or cc[-1][1] == 'M' or cc[-1][1] == 'N':
                    RemoverCarta(cc, ca, cc[-1], 0, pc)
                    v, pc, debt = AnalisaCarta(ca, pc, debt, v, 1)
                    print("Carta jogada: ", end="")
                    ImprimeCarta(ca, 1)
                    print()
                    time.sleep(1)
                else:
                    v = 1
        elif pc == 1:
            for i in range(nc):
                if ca[0][0] == cc[i][0]:
                    filtro2.append(i)
                    p = 1
            time.sleep(1)
            if p == 1:
                r = random.choice(filtro2)
                RemoverCarta(cc, ca, cc[r], 0, pc)
                v, pc, debt = AnalisaCarta(ca, pc, debt, v, 1)
                print("Carta jogada: ", end="")
                ImprimeCarta(ca, 1)
                print()
                time.sleep(1)
                if UNO == 1:
                    if ca[0][0] == '+4':
                        print("Finalização com carta coringa proibida!")
                        print("COMPRANDO CARTA SUBSTITUTA...")
                        time.sleep(1)
                        EntregaCarta(cc, 1, 0)
                        #EntregaCarta(cc, 1, 1)
                        #print("1 carta comprada")
                        #print()
                    else:
                        v = 3
            else:
                print("O computador não possui uma carta para se defender.")
                print("COMPRANDO CARTAS...")
                time.sleep(1)
                EntregaCarta(cc, debt, 0)
                #EntregaCarta(cc, debt, 1)
                #print("%d cartas compradas" %debt)
                #print()
                pc = 0
                debt = 0
                v = 1
        elif UNO == 1:
            if ca[0][0] == cc[0][0] or ca[0][1] == cc[0][1] or cc[0][1] == 'M' or cc[0][1] == 'N':
                p = 1
            time.sleep(1)
            if p == 1:
                RemoverCarta(cc, ca, cc[0], 0, pc)
                v, pc, debt = AnalisaCarta(ca, pc, debt, v, 1)
                print("Carta jogada: ", end="")
                ImprimeCarta(ca, 1)
                print()
                time.sleep(1)
                if ca[0][0] == '+4' or ca[0][0] == '////':
                    print("Finalização com carta coringa proibida!")
                    print("COMPRANDO CARTA SUBSTITUTA...")
                    time.sleep(1)
                    EntregaCarta(cc, 1, 0)
                    #EntregaCarta(cc, 1, 1)
                    #print("1 carta comprada")
                    #print()
                else:
                    v = 3
            else:
                print("O computador não possui uma carta disponível para jogar.")
                print("COMPRANDO CARTA...")
                time.sleep(1)
                EntregaCarta(cc, 1, 0)
                #EntregaCarta(cc, 1, 1)
                #print("1 carta comprada")
                #print()
                if cc[-1][0] == ca[0][0] or cc[-1][1] == ca[0][1] or cc[-1][1] == 'M' or cc[-1][1] == 'N':
                    RemoverCarta(cc, ca, cc[-1], 0, pc)
                    v, pc, debt = AnalisaCarta(ca, pc, debt, v, 1)
                    print("Carta jogada: ", end="")
                    ImprimeCarta(ca, 1)
                    print()
                    time.sleep(1)
                else:
                    UNO = 0
                    v = 1

        if v == 0:
            print("VEZ DO COMPUTADOR NOVAMENTE.")
            print()
            time.sleep(1)
        elif v == 1:
            print("VEZ DO JOGADOR.")
            print()
            time.sleep(1)
    return v, debt, pc

def main():
    print("---------- UNO! -----------") 
    print()
    ln = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    c = ['R', 'G', 'Y', 'B']
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
            print("(digite o número ao lado da carta invés do símbolo na carta.)")
            print()
        elif e == '1':
            cc = []
            cj = []
            ca = []
            EntregaCarta(cc, 7, 1)
            EntregaCarta(cj, 7, 1)
            v = 1
            pc = 0
            debt = 0
            print("O JOGADOR COMEÇA.")
            print()
            ca.append([])
            ca[0].append(random.choice(ln))
            ca[0].append(random.choice(c))
            while 2 != v != 3:
                if v == 1:
                    v, debt, pc = VezJogador(cc, cj, ca, v, debt, pc)
                elif v == 0:
                    v, debt, pc = VezComputador(cc, cj, ca, v, debt, pc)
            print("FIM DE JOGO!")
            if v == 2:
                print("O Jogador Venceu.")
            elif v == 3:
                print("O Computador Venceu.")
            print()
            
            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()
            
main()
