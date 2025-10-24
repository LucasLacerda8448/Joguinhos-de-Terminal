import os
os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    grey = '\033[90m'
    fim = '\033[0m'

def ImprimeJogo(l, li, si):
    lX = ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X']
    lO = ['O', 'O', 'O', 'O', ' ', 'O', 'O', 'O', 'O']
    p = 0
    c = 0
    le = 0
    for i in range(12):
        if i == 0 or i == 4 or i == 8:
            for j in range(3):
                if c == li:
                    print(colors.yellow + "     [%d]" %c + colors.fim, end="")
                elif si[c] == 'X':
                    print(colors.red + "     [%d]" %c + colors.fim, end="")
                elif si[c] == 'O':
                    print(colors.green + "     [%d]" %c + colors.fim, end="")
                elif si[c] == 'E':
                    print(colors.grey + "     [%d]" %c + colors.fim, end="")
                else:
                    print("     [%d]" %c, end="")
                c = c + 1
            print()
        else:
            print("    ", end="")
            for j in range(11):
                if 1 <= i <= 3:
                    if 0 <= j <= 2:
                        le = 0
                    elif 4 <= j <= 6:
                        le = 1
                    elif 8 <= j <= 10:
                        le = 2
                elif 5 <= i <= 7:
                    if 0 <= j <= 2:
                        le = 3
                    elif 4 <= j <= 6:
                        le = 4
                    elif 8 <= j <= 10:
                        le = 5
                elif 9 <= i <= 11:
                    if 0 <= j <= 2:
                        le = 6
                    elif 4 <= j <= 6:
                        le = 7
                    elif 8 <= j <= 10:
                        le = 8
                if j == 3 or j == 7:
                    print("  ", end="")
                    p = p - 4
                elif si[le] == '*':
                    if li == le:
                        print(colors.yellow + "%s " %l[le][p] + colors.fim, end="")
                    else:
                        print("%s " %l[le][p], end="")
                else:
                    if si[le] == 'X':
                        print(colors.red + "%s " %lX[p] + colors.fim, end="")
                    elif si[le] == 'O':
                        print(colors.green + "%s " %lO[p] + colors.fim, end="")
                    elif si[le] == 'E':
                        print(colors.grey + "%s " %l[le][p] + colors.fim, end="")
                p = p + 1
            if p == 9:
                p = 0
            print()

def Verifica(j):
    c = 0
    v = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    m = j
    for i in range(8):
        p1 = m[v[i][0]]
        p2 = m[v[i][1]]
        p3 = m[v[i][2]]

        if p1 == '*' or p2 == '*' or p3 == '*':
            c = 1
            continue
        elif p1 == p2 == p3:
            return p1

    if c == 1:
        return 'C'
    else:
        return 'E'
    
def Verifica2(j, pA, pO, P, M, G):
    c = 0
    v = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    m = j
    for i in range(8):
        p1 = m[v[i][0]]
        p2 = m[v[i][1]]
        p3 = m[v[i][2]]

        if p1 == '*' or p2 == '*' or p3 == '*':
            c = 1
            continue
        elif p1 in pA and p2 in pA and p3 in pA:
            return 'A'
        elif p1 in pO and p2 in pO and p3 in pO:
            return 'O'

    if c == 1:
        if P == M == G == 0:
            return 'E'
        return 'C'
    else:
        if G != 0:
            return 'C'
        elif M == 0:
            return 'E'
        else:
            if '°' in j or 'ª' in j:
                return 'C'
            else:
                return 'E'

def Jogar(j, ji, si, v):
    while True:
        print("-> ", end="")
        p1 = input()
        p2 = 0
        for i in p1:
            if 48 <= ord(i) <= 57:
                p2 = 1
            else:
                p2 = 0
                break
        if p2 == 1:
            p1 = int(p1)
            if p1 < 0 or p1 > 8:
                print("Valores inválidos, insira outro valor.")
            elif j[ji][p1] == 'X' or j[ji][p1] == 'O':
                print("A posição inserida ja está ocupada, insira outro valor.")
            else:
                j[ji][p1] = v
                print()
                break
    r = Verifica(j[ji])
    if r != 'C':
        si[ji] = r
    r = Verifica(si)
    return r, p1

def main():
    print("------------- JOGO DA VELHA -------------")
    print()
    while True:
        mi = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        e = '/'
        while '1' != e != '2' and e != '3':
            print("[1] Modo normal        [2] Super-jogo da velha")
            print("[3] Modo Alternativo   [4] Sair")
            print("-> ", end="")
            e = input()
            print()

        if e == '4':
            print("ENCERRANDO JOGO...")
            break
        elif e == '1':
            jv = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            p = 0
            for i in range(3):
                print("    ", end="")
                for j in range(3):
                    print("%s " %jv[p], end="")
                    p = p + 1
                print()
            print()
            print("O jogador X começa.")
            v = 'X'
            while True:
                print("Insira a posição que deseja jogar:")
                p = 0
                for i in range (3):
                    print("    ", end="")
                    for j in range(3):
                        print("%s " %mi[p], end="")
                        p = p + 1
                    print()
                while True:
                    print("-> ", end="")
                    p1 = input()
                    p2 = 0
                    for i in p1:
                        if 48 <= ord(i) <= 57:
                            p2 = 1
                        else:
                            p2 = 0
                            break
                    if p2 == 1:
                        p1 = int(p1)
                        if p1 < 0 or p1 > 8:
                            print("Valores inválidos, insira outro valor.")
                        elif jv[p1] == 'X' or jv[p1] == 'O':
                            print("A posição inserida ja está ocupada, insira outro valor.")
                        else:
                            jv[p1] = v
                            print()
                            break

                p = 0
                for i in range(3):
                    print("    ", end="")
                    for j in range(3):
                        print("%s " %jv[p], end="")
                        p = p + 1
                    print()
                print()
                r = Verifica(jv)
                if r == 'C':
                    if v == 'X':
                        v = 'O'
                    else:
                        v = 'X'
                    print("Vez do jogador %s." %v)
                else:
                    print("FIM DE JOGO!")
                    if r == 'X' or r == 'O':
                        print("Jogador %s Venceu." %r)
                    elif r == 'E':
                        print("Empate.")
                    print()
                    break
        elif e == '2':
            si = ['*', '*', '*', '*', '*', '*', '*', '*', '*', ' ']
            sjv = []
            for i in range(9):
                sjv.append([])
                for j in range(9):
                    sjv[i].append('*')
            ji = 9
            ImprimeJogo(sjv, ji, si)
            print("O jogador X começa.")
            v = 'X'
            while True:
                if si[ji] != '*':
                    print("Insira a posição do jogo que deseja jogar:")
                    while True:
                        print("-> ", end="")
                        ji = input()
                        ij = 0
                        for i in ji:
                            if 48 <= ord(i) <= 57:
                                ij = 1
                            else:
                                ij = 0
                                break
                        if ij == 1:
                            ji = int(ji)
                            if ji < 0 or ji > 8:
                                print("Valores inválidos, insira outro valor.")
                            elif si[ji] == 'X' or si[ji] == 'O':
                                print("O jogo escolhido ja foi finalizado, insira outro valor.")
                            else:
                                print()
                                ImprimeJogo(sjv, ji, si)
                                break
                
                print("Insira a posição que deseja jogar:")
                p = 0
                for i in range (3):
                    print("    ", end="")
                    for j in range(3):
                        print("%s " %mi[p], end="")
                        p = p + 1
                    print()

                r, ji = Jogar(sjv, ji, si, v)
                if r == 'C':
                    if v == 'X':
                        v = 'O'
                    else:
                        v = 'X'
                    ImprimeJogo(sjv, ji, si)
                    print("Vez do jogador %s." %v)
                else:
                    ImprimeJogo(sjv, -1, si)
                    print("FIM DE JOGO!")
                    if r == 'X' or r == 'O':
                        print("Jogador %s Venceu." %r)
                    elif r == 'E':
                        print("Empate.")
                    print()
                    break
        elif e == '3':
            jva = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            jA = ['ª', 'a', 'A']
            jO = ['°', 'o', 'O']
            for i in range(3):
                print("    " + colors.grey, end="")
                for j in range(3):
                    print("* ", end="")
                print(colors.fim)
            print()
            print("O jogador " + colors.red + "A" + colors.fim + " começa.")
            v = 'X'
            pA = mA = gA = pO = mO = gO = 3
            while True:
                print("Insira a posição que deseja jogar:")
                p = 0
                for i in range (3):
                    print("    ", end="")
                    for j in range(3):
                        print("%d " %p, end="")
                        p = p + 1
                    print()
                while True:
                    print("-> ", end="")
                    p1 = input()
                    if len(p1) == 1 and 48 <= ord(p1) <= 56:
                        p1 = int(p1)
                        if jva[p1] == 'A' or jva[p1] == 'O':
                            print("A posição inserida ja está cheia, insira outro valor.")
                        elif jva[p1] == 'a' or jva[p1] == 'o':
                            if v == 'X':
                                G = gA
                            else:
                                G = gO
                            if G == 0:
                                print("Você não possui mais símbolos grandes, selecione outra posição.")
                            else:
                                print()
                                break
                        else:
                            print()
                            break
                    else:
                        print("Valor de entrada incorreto, insira outro valor.")

                p = 0
                for i in range(3):
                    print("    ", end="")
                    for j in range(3):
                        if p == p1:
                            print(colors.yellow, end="")
                        else:
                            if jva[p] in jA:
                                print(colors.red, end="")
                            elif jva[p] in jO:
                                print(colors.green, end="")
                            else:
                                print(colors.grey, end="")
                        print("%s " %jva[p], end="")    
                        p = p + 1
                    print(colors.fim)
                print()
                print("Escolha o tamanho do símbolo:")
                if v == 'X':
                    print("[1] %dx Pequeno   [2] %dx Médio   [3] %dx Grande" %(pA,mA,gA))
                    P = pA
                    M = mA
                    G = gA
                else:
                    print("[1] %dx Pequeno   [2] %dx Médio   [3] %dx Grande" %(pO,mO,gO))
                    P = pO
                    M = mO
                    G = gO
                while True:
                    print("-> ", end="")
                    p2 = input()
                    if len(p2) == 1 and 49 <= ord(p2) <= 51:
                        if p2 == '1':
                            if P == 0:
                                print("Você não possui mais símbolos pequenos, escolha outro tamanho.")
                            elif jva[p1] != '*':
                                print("A posição selecionada possui um símbolo maior que o escolhido, escolha um tamanho maior.")
                            else:
                                P -= 1
                                p2 = 0
                                break
                        elif p2 == '2':
                            if M == 0:
                                print("Você não possui mais símbolos médios, escolha outro tamanho.")
                            elif jva[p1] == 'a' or jva[p1] == 'o':
                                print("A posição selecionada possui um símbolo maior que o escolhido, escolha um tamanho maior.")
                            else:
                                M -= 1
                                p2 = 1
                                break
                        else:
                            if G == 0:
                                print("Você não possui mais símbolos grandes, escolha outro tamanho.")
                            else:
                                G -= 1
                                p2 = 2
                                break
                    else:
                        print("Valor de entrada incorreto, insira outro valor.")

                if v == 'X':
                    jva[p1] = jA[p2]
                    pA = P
                    mA = M
                    gA = G
                    P = pO
                    M = mO
                    G = gO
                else:
                    jva[p1] = jO[p2]
                    pO = P
                    mO = M
                    gO = G
                    P = pA
                    M = mA
                    G = gA

                print()
                p = 0
                for i in range(3):
                    print("    ", end="")
                    for j in range(3):
                        if jva[p] in jA:
                            print(colors.red, end="")
                        elif jva[p] in jO:
                            print(colors.green, end="")
                        else:
                            print(colors.grey, end="")
                        print("%s " %jva[p], end="")    
                        p = p + 1
                    print(colors.fim)
                print()
                r = Verifica2(jva, jA, jO, P, M, G)
                if r == 'C':
                    if v == 'X':
                        v = 'O'
                        print("Vez do jogador " + colors.green + "O" + colors.fim + ".")
                    else:
                        v = 'X'
                        print("Vez do jogador " + colors.red + "A" + colors.fim + ".")
                else:
                    print("FIM DE JOGO!")
                    if r == 'A' or r == 'O':
                        print("Jogador ", end="")
                        if r == 'A':
                            print(colors.red + "A" + colors.fim, end="")
                        else:
                            print(colors.green + "O" + colors.fim, end="")
                        print(" Venceu.")
                    elif r == 'E':
                        print("Empate.")
                    print()
                    break

        e2 = '/'
        while '1' != e2 != '2':
            print("[1] Jogar Novamente   [2] Sair")
            print("-> ", end="")
            e2= input()
            print()

        if e2 == '2':
            print("ENCERRANDO JOGO...")
            break
        elif e2 == '1':
            print("INICIANDO NOVO JOGO...")
            print()

main()

