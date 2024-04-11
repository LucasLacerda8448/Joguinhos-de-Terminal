import os
os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    fim = '\033[0m'

def ImprimeJogo(l0, l1, l2, l3, l4, l5, l6, l7, l8, li, si):
    lX = ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X']
    lO = ['O', 'O', 'O', 'O', ' ', 'O', 'O', 'O', 'O']
    p = 0
    c = 3
    if li == 0:
        print(colors.yellow + "     [0]" + colors.fim + "     [1]     [2]")
    elif li == 1:
        print("     [0]" + colors.yellow + "     [1]" + colors.fim + "     [2]")
    elif li == 2:
        print("     [0]     [1]" + colors.yellow + "     [2]" + colors.fim)
    else:
        print("     [0]     [1]     [2]")
    for i in range(11):
        if i == 3 or i == 7:
            for j in range(3):
                if c == li:
                    print(colors.yellow + "     [%d]" %c + colors.fim, end="")
                else:
                    print("     [%d]" %c, end="")
                c = c + 1
            print()
        else:
            print("    ", end="")
            for j in range(11):
                if 0 <= i <= 2:
                    if 0 <= j <= 2:
                        if li == 0:
                            print(colors.yellow + "%s " %l0[p] + colors.fim, end="")
                        else:
                            print("%s " %l0[p], end="")
                    elif 4 <= j <= 6:
                        if li == 1:
                            print(colors.yellow + "%s " %l1[p] + colors.fim, end="")
                        else:
                            print("%s " %l1[p], end="")
                    elif 8 <= j <= 10:
                        if li == 2:
                            print(colors.yellow + "%s " %l2[p] + colors.fim, end="")
                        else:
                            print("%s " %l2[p], end="")
                elif 4 <= i <= 6:
                    if 0 <= j <= 2:
                        if li == 3:
                            print(colors.yellow + "%s " %l3[p] + colors.fim, end="")
                        else:
                            print("%s " %l3[p], end="")
                    elif 4 <= j <= 6:
                        if li == 4:
                            print(colors.yellow + "%s " %l4[p] + colors.fim, end="")
                        else:
                            print("%s " %l4[p], end="")
                    elif 8 <= j <= 10:
                        if li == 5:
                            print(colors.yellow + "%s " %l5[p] + colors.fim, end="")
                        else:
                            print("%s " %l5[p], end="")
                elif 8 <= i <= 10:
                    if 0 <= j <= 2:
                        if li == 6:
                            print(colors.yellow + "%s " %l6[p] + colors.fim, end="")
                        else:
                            print("%s " %l6[p], end="")
                    elif 4 <= j <= 6:
                        if li == 7:
                            print(colors.yellow + "%s " %l7[p] + colors.fim, end="")
                        else:
                            print("%s " %l7[p], end="")
                    elif 8 <= j <= 10:
                        if li == 8:
                            print(colors.yellow + "%s " %l8[p] + colors.fim, end="")
                        else:
                            print("%s " %l8[p], end="")
                if j == 3 or j == 7:
                    print("  ", end="")
                    p = p - 4
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

def Jogar(j0, j1, j2, j3, j4, j5, j6, j7, j8, ji, v):
    if ji == 0:
        j = j0
    elif ji == 1:
        j = j1
    elif ji == 2:
        j = j2
    elif ji == 3:
        j = j3
    elif ji == 4:
        j = j4
    elif ji == 5:
        j = j5
    elif ji == 6:
        j = j6
    elif ji == 7:
        j = j7
    elif ji == 8:
        j = j8
    while True:
        print("-> ", end="")
        p1 = int(input())
        if p1 < 0 or p1 > 8:
            print("Valores inválidos, insira outro valor.")
        elif j[p1] == 'X' or j[p1] == 'O':
            print("A posição inserida ja está ocupada, insira outro valor.")
        else:
            j[p1] = v
            print()
            break
    r = Verifica(j)
    return r, p1

def main():
    print("------------- JOGO DA VELHA -------------")
    print()
    while True:
        j0 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
        mi = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        e = '/'
        while '1' != e != '2':
            print("[1] Modo normal   [2] Super-jogo da velha")
            print("             [3] Sair")
            print("-> ", end="")
            e = input()
            print()

        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        elif e == '1':
            p = 0
            for i in range(3):
                print("    ", end="")
                for j in range(3):
                    print("%s " %j0[p], end="")
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
                    p1 = int(input())
                    if p1 < 0 or p1 > 8:
                        print("Valores inválidos, insira outro valor.")
                    elif j0[p1] == 'X' or j0[p1] == 'O':
                        print("A posição inserida ja está ocupada, insira outro valor.")
                    else:
                        j0[p1] = v
                        print()
                        break

                p = 0
                for i in range(3):
                    print("    ", end="")
                    for j in range(3):
                        print("%s " %j0[p], end="")
                        p = p + 1
                    print()
                print()
                r = Verifica(j0)
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
            j1 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            j2 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            j3 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            j4 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            j5 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            j6 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            j7 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            j8 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            ji = -1
            p1 = 9
            ImprimeJogo(j0, j1, j2, j3, j4, j5, j6, j7, j8, ji, si)
            print("O jogador X começa.")
            v = 'X'
            while True:
                if si[p1] != '*':
                    print("Insira a posição do jogo que deseja jogar:")
                    while True:
                        print("-> ", end="")
                        p1 = int(input())
                        if p1 < 0 or p1 > 8:
                            print("Valores inválidos, insira outro valor.")
                        elif si[p1] == 'X' or si[p1] == 'O':
                            print("O jogo escolhido ja foi finalizado, insira outro valor.")
                        else:
                            ji = p1
                            print()
                            break
                
                ImprimeJogo(j0, j1, j2, j3, j4, j5, j6, j7, j8, ji, si)
                print("Insira a posição que deseja jogar:")
                p = 0
                for i in range (3):
                    print("    ", end="")
                    for j in range(3):
                        print("%s " %mi[p], end="")
                        p = p + 1
                    print()

                r, p1 = Jogar(j0, j1, j2, j3, j4, j5, j6, j7, j8, ji, v)
                if r == 'C':
                    if v == 'X':
                        v = 'O'
                    else:
                        v = 'X'
                    ImprimeJogo(j0, j1, j2, j3, j4, j5, j6, j7, j8, p1, si)
                    print("Vez do jogador %s." %v)
                else:
                    ImprimeJogo(j0, j1, j2, j3, j4, j5, j6, j7, j8, -1, si)
                    print("FIM DE JOGO!")
                    if r == 'X' or r == 'O':
                        print("Jogador %s Venceu." %r)
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
