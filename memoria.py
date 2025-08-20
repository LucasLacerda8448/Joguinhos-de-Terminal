import random

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    purple = '\033[95m'
    fim = '\033[0m'

def CriaJogo():
    l = ['☻', '♥', '♦', '♣', '♠', '♂', '♀', '♫']
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

def CriaJogo2():
    l = ['☻', '♥', '♦', '♣', '♠', '•', '◙', '♂', '♀', '♪', '♫', '☼', '‼', '¶', '►', '◄', '▲', '§']
    m2 = []

    for i in range(6):
        m2.append([])
        for j in range(6):
            m2[i].append('#')

    for i in l:
        for j in range(2):
            while True:
                x = random.randint(0, 5)
                y = random.randint(0, 5)
                if m2[x][y] == '#':
                    m2[x][y] = i
                    break
    return m2

def Verifica(m, t):
    for i in range(t):
        for j in range(t):
            if m[i][j] == '#':
                return 0
    return 1

def Posicao(mj, tam):
    while True:
        print("-> ", end="")
        p1 = input()
        p = []
        for i in range(len(p1)):
            p.append(p1[i])
        if tam == 4:
            if len(p) == 2:
                if 48 <= ord(p[0]) <= 51 and 48 <= ord(p[1]) <= 51:
                    x = int(p[0])
                    y = int(p[1])
                    if mj[x][y] == '#':
                        break
                    else:
                        print("A posição inserida já foi usada, insira outro valor.")
                else:
                    print("Insira uma posição dentro do intervalo.")
            elif len(p) == 3:
                if 48 <= ord(p[0]) <= 51 and ord(p[1]) == 32 and 48 <= ord(p[2]) <= 51:
                    x = int(p[0])
                    y = int(p[2])
                    if mj[x][y] == '#':
                        break
                    else:
                        print("A posição inserida já foi usada, insira outro valor.")
                else:
                    print("Insira uma posição dentro do intervalo.")
            else:
                print("Insira a posição corretamente.")
        elif tam == 6:
            if len(p) == 2:
                if 48 <= ord(p[0]) <= 53 and 48 <= ord(p[1]) <= 53:
                    x = int(p[0])
                    y = int(p[1])
                    if mj[x][y] == '#':
                        break
                    else:
                        print("A posição inserida já foi usada, insira outro valor.")
                else:
                    print("Insira uma posição dentro do intervalo.")
            elif len(p) == 3:
                if 48 <= ord(p[0]) <= 53 and ord(p[1]) == 32 and 48 <= ord(p[2]) <= 53:
                    x = int(p[0])
                    y = int(p[2])
                    if mj[x][y] == '#':
                        break
                    else:
                        print("A posição inserida já foi usada, insira outro valor.")
                else:
                    print("Insira uma posição dentro do intervalo.")
            else:
                print("Insira a posição corretamente.")
    return x, y

def main():
    print("- JOGO DA MEMÓRIA -")
    print()
    while True:
        e = '/'
        while '1' != e != '2' and e != '3':
            print("[1] 4x4  [2] 6x6")
            print("    [3] Sair")
            print("-> ", end="")
            e = input()
            print()

        if e == '3':
            print("ENCERRANDO JOGO...")
            break

        elif e == '1':
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
            mr = []
            mr = CriaJogo()
            v = 1
            p1 = 0
            p2 = 0
            print("Jogador 1 começa.")
            while True:
                v2 = 0
                print("Insira a posição da primeira carta:")
                x, y = Posicao(mj, 4)
                print()
                print("  0 1 2 3")
                for i in range(4):
                    print("%d " %i, end="")
                    for j in range(4):
                        if x == i and y == j:
                            print(colors.yellow + "%s " %mr[x][y] + colors.fim, end="")
                        else:
                            print("%s " %mj[i][j], end="")
                    print()
                print()
                print("Insira a posição da segunda carta:")
                while True:
                    x2, y2 = Posicao(mj, 4)
                    if x2 == x and y2 == y:
                        print("A posição inserida já foi usada, insira outro valor.")
                    else:
                        break
                print()
                print("  0 1 2 3")
                for i in range(4):
                    print("%d " %i, end="")
                    for j in range(4):
                        if x == i and y == j:
                            print(colors.yellow + "%s " %mr[x][y] + colors.fim, end="")
                        elif x2 == i and y2 == j:
                            print(colors.yellow + "%s " %mr[x2][y2] + colors.fim, end="")
                        else:
                            print("%s " %mj[i][j], end="")
                    print()
                print()
                if mr[x][y] == mr[x2][y2]:
                    mj[x][y] = ' '
                    mj[x2][y2] = ' '
                    print("Cartas iguais!")
                    v2 = 1
                r = Verifica(mj, 4)
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
                    print("Aperte Enter para continuar...")
                    cont = input()
                    print("  0 1 2 3")
                    for i in range(4):
                        print("%d " %i, end="")
                        for j in range(4):
                            print("%s " %mj[i][j], end="")
                        print()
                    print()
                elif r == 1:
                    if v2 == 1:
                        if v == 1:
                            p1 = p1 + 1
                        else:
                            p2 = p2 + 1
                    print()
                    print("==== FIM DE JOGO! ====")
                    print("       PLACAR:")
                    print("    %d     X     %d" %(p1, p2))
                    print("Jogador 1    Jogador 2")
                    print()
                    if p1 > p2:
                        print("VITÓRIA DO JOGADOR 1!")
                    elif p2 > p1:
                        print("VITÓRIA DO JOGADOR 2!")
                    elif p1 == p2:
                        print("EMPATE!")
                    print()
                    break

        elif e == '2':
            mj = []
            print("  0 1 2 3 4 5")
            for i in range(6):
                print("%d " %i, end="")
                mj.append([])
                for j in range(6):
                    mj[i].append('#')
                    print("%s " %mj[i][j], end="")
                print()
            print()
            mr = []
            mr = CriaJogo2()
            v = 1
            p1 = 0
            p2 = 0
            print("Jogador 1 começa.")
            while True:
                v2 = 0
                print("Insira a posição da primeira carta:")
                x, y = Posicao(mj, 6)
                print()
                print("  0 1 2 3 4 5")
                for i in range(6):
                    print("%d " %i, end="")
                    for j in range(6):
                        if x == i and y == j:
                            print(colors.yellow + "%s " %mr[x][y] + colors.fim, end="")
                        else:
                            print("%s " %mj[i][j], end="")
                    print()
                print()
                print("Insira a posição da segunda carta:")
                while True:
                    x2, y2 = Posicao(mj, 6)
                    if x2 == x and y2 == y:
                        print("A posição inserida já foi usada, insira outro valor.")
                    else:
                        break
                print()
                print("  0 1 2 3 4 5")
                for i in range(6):
                    print("%d " %i, end="")
                    for j in range(6):
                        if x == i and y == j:
                            print(colors.yellow + "%s " %mr[x][y] + colors.fim, end="")
                        elif x2 == i and y2 == j:
                            print(colors.yellow + "%s " %mr[x2][y2] + colors.fim, end="")
                        else:
                            print("%s " %mj[i][j], end="")
                    print()
                print()
                if mr[x][y] == mr[x2][y2]:
                    mj[x][y] = ' '
                    mj[x2][y2] = ' '
                    print("Cartas iguais!")
                    v2 = 1
                r = Verifica(mj, 6)
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
                    print("Aperte Enter para continuar...")
                    cont = input()
                    print("  0 1 2 3 4 5")
                    for i in range(6):
                        print("%d " %i, end="")
                        for j in range(6):
                            print("%s " %mj[i][j], end="")
                        print()
                    print()
                elif r == 1:
                    if v2 == 1:
                        if v == 1:
                            p1 = p1 + 1
                        else:
                            p2 = p2 + 1
                    print("==== FIM DE JOGO! ====")
                    print("       PLACAR:")
                    print("    %d     X     %d" %(p1, p2))
                    print("Jogador 1    Jogador 2")
                    if p1 > p2:
                        print("VITÓRIA DO JOGADOR 1!")
                    elif p2 > p1:
                        print("VITÓRIA DO JOGADOR 2!")
                    elif p1 == p2:
                        print("EMPATE!")
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
