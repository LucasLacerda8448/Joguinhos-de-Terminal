import random

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

def VerificaLado(pos_x, pos_y, m, tamy, tamx):
    qb = 0
    #dir
    if pos_y != tamy: #17 or 10
        if m[pos_x][pos_y + 1] == 'X':
            qb += 1
    #esq
    if pos_y != 0:
        if m[pos_x][pos_y - 1] == 'X':
            qb += 1
    #up
    if pos_x != 0:
        if m[pos_x - 1][pos_y] == 'X':
            qb += 1
    #down
    if pos_x != tamx: #14 or 8
        if m[pos_x + 1][pos_y] == 'X':
            qb += 1
    #d_esq_up
    if pos_y != 0 and pos_x != 0:
        if m[pos_x - 1][pos_y - 1] == 'X':
            qb += 1
    #d_dir_up
    if pos_y != tamy and pos_x != 0:
        if m[pos_x - 1][pos_y + 1] == 'X':
            qb += 1
    #d_esq_down
    if pos_y != 0 and pos_x != tamx:
        if m[pos_x + 1][pos_y - 1] == 'X':
            qb += 1
    #d_dir_down
    if pos_y != tamy and pos_x != tamx:
        if m[pos_x + 1][pos_y + 1] == 'X':
            qb += 1

    if qb == 0:
        return '.'
    else:
        return str(qb)

def TelaJogo(mj, modo):
    if modo == 'L':
        print("   A B C D E F G H I J K L M N O P Q R")
        lin = 15
        col = 18
    elif modo == 'C':
        print("  A B C D E F G H I J K")
        lin = 9
        col = 11
    for i in range(lin):
        if i <= 9 and lin == 15:
            print("%d  " %i, end="")
        else:
            print("%d " %i, end="")
        for j in range(col):
            if mj[i][j] == 'B':
                print(colors.dark_red + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '.':
                print(colors.grey + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == 'X':
                print(colors.dark_purple + "%s" %mj[i][j] + colors.fim + " ", end="")
            elif mj[i][j] == '1':
                print(colors.blue + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '2':
                print(colors.green + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '3':
                print(colors.yellow + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '4':
                print(colors.purple + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '5':
                print(colors.red + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '6':
                print(colors.cyan + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '7':
                print(colors.white + "%s " %mj[i][j] + colors.fim, end="")
            elif mj[i][j] == '8':
                print(colors.grey + "%s " %mj[i][j] + colors.fim, end="")
            else:
                print("%s " %mj[i][j], end="")  
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
            m2[i].append('.')

    for i in range(qnt):
        while True:
            x = random.randint(0, lin - 1)
            y = random.randint(0, col - 1)
            if m2[x][y] == '.':
                m2[x][y] = 'X'
                break
    
    for i in range(lin):
        for j in range(col):
            if m2[i][j] == '.':
                m2[i][j] = VerificaLado(i, j, m2, col - 1, lin - 1)
    #TelaJogo(m2, modo)
    return m2

def Posicao(mj, modo):
    while True:
        print("-> ", end="")
        p1 = input()
        p = []
        for i in range(len(p1)):
            p.append(p1[i])
        if modo == 'L':
            if 2 <= len(p) <= 3:
                if 65 <= ord(p[0]) <= 82 and 48 <= ord(p[1]) <= 57:
                    col = p[0]
                    p.remove(col)
                    col = ord(col)
                    col -= 65
                    if len(p) == 2:
                        if 48 <= ord(p[1]) <= 52:
                            p1 = p[0] + p[1]
                            p1 = int(p1)
                            if p1 <= 14:
                                if mj[p1][col] == '#' or mj[p1][col] == 'B':
                                    break
                                else:
                                    print("A posição inserida ja foi usada.")
                            else:
                                print("Insira uma posição dentro do intervalo.")
                        else:
                            print("Insira uma posição dentro do intervalo.")
                    else:
                        p1 = p[0]
                        p1 = int(p1)
                        if mj[p1][col] == '#' or mj[p1][col] == 'B':
                            break
                        else:
                            print("A posição inserida ja foi usada.")
                else:
                    print("Insira uma posição dentro do intervalo.") 
            else:
                print("Insira a posição corretamente.")
        elif modo == 'C':
            if len(p) == 2:
                if 65 <= ord(p[0]) <= 75 and 48 <= ord(p[1]) <= 56:
                    col = p[0]
                    p.remove(col)
                    col = ord(col)
                    col -= 65
                    p1 = p[0]
                    p1 = int(p1)
                    if mj[p1][col] == '#' or mj[p1][col] == 'B':
                        break
                    else:
                        print("A posição inserida ja foi usada.")
                else:
                    print("Insira uma posição dentro do intervalo.") 
            else:
                print("Insira a posição corretamente.")
    return col, p1

def Bandeira(col, lin, mj):
    if mj[col][lin] == 'B':
        mj[col][lin] = '#'
    else:
        mj[col][lin] = 'B'

def CavaPonto2(lin, col, mj, mr, dir, maxcol, maxlin):
    if mr[lin][col] != '.':
        mj[lin][col] = mr[lin][col]
    else:
        #abre lateral
        mj[lin][col] = mr[lin][col]
        if col != maxcol:
            mj[lin][col + 1] = mr[lin][col + 1]
        if lin != 0:
            mj[lin - 1][col] = mr[lin - 1][col]
        if col != 0:
            mj[lin][col - 1] = mr[lin][col - 1]
        if lin != maxlin:
            mj[lin + 1][col] = mr[lin + 1][col]
        #pula pro proximo
        if dir == 1 and col != maxcol:
            CavaPonto2(lin, col + 1, mj, mr, 1, maxcol, maxlin)
        elif dir == 2 and lin != 0:
            CavaPonto2(lin - 1, col, mj, mr, 2, maxcol, maxlin)
        elif dir == -1 and col != 0:
            CavaPonto2(lin, col - 1, mj, mr, -1, maxcol, maxlin)
        elif dir == -2 and lin != maxlin:
            CavaPonto2(lin + 1, col, mj, mr, -2, maxcol, maxlin)

def CavaPonto(lin, col, mj, mr, dir, modo):
    if modo == 'L':
        maxcol = 17
        maxlin = 14
    elif modo == 'C':
        maxcol = 10
        maxlin = 8
    if mr[lin][col] != '.':
        mj[lin][col] = mr[lin][col]
    else:
        #abre lateral
        mj[lin][col] = mr[lin][col]
        if col != maxcol:
            mj[lin][col + 1] = mr[lin][col + 1]
        if lin != 0:
            mj[lin - 1][col] = mr[lin - 1][col]
        if col != 0:
            mj[lin][col - 1] = mr[lin][col - 1]
        if lin != maxlin:
            mj[lin + 1][col] = mr[lin + 1][col]
        #pula pro proximo
        if dir != -1 and col != maxcol:
            CavaPonto2(lin, col + 1, mj, mr, 1, maxcol, maxlin)
        if dir != -2 and lin != 0:
            CavaPonto2(lin - 1, col, mj, mr, 2, maxcol, maxlin)
        if dir != 1 and col != 0:
            CavaPonto2(lin, col - 1, mj, mr, -1, maxcol, maxlin)
        if dir != 2 and lin != maxlin:
            CavaPonto2(lin + 1, col, mj, mr, -2, maxcol, maxlin)
    
def Verifica(col, lin, mj, mr, modo):
    f = 1
    if mr[lin][col] == 'X':
        f = 0
        mj[lin][col] = mr[lin][col]
    else:
        f = 1
        if mr[lin][col] == '.':
            CavaPonto(lin, col, mj, mr, 0, modo)
        else:
            mj[lin][col] = mr[lin][col]
    return f

def main():
    print("--------- CAMPO MINADO ---------")
    print()
    while True:
        e = '/'
        while '1' != e != '2' and e != '3':
            print("[1] Modo Curto   [2] Modo Longo")
            print("         [3] Sair")
            print("-> ", end="")
            e = input()
            print()

        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        elif e == '1':
            mj = []
            print("   A B C D E F G H I J K")
            for i in range(9):
                if i <= 9:
                    print("%d  " %i, end="")
                else:
                    print("%d " %i, end="")
                mj.append([])
                for j in range(11):
                    mj[i].append('#')
                    print("%s " %mj[i][j], end="")  
                print()
            print()
            mr = []
            mr = CriaJogo('C')
            while True:
                print("Insira a posição que deseja jogar: (letra primeiro, depois o número)")
                col, lin = Posicao(mj, 'C')
                print("O que deseja fazer?")
                r = 1
                if mj[lin][col] == '#':
                    print("[1] Cavar o lugar     [2] Colocar uma bandeira")
                    if Escolha(2) == '2':
                        Bandeira(lin, col, mj)
                    else:
                        r = Verifica(col, lin, mj, mr, 'C')
                else:
                    print("[1] Tirar a bandeira   [2] Não fazer nada")
                    if Escolha(2) == '1':
                        Bandeira(lin, col, mj)
                TelaJogo(mj, 'C')
                if r == 0:
                    print(colors.red + "FIM DE JOGO!!" + colors.fim)
                    print("VOCE PERDEU")
                    break
                f = 0
                for i in range(9):
                    for j in range(11):
                        if mj[i][j] == '#':
                            f = 1
                if f == 0:
                    print(colors.green + "FIM DE JOGO!!" + colors.fim)
                    print("VOCE GANHOU")
                    break

        elif e == '2':
            mj = []
            print("   A B C D E F G H I J K L M N O P Q R")
            for i in range(15):
                if i <= 9:
                    print("%d  " %i, end="")
                else:
                    print("%d " %i, end="")
                mj.append([])
                for j in range(18):
                    mj[i].append('#')
                    print("%s " %mj[i][j], end="")  
                print()
            print()
            mr = []
            mr = CriaJogo('L')
            while True:
                print("Insira a posição que deseja jogar: (letra primeiro, depois o número)")
                col, lin = Posicao(mj, 'L')
                print("O que deseja fazer?")
                r = 1
                if mj[lin][col] == '#':
                    print("[1] Cavar o lugar     [2] Colocar uma bandeira")
                    if Escolha(2) == '2':
                        Bandeira(lin, col, mj)
                    else:
                        r = Verifica(col, lin, mj, mr, 'L')
                else:
                    print("[1] Tirar a bandeira   [2] Não fazer nada")
                    if Escolha(2) == '1':
                        Bandeira(lin, col, mj)
                TelaJogo(mj, 'L')
                if r == 0:
                    print(colors.red + "FIM DE JOGO!!" + colors.fim)
                    print("VOCE PERDEU")
                    break
                f = 0
                for i in range(15):
                    for j in range(18):
                        if mj[i][j] == '#':
                            f = 1
                if f == 0:
                    print(colors.green + "FIM DE JOGO!!" + colors.fim)
                    print("VOCE GANHOU")
                    break    
            
        print("[1] Jogar Novamente   [2] Sair")
        e = 0
        if Escolha(2) == '2':
            print("ENCERRANDO JOGO...")
            break
        else:
            print("INICIANDO NOVO JOGO...")
            print()

main()
