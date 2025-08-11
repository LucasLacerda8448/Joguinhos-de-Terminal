import os
import random
#os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    grey = '\033[90m'
    RED = '\033[101m'
    BLUE = '\033[104m'
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
    print("    A B C   D E F   G H I")
    print("  +-------+-------+-------+")
    for i in range(9):
        print("%d | " %i, end="")
        for j in range(9):
            if sj[i][j] == 0:
                print("  ", end="")
            else:
                if si[i][j] == 0:
                    print(colors.grey + "%d " %sj[i][j] + colors.fim, end="")
                else:
                    print("%d " %sj[i][j], end="")
            if j == 2 or j == 5:
                print("| ", end="")
        print("|")
        if i == 2 or i == 5:
            print("  +-------+-------+-------+")
    print("  +-------+-------+-------+")
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
    print("  A B C D E F G H I J K L M N O P Q")
    for i in range(9):
        print("%d " %i, end="")
        if i == 0:
            for j in range(17):
                if (j % 2) == 0:
                    print("  ", end="")
                else:
                    print("_ ", end="")
            print()
        else:
            for j in range(17):
                if (j % 2) == 0:
                    print("|", end="")
                else:
                    print(" _ ", end="")
            print()
    print()

    print("------- JOGO DAS LINHAS -------")
    print()
    while True:
        print("========= OPÇÕES =========")
        print("[1] Jogar   [2] Instruções")
        print("        [3] Sair")
        e = Escolha(3)
        if e == '3':
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
                print("    A B C   D E F   G H I")
                print("  +-------+-------+-------+")
                for i in range(9):
                    print("%d | " %i, end="")
                    for j in range(9):
                        if sj[i][j] == 0:
                            if i == lin and j == col:
                                print(colors.yellow + "* " + colors.fim, end="")
                            else:
                                print("  ", end="")
                        else:
                            if si[i][j] == 0:
                                if i == lin and j == col:
                                    print(colors.yellow + "%d " %sj[i][j] + colors.fim, end="")
                                else:
                                    print(colors.grey + "%d " %sj[i][j] + colors.fim, end="")
                            else:
                                print("%d " %sj[i][j], end="")
                        if j == 2 or j == 5:
                            print("| ", end="")
                    print("|")
                    if i == 2 or i == 5:
                        print("  +-------+-------+-------+")
                print("  +-------+-------+-------+")
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
