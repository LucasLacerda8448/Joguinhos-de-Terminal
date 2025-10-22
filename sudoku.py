import os
import random
os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    b_yellow = '\033[93m'
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

def IniciaJogo():
    j1 = [
        [0,7,0,4,0,5,6,0,0],
        [9,2,4,0,6,0,8,0,0],
        [1,0,5,0,0,8,7,0,0],
        [0,3,8,0,5,7,0,0,0],
        [0,0,0,0,0,0,0,7,3],
        [0,4,7,0,9,0,1,2,0],
        [4,0,9,6,0,2,0,0,1],
        [7,0,0,8,3,0,4,0,9],
        [0,1,0,5,4,9,0,0,0]
]
    j2 = [
        [0,0,0,2,0,9,5,4,0],
        [0,0,4,0,0,0,3,0,2],
        [0,1,0,0,3,0,0,0,0],
        [0,0,2,0,0,0,0,5,0],
        [0,4,0,3,0,1,0,0,7],
        [0,7,9,0,2,6,0,0,0],
        [3,0,8,0,4,2,7,1,5],
        [6,0,1,0,0,0,0,9,0],
        [4,0,7,1,9,8,2,0,6]
    ]
    j3 = [
        [0,3,0,0,0,0,0,0,0],
        [7,0,0,3,0,0,0,8,0],
        [1,0,0,2,8,4,0,3,0],
        [0,2,9,0,6,3,0,0,8],
        [0,0,8,4,0,5,0,2,6],
        [5,0,0,0,2,0,0,0,0],
        [0,0,4,0,7,0,5,0,0],
        [2,5,0,8,0,0,6,0,0],
        [6,0,0,0,0,0,0,7,0]
    ]
    j4 = [
        [0,0,0,0,1,3,0,0,0],
        [0,0,0,6,8,0,0,1,0],
        [7,0,9,0,0,0,0,8,0],
        [0,0,0,0,4,5,0,0,1],
        [0,0,5,0,0,6,3,0,0],
        [3,4,0,0,0,0,0,0,0],
        [5,0,0,0,0,9,0,0,0],
        [0,7,0,0,6,2,5,9,0],
        [0,2,0,0,0,0,0,0,4]
    ]
    j5 = [
        [0,1,3,0,2,0,0,0,6],
        [0,5,0,0,8,0,0,0,0],
        [0,0,0,0,0,0,3,0,4],
        [0,0,0,0,6,4,0,0,1],
        [0,7,9,0,0,0,0,5,0],
        [0,0,0,0,0,0,7,0,0],
        [0,0,6,0,4,9,0,1,5],
        [0,0,0,8,0,1,9,0,0],
        [0,0,1,0,0,0,4,0,0]
    ]
    j6 = [
        [0,0,8,0,3,0,0,0,1],
        [2,0,3,4,0,0,0,0,0],
        [0,0,0,0,2,0,0,0,0],
        [0,0,0,0,6,4,0,1,0],
        [0,0,0,0,0,0,2,3,8],
        [0,0,0,0,0,7,0,4,0],
        [4,0,0,0,0,0,0,0,5],
        [0,1,0,0,0,0,8,0,0],
        [0,6,0,5,0,9,0,0,0]
    ]
    
    e = random.randint(1, 6)
    if e == 1:
        return j1
    elif e == 2:
        return j2
    elif e == 3:
        return j3
    elif e == 4:
        return j4
    elif e == 5:
        return j5
    else:
        return j6

def Posicao(si):
    while True:
        print("-> ", end="")
        p1 = input()
        p = []
        for i in range(len(p1)):
            p.append(p1[i])
        if len(p) == 2:
            if 65 <= ord(p[0]) <= 73 and 48 <= ord(p[1]) <= 56:
                col = p[0]
                p.remove(col)
                col = ord(col)
                col -= 65
                p1 = p[0]
                p1 = int(p1)
                if si[p1][col] == 0:
                    break
                else:
                    print("A posição inserida não pode ser usada.")
            else:
                print("Insira uma posição dentro do intervalo.") 
        else:
            print("Insira a posição corretamente.")
    return col, p1

def ImprimeJogo(sj, si):
    print("    A   B   C   D   E   F   G   H   I")
    print("  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    for i in range(9):
        print("%d ║ " %i, end="")
        for j in range(9):
            if sj[i][j] == 0:
                print("  ", end="")
            else:
                if si[i][j] == 0:
                    print(colors.b_yellow + "%d " %sj[i][j] + colors.fim, end="")
                else:
                    print("%d " %sj[i][j], end="")
            if j == 2 or j == 5:
                print("║ ", end="")
            elif j != 8:
                print(colors.grey + "│ " + colors.fim, end="")
        print("║")
        if i == 2 or i == 5:
            print("  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
        elif i != 8:
            print("  ╟" + colors.grey + "───┼───┼───" + colors.fim + "╫" + colors.grey+ "───┼───┼───" + colors.fim + "╫" + colors.grey + "───┼───┼───" + colors.fim + "╢")
    print("  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
    print()

def Verifica(sj, x, y, e):
    c = 0
    for i in range(9):
        for j in range(9):
            if sj[i][j] == 0:
                c = 1
                break
        if c == 1:
            break
    if c == 0:
        for i in range(9):
            if sj[i][y] == e and i != x:
                c == 1
                break
            if sj[x][i] == e and i != y:
                c == 1
                break
        if 0 <= x <= 2:
            if 0 <= y <= 2:
                for i in range(3):
                    for j in range(3):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
            elif 3 <= y <= 5:
                for i in range(3):
                    for j in range(3,6):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
            else:
                for i in range(3):
                    for j in range(6,9):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
        elif 3 <= x <= 5:
            if 0 <= y <= 2:
                for i in range(3,6):
                    for j in range(3):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
            elif 3 <= y <= 5:
                for i in range(3,6):
                    for j in range(3,6):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
            else:
                for i in range(3,6):
                    for j in range(6,9):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
        else:
            if 0 <= y <= 2:
                for i in range(6,9):
                    for j in range(3):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
            elif 3 <= y <= 5:
                for i in range(6,9):
                    for j in range(3,6):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
            else:
                for i in range(6,9):
                    for j in range(6,9):
                        if sj[i][j] == e and i != x and j != y:
                            c == 1
                            break
    if c == 1:
        return 'C'
    else:
        return 'E'

def main():
    print("╔═══╤═══╤════╤═══╤═══╗")
    print("║   │   SUDOKU   │   ║")
    print("╚═══╧═══╧════╧═══╧═══╝")
    while True:
        print("╔═══╤═════╗ ╔═══╤════╗")
        print("║ 1 │Jogar║ ║ 2 │Sair║")
        print("╚═══╧═════╝ ╚═══╧════╝")
        e = Escolha(2)
        if e == '2':
            print("ENCERRANDO JOGO...")
            break
        elif e == '1':
            si = IniciaJogo()
            sj = []
            for i in range(9):
                sj.append([])
                for j in range(9):
                    sj[i].append(si[i][j])
            ImprimeJogo(sj, si)
            while True:
                print("Insira a posição que deseja jogar: (letra primeiro, depois o número)")
                col, lin = Posicao(si)
                print("    A   B   C   D   E   F   G   H   I")
                print("  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
                for i in range(9):
                    print("%d ║" %i, end="")
                    for j in range(9):
                        if sj[i][j] == 0:
                            if i == lin and j == col:
                                print(colors.yellow + "░░░" + colors.fim, end="")
                            else:
                                print("   ", end="")
                        else:
                            if si[i][j] == 0:
                                if i == lin and j == col:
                                    print(colors.yellow + " %d " %sj[i][j] + colors.fim, end="")
                                else:
                                    print(colors.b_yellow + " %d " %sj[i][j] + colors.fim, end="")
                            else:
                                print(" %d " %sj[i][j], end="")
                        if j == 2 or j == 5:
                            print("║", end="")
                        elif j != 8:
                            print(colors.grey + "│" + colors.fim, end="")
                    print("║")
                    if i == 2 or i == 5:
                        print("  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
                    elif i != 8:
                        print("  ╟" + colors.grey + "───┼───┼───" + colors.fim + "╫" + colors.grey+ "───┼───┼───" + colors.fim + "╫" + colors.grey + "───┼───┼───" + colors.fim + "╢")
                print("  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
                print()
                print("O que deseja fazer?")
                r = 1
                print("[1] Escrever   [2] Voltar")
                if Escolha(2) == '1':
                    print("Informe o número que deseja colocar:")
                    e2 = int(Escolha(9))
                    sj[lin][col] = e2
                    r = Verifica(sj, lin, col, e2)
                ImprimeJogo(sj, si)
                if r == 'E':
                    print(colors.green + "FIM DE JOGO!!" + colors.fim)
                    print("VOCE GANHOU")
                    break

        print("[1] Jogar Novamente   [2] Sair")
        e2 = Escolha(2)
        if e2 == '2':
            print("ENCERRANDO JOGO...")
            break
        elif e2 == '1':
            print("INICIANDO NOVO JOGO...")
            print()

main()
