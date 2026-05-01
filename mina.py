import os
import random
os.system('color')

class colors:
    white = '\033[37m'
    red = '\033[91m'
    dark_red = '\033[31m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    cyan = '\033[96m'
    purple = '\033[95m'
    dark_purple = '\033[35m'
    grey = '\033[90m'
    fim = '\033[0m'
    RED = '\033[41m'
    b_yellow = '\033[93m'
    d_green = '\033[32m'

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

def limpa():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def VerificaLado(pos_x, pos_y, m, tamy, tamx):
    qb = 0
    #dir
    if pos_y != tamy and m[pos_x][pos_y + 1] == 'X': #17 or 10
        qb += 1
    #esq
    if pos_y != 0 and m[pos_x][pos_y - 1] == 'X':
        qb += 1
    #up
    if pos_x != 0 and m[pos_x - 1][pos_y] == 'X':
        qb += 1
    #down
    if pos_x != tamx and m[pos_x + 1][pos_y] == 'X': #14 or 8
        qb += 1
    #d_esq_up
    if pos_y != 0 and pos_x != 0 and m[pos_x - 1][pos_y - 1] == 'X':
        qb += 1
    #d_dir_up
    if pos_y != tamy and pos_x != 0 and m[pos_x - 1][pos_y + 1] == 'X':
        qb += 1
    #d_esq_down
    if pos_y != 0 and pos_x != tamx and m[pos_x + 1][pos_y - 1] == 'X':
        qb += 1
    #d_dir_down
    if pos_y != tamy and pos_x != tamx and m[pos_x + 1][pos_y + 1] == 'X':
        qb += 1

    if qb == 0:
        return '   '
    else:
        return str(qb)

def TelaJogo(mj, bd, modo):
    if modo == 'L':
        print("     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R")
        print("   ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
        lin = 15
        col = 18
    elif modo == 'C':
        print("     A   B   C   D   E   F   G   H   I   J   K")
        print("   ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
        lin = 9
        col = 11

    for i in range(lin):
        if i <= 9:
            print(" %d ║" %i, end="")
        else:
            print("%d ║" %i, end="")
        for j in range(col):
            if mj[i][j] == 'B':
                print(colors.dark_red + "▐▀■" + colors.fim, end="")
            elif mj[i][j] == 'b':
                print(colors.b_yellow + "▐▀■" + colors.fim, end="")
            elif mj[i][j] == ' ■ ':
                print(colors.b_yellow + "%s" %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == 'X':
                print(colors.RED + colors.b_yellow + "░" + colors.b_yellow + "▒" + colors.b_yellow + "░" + colors.fim, end="")
            elif mj[i][j] == '1':
                print(colors.blue + " %s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '2':
                print(colors.green + " %s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '3':
                print(colors.yellow + " %s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '4':
                print(colors.purple + " %s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '5':
                print(colors.red + " %s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '6':
                print(colors.cyan + " %s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '7':
                print(colors.dark_purple + " %s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '8':
                print(colors.grey + " %s " %mj[i][j] + colors.fim, end="")
            else:
                print("%s" %mj[i][j], end="")
            
            if j == (col-1):
                print("║    ", end="")
                if i == 1:
                    print(colors.b_yellow + "   TOTAL DE BOMBAS:" + colors.fim, end="")
                elif i == 3:
                    print(colors.d_green + "         %d" %bd + colors.fim, end="")
                print()
            else:
                print("│", end="")

        if i == (lin-1):
            if modo == 'L':
                print("   ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝")
            else:
                print("   ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝")
        else:
            if modo == 'L':
                print("   ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢    ", end="")
                if i == 1:
                    print(colors.b_yellow + "         40" + colors.fim, end="")
                elif i == 2:
                    print(colors.d_green + "BANDEIRAS POSICIONADAS:" + colors.fim, end="")
            else:
                print("   ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢    ", end="")
                if i == 1:
                    print(colors.b_yellow + "         12" + colors.fim, end="")
                elif i == 2:
                    print(colors.d_green + "BANDEIRAS POSICIONADAS:" + colors.fim, end="")
            print()
    print()

def CriaJogo(modo):
    m2 = []
    if modo == 'L':
        lin = 15
        col = 18
        qnt = 40
    elif modo == 'C':
        lin = 9
        col = 11
        qnt = 12
    for i in range(lin):
        m2.append([])
        for j in range(col):
            m2[i].append('   ')

    for i in range(qnt):
        while True:
            x = random.randint(0, lin - 1)
            y = random.randint(0, col - 1)
            if m2[x][y] == '   ':
                m2[x][y] = 'X'
                break
    
    for i in range(lin):
        for j in range(col):
            if m2[i][j] == '   ':
                m2[i][j] = VerificaLado(i, j, m2, col - 1, lin - 1)
    #TelaJogo(m2, modo)
    return m2

def Posicao(mj, modo):
    while True:
        print("-> ", end="")
        p1 = input()
        if modo == 'L':
            if 2 <= len(p1) <= 3:
                if 65 <= ord(p1[0]) <= 82 and 48 <= ord(p1[1]) <= 57:
                    col = ord(p1[0]) - 65
                    if len(p1) == 3:
                        if 48 <= ord(p1[2]) <= 52:
                            lin = int(p1[1] + p1[2])
                            if lin <= 14:
                                if mj[lin][col] == '▐█▌' or mj[lin][col] == 'B':
                                    break
                                else:
                                    print("A posição inserida ja foi usada.")
                            else:
                                print("Insira uma posição dentro do intervalo.")
                        else:
                            print("Insira uma posição dentro do intervalo.")
                    else:
                        lin = int(p1[1])
                        if mj[lin][col] == '▐█▌' or mj[lin][col] == 'B':
                            break
                        else:
                            print("A posição inserida ja foi usada.")
                else:
                    print("Insira uma posição dentro do intervalo.")
            else:
                print("Insira a posição corretamente.")
        elif modo == 'C':
            if len(p1) == 2:
                if 65 <= ord(p1[0]) <= 75 and 48 <= ord(p1[1]) <= 56:
                    col = ord(p1[0]) - 65
                    lin = int(p1[1])
                    if mj[lin][col] == '▐█▌' or mj[lin][col] == 'B':

                        break
                    else:
                        print("A posição inserida ja foi usada.")
                else:
                    print("Insira uma posição dentro do intervalo.") 
            else:
                print("Insira a posição corretamente.")

    return col, lin

def Bandeira(col, lin, mj):
    if mj[col][lin] == 'b':
        mj[col][lin] = '▐█▌'
    else:
        mj[col][lin] = 'B'

def CavaPonto2(lin, col, mj, mr, dir, maxcol, maxlin):
    mj[lin][col] = mr[lin][col]
    if mr[lin][col] == '   ':
        if dir == 1 and col != maxcol:
            if lin != maxlin:
                mj[lin + 1][col + 1] = mr[lin + 1][col + 1]
            if lin != 0:
                mj[lin - 1][col + 1] = mr[lin - 1][col + 1]
            CavaPonto2(lin, col + 1, mj, mr, 1, maxcol, maxlin)

        elif dir == -2 and lin != 0:
            if col != maxcol:
                mj[lin - 1][col + 1] = mr[lin - 1][col + 1]
            if col != 0:
                mj[lin - 1][col - 1] = mr[lin - 1][col - 1]
            CavaPonto2(lin - 1, col, mj, mr, -2, maxcol, maxlin)

        elif dir == -1 and col != 0:
            if lin != 0:
                mj[lin - 1][col - 1] = mr[lin - 1][col - 1]
            if lin != maxlin:
                mj[lin + 1][col - 1] = mr[lin + 1][col - 1]
            CavaPonto2(lin, col - 1, mj, mr, -1, maxcol, maxlin)

        elif dir == 2 and lin != maxlin:
            if col != maxcol:
                mj[lin + 1][col + 1] = mr[lin + 1][col + 1]
            if col != 0:
                mj[lin + 1][col - 1] = mr[lin + 1][col - 1]
            CavaPonto2(lin + 1, col, mj, mr, 2, maxcol, maxlin)

def CavaPonto(lin, col, mj, mr, modo):
    if modo == 'L':
        maxcol = 17
        maxlin = 14
    elif modo == 'C':
        maxcol = 10
        maxlin = 8

    mj[lin][col] = mr[lin][col]
    if mr[lin][col] == '   ':
        if col != maxcol and lin != maxlin:
            mj[lin + 1][col + 1] = mr[lin + 1][col + 1]
        if col != maxcol and lin != 0:
            mj[lin - 1][col + 1] = mr[lin - 1][col + 1]
        if col != 0 and lin != 0:
            mj[lin - 1][col - 1] = mr[lin - 1][col - 1]
        if col != 0 and lin != maxlin:
            mj[lin + 1][col - 1] = mr[lin + 1][col - 1]

        if col != maxcol:
            CavaPonto2(lin, col + 1, mj, mr, 1, maxcol, maxlin)
        if lin != 0:
            CavaPonto2(lin - 1, col, mj, mr, -2, maxcol, maxlin)
        if col != 0:
            CavaPonto2(lin, col - 1, mj, mr, -1, maxcol, maxlin)
        if lin != maxlin:
            CavaPonto2(lin + 1, col, mj, mr, 2, maxcol, maxlin)
    
def FimDeJogo(mj, mr, modo):
    if modo == 'L':
        for i in range(15):
            for j in range(18):
                if mr[i][j] == 'X':
                    mj[i][j] = 'X'
    else:
        for i in range(9):
            for j in range(11):
                if mr[i][j] == 'X':
                    mj[i][j] = 'X'

def Verifica(col, lin, mj, mr, modo):
    if mr[lin][col] == 'X':
        FimDeJogo(mj, mr, modo)
        return 0
    else:
        CavaPonto(lin, col, mj, mr, modo)
        return 1

def main():
    limpa()
    print("───────── CAMPO MINADO ─────────")
    print()
    while True:
        print("[1] Modo Curto   [2] Modo Longo")
        print("           [3] Sair")
        e = Escolha(3)
        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        elif e == '1':
            mj = []
            bd = 0
            limpa()
            print("     A   B   C   D   E   F   G   H   I   J   K")
            print("   ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
            for i in range(9):
                print(" %d ║" %i, end="")
                mj.append([])
                for j in range(11):
                    mj[i].append('▐█▌')
                    print("%s" %mj[i][j], end="")

                    if j == 10:
                        print("║    ", end="")
                        if i == 1:
                            print(colors.b_yellow + "   TOTAL DE BOMBAS:" + colors.fim, end="")
                        elif i == 3:
                            print(colors.d_green + "         %d" %bd + colors.fim, end="")
                        print()
                    else:
                        print("│", end="")
                if i == 8:
                    print("   ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝")
                else:
                    print("   ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢    ", end="")
                    if i == 1:
                        print(colors.b_yellow + "         12" + colors.fim, end="")
                    elif i == 2:
                        print(colors.d_green + "BANDEIRAS POSICIONADAS:" + colors.fim, end="")
                    print()
            print()
            mr = []
            mr = CriaJogo('C')
            while True:
                print("Insira a posição que deseja jogar: (letra primeiro, depois o número)")
                col, lin = Posicao(mj, 'C')
                r = 1
                limpa()
                if mj[lin][col] == '▐█▌':
                    mj[lin][col] = ' ■ '
                    TelaJogo(mj, bd, 'C')
                    print("[1] Cavar o lugar     [2] Colocar uma bandeira     [3] Voltar")
                    e = Escolha(3)
                    if e == '2':
                        bd += 1
                        Bandeira(lin, col, mj)
                    elif e == '1':
                        r = Verifica(col, lin, mj, mr, 'C')
                    else:
                        mj[lin][col] = '▐█▌'
                else:
                    mj[lin][col] = 'b'
                    TelaJogo(mj, bd, 'C')
                    print("[1] Tirar a bandeira   [2] Voltar")
                    if Escolha(2) == '1':
                        bd -= 1
                        Bandeira(lin, col, mj)
                    else:
                        mj[lin][col] = 'B'
                limpa()
                TelaJogo(mj, bd, 'C')
                if r == 0:
                    print(colors.red + "BOMBAS ATIVADAS!!" + colors.fim)
                    print("VOCE PERDEU")
                    break
                f = 0
                for i in range(9):
                    for j in range(11):
                        if mj[i][j] == '▐█▌':
                            f = 1
                            break
                    if f:
                        break
                if not f:
                    print(colors.d_green + "BOMBAS DESATIVADAS!!" + colors.fim)
                    print("VOCE GANHOU")
                    break

        elif e == '2':
            mj = []
            bd = 0
            limpa()
            print("     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R")
            print("   ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
            for i in range(15):
                if i <= 9:
                    print(" %d ║" %i, end="")
                else:
                    print("%d ║" %i, end="")
                mj.append([])
                for j in range(18):
                    mj[i].append('▐█▌')
                    print("%s" %mj[i][j], end="")  

                    if j == 17:
                        print("║    ", end="")
                        if i == 1:
                            print(colors.b_yellow + "   TOTAL DE BOMBAS:" + colors.fim, end="")
                        elif i == 3:
                            print(colors.d_green + "         %d" %bd + colors.fim, end="")
                        print()
                    else:
                        print("│", end="")
                if i == 14:
                    print("   ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝")
                else:
                    print("   ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢    ", end="")
                    if i == 1:
                        print(colors.b_yellow + "         40" + colors.fim, end="")
                    elif i == 2:
                        print(colors.d_green + "BANDEIRAS POSICIONADAS:" + colors.fim, end="")
                    print()
            print()
            mr = []
            mr = CriaJogo('L')
            while True:
                print("Insira a posição que deseja jogar: (letra primeiro, depois o número)")
                col, lin = Posicao(mj, 'L')
                r = 1
                limpa()
                if mj[lin][col] == '▐█▌':
                    mj[lin][col] = ' ■ '
                    TelaJogo(mj, bd, 'L')
                    print("[1] Cavar o lugar     [2] Colocar uma bandeira     [3] Voltar")
                    e = Escolha(3)
                    if e == '2':
                        bd += 1
                        Bandeira(lin, col, mj)
                    elif e == '1':
                        r = Verifica(col, lin, mj, mr, 'L')
                    else:
                        mj[lin][col] = '▐█▌'
                else:
                    mj[lin][col] = 'b'
                    TelaJogo(mj, bd, 'L')
                    print("[1] Tirar a bandeira   [2] Voltar")
                    if Escolha(2) == '1':
                        bd -= 1
                        Bandeira(lin, col, mj)
                    else:
                        mj[lin][col] = 'B'
                limpa()
                TelaJogo(mj, bd, 'L')
                if r == 0:
                    print(colors.red + "BOMBAS ATIVADAS!!" + colors.fim)
                    print("VOCE PERDEU")
                    break
                f = 0
                for i in range(15):
                    for j in range(18):
                        if mj[i][j] == '▐█▌':
                            f = 1
                            break
                    if f:
                        break
                if not f:
                    print(colors.d_green + "BOMBAS DESATIVADAS!!" + colors.fim)
                    print("VOCE GANHOU")
                    break 

        print() 
        print("[1] Jogar Novamente   [2] Sair")
        if Escolha(2) == '2':
            print("ENCERRANDO JOGO...")
            break
        else:
            limpa()
            print("INICIANDO NOVO JOGO...")
            print()

main()
