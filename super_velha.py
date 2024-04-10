#     [0]     [1]     [2]
#0    * * *   * * *   * * *
#1[0] * * *   * * *   * * *
#2    * * *   * * *   * * *
#3
#4    * * *   O O O   * * *
#5[1] * * *   O   O   * * *
#6    * * *   O O O   * * *
#7
#8    * * *   * * *   X   X
#9[2] * * *   * * *     X  
#10    * * *   * * *   X   X
def ImprimeJogo(l0, l1, l2, l3, l4, l5, l6, l7, l8):
    p = 0
    c = 3
    print("     [0]     [1]     [2]")
    for i in range(11):
        if i == 3 or i == 7:
            print("     [%d]" %c, end="")
            c = c + 1
            print("     [%d]" %c, end="")
            c = c + 1
            print("     [%d]" %c)
            c = c + 1
        else:
            print("    ", end="")
        for j in range(11):
            if 0 <= i <= 2:
                if 0 <= j <= 2:
                    print("%s " %l0[p], end="")
                elif 4 <= j <= 6:
                    print("%s " %l1[p], end="")
                elif 8 <= j <= 10:
                    print("%s " %l2[p], end="")
            elif 4 <= i <= 6:
                if 0 <= j <= 2:
                    print("%s " %l3[p], end="")
                elif 4 <= j <= 6:
                    print("%s " %l4[p], end="")
                elif 8 <= j <= 10:
                    print("%s " %l5[p], end="")
            elif 8 <= i <= 10:
                if 0 <= j <= 2:
                    print("%s " %l6[p], end="")
                elif 4 <= j <= 6:
                    print("%s " %l7[p], end="")
                elif 8 <= j <= 10:
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

def main():
    print("JOGO DA VELHA")
    print()
    while True:
        j0 = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
        mi = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        si = []
        j1 = j2 = j3 = j4 = j5 = j6 = j7 = j8 = j0

        e = '/'
        while 's' != e != 'n':
            print("Começar jogo? (s/n):")
            print("-> ", end="")
            e = input()
            print()

        if e == 'n':
            print("ENCERRANDO JOGO...")
            break
        else:
            ImprimeJogo(j0, j1, j2, j3, j4, j5, j6, j7, j8)
            print("O jogador X começa.")
            v = 'X'
            while True:
                print("Insira a posição do jogo que deseja começar:")
                while True:
                    print("-> ", end="")
                    x, y = map(int, input().split())
                    if (x < 0 or x > 2) and (y < 0 or y > 2):
                        print("Valores inválidos, insira outro valor.")
                    elif j0[p1] == 'X' or j0[p1] == 'O':
                        print("A posição inserida ja está ocupada, insira outro valor.")
                    else:
                        j0[p1] = v
                        print()
                        break

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

            e2 = '/'
            while 's' != e2 != 'n':
                print("Jogar novamente? (s/n):")
                print("-> ", end="")
                e2 = input()
                print()

            if e2 == 'n':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()
