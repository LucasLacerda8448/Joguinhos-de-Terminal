import random

def CriaJogo():
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    m2 = []

    for i in range(4):
        m2.append([])
        for j in range(4):
            m2[i].append('#')

    for i in l:
        for j in range(2):
            while True:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
                if m2[x][y] == '#':
                    m2[x][y] = i
                    break
    return m2

def Verifica(m):
    f = 1
    for i in range(4):
        for j in range(4):
            if m[i][j] == '#':
                f = 0
    if f == 0:
        return 0
    else:
        return 1

def main():
    print("-- JOGO DA MEMÓRIA --")
    print()
    while True:
        mj = []
        print("  0 1 2 3")
        for i in range(4):
            print("%d " %i, end="")
            mj.append([])
            for j in range(4):
                mj[i].append('#')
                print("%s " %mj[i][j], end="")
            print()
        print()

        e = '/'
        while '1' != e != '2':
            print("[1] Jogar   [2] Sair")
            print("-> ", end="")
            e = input()
            print()

        if e == '2':
            print("ENCERRANDO JOGO...")
            break
        elif e == '1':
            mr = []
            mr = CriaJogo()
            v = 1
            p1 = 0
            p2 = 0
            print("Jogador 1 começa.")
            while True:
                v2 = 0
                print("Insira a posição da primeira carta:")
                while True:
                    print("-> ", end="")
                    x, y = map(int, input().split())
                    if 0 > x or x > 3 or 0 > y or y > 3:
                        print("Valores inválidos, insira outro valor.")
                    elif mj[x][y] != '#':
                        print("A posição inserida ja foi usada, insira outro valor.")
                    else:
                        print()
                        break
                print("  0 1 2 3")
                for i in range(4):
                    print("%d " %i, end="")
                    for j in range(4):
                        if x == i and y == j:
                            print("%s " %mr[x][y], end="")
                        else:
                            print("%s " %mj[i][j], end="")
                    print()
                print()
                print("Insira a posição da segunda carta:")
                while True:
                    print("-> ", end="")
                    x2, y2 = map(int, input().split())
                    if 0 > x2 or x2 > 3 or 0 > y2 or y2 > 3:
                        print("Valores inválidos, insira outro valor.")
                    elif mj[x2][y2] != '#':
                        print("A posição inserida ja foi usada, insira outro valor.")
                    else:
                        print()
                        break
                print("  0 1 2 3")
                for i in range(4):
                    print("%d " %i, end="")
                    for j in range(4):
                        if x == i and y == j:
                            print("%s " %mr[x][y], end="")
                        elif x2 == i and y2 == j:
                            print("%s " %mr[x2][y2], end="")
                        else:
                            print("%s " %mj[i][j], end="")
                    print()
                print()
                if mr[x][y] == mr[x2][y2]:
                    mj[x][y] = ' '
                    mj[x2][y2] = ' '
                    print("Cartas iguais!")
                    v2 = 1
                r = Verifica(mj)
                if r == 0:
                    if v2 == 1:
                        print("Jogador %d joga mais uma vez." %v)
                        if v == 1:
                            p1 = p1 + 1
                        else:
                            p2 = p2 + 1
                    else:
                        if v == 1:
                            v = 2
                        else:
                            v = 1
                        print("Vez do jogador %d." %v)
                    print()
                    print("  0 1 2 3")
                    for i in range(4):
                        print("%d " %i, end="")
                        for j in range(4):
                            print("%s " %mj[i][j], end="")
                        print()
                    print()
                elif r == 1:
                    print("FIM DE JOGO!")
                    if p1 > p2:
                        p1 = p1 + 1
                        print("Jogador 1 venceu com uma pontuação de %d pares de cartas." %p1)
                    elif p2 > p1:
                        p2 = p2 + 1
                        print("Jogador 2 venceu com uma pontuação de %d pares de cartas." %p2)
                    elif p1 == p2:
                        print("Jogo empatado, ambos os jogadores obtiveram %d pares de cartas." %p1)
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
