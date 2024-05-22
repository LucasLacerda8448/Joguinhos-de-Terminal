import os
#os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
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

def AdicionaBola(p, mj):
    v = 6
    for i in range(6)[::-1]:
        if mj[i][p] == '*':
            v = i
            break
    return v

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
            if p4 == '*':
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
    for i in range(6):
        h = [0, 1, 2, 3]
        for j in range(4):
            p1 = m[i][h[0]]
            p2 = m[i][h[1]]
            p3 = m[i][h[2]]
            p4 = m[i][h[3]]
            if p1 == '*' or p2 == '*' or p3 == '*' or p4 == '*':
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
            if p1 == '*' or p2 == '*' or p3 == '*' or p4 == '*':
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
            if p1 == '*' or p2 == '*' or p3 == '*' or p4 == '*':
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
        print("    0 1 2 3 4 5 6")
        for i in range(6):
            print("    ", end="")
            mi.append([])
            for j in range(7):
                mi[i].append('O')
                print(colors.blue + "%s " %mi[i][j] + colors.fim, end="")
            print()
        print()

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
                    mj[i].append('*')

            v = 'O'
            print("Jogador " + colors.yellow + "O" + colors.fim + " começa.")
            while True:
                print("Escolha a coluna que deseja jogar:")
                while True:
                    p = '/'
                    while '0' != p != '1' and '2' != p != '3' and '4' != p != '5' and '6' != p:
                        print("-> ", end="")
                        p = input()
                    p = int(p)
                    i = AdicionaBola(p, mj)
                    if i == 6:
                        print("A coluna escolhida ja está cheia, escolha outra coluna.")
                    else:
                        mj[i][p] = v
                        print()
                        break
                r = Verifica(mj)
                print("    0 1 2 3 4 5 6")
                for i in range(6):
                    print("    ", end="")
                    for j in range(7):
                        if mj[i][j] == '*':
                            print(colors.blue + "%s " %mi[i][j] + colors.fim, end="")
                        elif mj[i][j] == 'X':
                            print(colors.red + "%s " %mi[i][j] + colors.fim, end="")
                        elif mj[i][j] == 'O':
                            print(colors.yellow + "%s " %mi[i][j] + colors.fim, end="")
                        elif mj[i][j] == 'V':
                            print(colors.green + "%s " %mi[i][j] + colors.fim, end="")
                    print()
                print()
                if r == 'C':
                    if v == 'O':
                        v = 'X'
                        print("Vez do jogador " + colors.red + "O" + colors.fim + ".")
                    else:
                        v = 'O'
                        print("Vez do jogador " + colors.yellow + "O" + colors.fim + ".")
                else:
                    print("FIM DE JOGO!")
                    if r == 'O':
                        print("Jogador " + colors.yellow + "O" + colors.fim + " Venceu.")
                    elif r == 'X':
                        print("Jogador " + colors.red + "O" + colors.fim + " Venceu.")
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
