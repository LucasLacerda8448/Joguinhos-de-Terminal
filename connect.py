import os
os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    BLUE = '\033[104m'
    grey = '\033[90m'
    black = '\033[30m'
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

def AdicionaBola(p, mj):
    for i in range(6)[::-1]:
        if mj[i][p-1] == '◯':
            return i
    return 6

def Verifica(m):
    c = 0
    #Vertical
    for i in range(7):
        h = [5, 4, 3, 2]
        for j in range(3):
            p1 = m[h[0]][i]
            p2 = m[h[1]][i]
            p3 = m[h[2]][i]
            p4 = m[h[3]][i]
            if p4 == '◯':
                c = 1
                break
            elif p1 == p2 == p3 == p4:
                m[h[0]][i] = 'V'
                m[h[1]][i] = 'V'
                m[h[2]][i] = 'V'
                m[h[3]][i] = 'V'
                return p1
            h[0] -= 1
            h[1] -= 1
            h[2] -= 1
            h[3] -= 1
    #Horizontal
    for i in range(6)[::-1]:
        h = [0, 1, 2, 3]
        for j in range(4):
            p1 = m[i][h[0]]
            p2 = m[i][h[1]]
            p3 = m[i][h[2]]
            p4 = m[i][h[3]]
            if p1 == '◯' or p4 == '◯':
                c = 1
            elif p1 == p2 == p3 == p4:
                m[i][h[0]] = 'V'
                m[i][h[1]] = 'V'
                m[i][h[2]] = 'V'
                m[i][h[3]] = 'V'
                return p1
            h[0] += 1
            h[1] += 1
            h[2] += 1
            h[3] += 1
    #Diagonal1
    for i in range(4):
        h = [2, 3, 4, 5]
        for j in range(3):
            p1 = m[h[0]][i]
            p2 = m[h[1]][i + 1]
            p3 = m[h[2]][i + 2]
            p4 = m[h[3]][i + 3]
            if p1 == '◯' or p4 == '◯':
                c = 1
                break
            elif p1 == p2 == p3 == p4:
                m[h[0]][i] = 'V'
                m[h[1]][i + 1] = 'V'
                m[h[2]][i + 2] = 'V'
                m[h[3]][i + 3] = 'V'
                return p1
            h[0] -= 1
            h[1] -= 1
            h[2] -= 1
            h[3] -= 1
    #Diagonal2 
    for i in range(4):
        h = [5, 4, 3, 2]
        for j in range(3):
            p1 = m[h[0]][i]
            p2 = m[h[1]][i + 1]
            p3 = m[h[2]][i + 2]
            p4 = m[h[3]][i + 3]
            if p1 == '◯' or p4 == '◯':
                c = 1
                break
            elif p1 == p2 == p3 == p4:
                m[h[0]][i] = 'V'
                m[h[1]][i + 1] = 'V'
                m[h[2]][i + 2] = 'V'
                m[h[3]][i + 3] = 'V'
                return p1
            h[0] -= 1
            h[1] -= 1
            h[2] -= 1
            h[3] -= 1
    
    if c == 1:
        return 'C'
    else:
        return 'E'

def main():
    print("----- CONNECT-4 -----")
    print()
    while True:
        mi = []
        print(colors.blue + "  ┐ " + colors.fim + "1 2 3 4 5 6 7" + colors.blue + " ┌")
        for i in range(6):
            print("  │ ", end="")
            mi.append([])
            for j in range(7):
                mi[i].append('◯')
                print("%s " %mi[i][j], end="")
            print("│")
        print(" ─┼───────────────┼─")
        print("  ┘               └" + colors.fim)

        print("[1] Jogar   [2] Sair")
        e = Escolha(2)
        if e == '2':
            print("ENCERRANDO JOGO...")
            break
        elif e == '1':
            mj = []
            for i in range(6):
                mj.append([])
                for j in range(7):
                    mj[i].append('◯')

            v = 'Y'
            print("Jogador " + colors.yellow + "⬤" + colors.fim + " começa.")
            while True:
                print("Escolha a coluna que deseja jogar:")
                while True:
                    p = int(Escolha(7))
                    i = AdicionaBola(p, mj)
                    if i == 6:
                        print("A coluna escolhida ja está cheia, escolha outra coluna.")
                    else:
                        mj[i][p-1] = v
                        print()
                        break
                r = Verifica(mj)
                print(colors.blue + "  ┐ " + colors.fim + "1 2 3 4 5 6 7" + colors.blue + " ┌")
                for i in range(6):
                    print("  │ ", end="")
                    for j in range(7):
                        if mj[i][j] == '◯':
                            print("%s " %mi[i][j], end="")
                        elif mj[i][j] == 'R':
                            print(colors.red + "⬤ " + colors.blue, end="")
                        elif mj[i][j] == 'Y':
                            print(colors.yellow + "⬤ " + colors.blue, end="")
                        elif mj[i][j] == 'V':
                            print(colors.green + "⬤ " + colors.blue, end="")
                    print("│")
                print(" ─┼───────────────┼─")
                print("  ┘               └" + colors.fim)
                if r == 'C':
                    if v == 'Y':
                        v = 'R'
                        print("Vez do jogador " + colors.red + "⬤" + colors.fim + ".")
                    else:
                        v = 'Y'
                        print("Vez do jogador " + colors.yellow + "⬤" + colors.fim + ".")
                else:
                    print("FIM DE JOGO!")
                    if r == 'Y':
                        print("Jogador " + colors.yellow + "⬤" + colors.fim + " Venceu.")
                    elif r == 'R':
                        print("Jogador " + colors.red + "⬤" + colors.fim + " Venceu.")
                    elif r == 'E':
                        print("Empate.")
                    print()
                    break

            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()
