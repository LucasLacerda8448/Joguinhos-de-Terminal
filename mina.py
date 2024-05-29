import random

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

def VerificaLado(pos_x, pos_y, m):
    qb = 0
    #dir
    if pos_y != 17:
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
    if pos_x != 14:
        if m[pos_x + 1][pos_y] == 'X':
            qb += 1
    #d_esq_up
    if pos_y != 0 and pos_x != 0:
        if m[pos_x - 1][pos_y - 1] == 'X':
            qb += 1
    #d_dir_up
    if pos_y != 17 and pos_x != 0:
        if m[pos_x - 1][pos_y + 1] == 'X':
            qb += 1
    #d_esq_down
    if pos_y != 0 and pos_x != 14:
        if m[pos_x + 1][pos_y - 1] == 'X':
            qb += 1
    #d_dir_down
    if pos_y != 17 and pos_x != 14:
        if m[pos_x + 1][pos_y + 1] == 'X':
            qb += 1

    if qb == 0:
        return '.'
    else:
        return str(qb)

def CriaJogo():
    m2 = []
    for i in range(15):
        m2.append([])
        for j in range(18):
            m2[i].append('.')

    for i in range(40):
        while True:
            x = random.randint(0, 14)
            y = random.randint(0, 17)
            if m2[x][y] == '.':
                m2[x][y] = 'X'
                break
    
    for i in range(15):
        for j in range(18):
            if m2[i][j] == '.':
                m2[i][j] = VerificaLado(i, j, m2)
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
    #40 bombas
    #a partir de onde ele escolher, andar 5 casas por 4 linhas, parar e pular pra proxima
    #linha se encontrar uma bomba
    #letra depois num
    print("-- CAMPO MINADO --")
    print()
    while True:
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
            mr = CriaJogo()
            while True:
                print("Insira a posição que deseja jogar: (letra primeiro, depois o número)")
                while True:
                    print("-> ", end="")
                    p1 = input()
                    p = []
                    for i in range(len(p1)):
                        p.append(p1[i])
                    if 2 <= len(p) <= 3:
                        if 65 <= ord(p[0]) <= 82 and 48 <= ord(p[1]) <= 57:
                            col = p[0]
                            p.remove(col)
                            if len(p) == 2:
                                if 48 <= ord(p[1]) <= 52:
                                    p1 = p[0] + p[1]
                                    p1 = int(p1)
                                    if p1 <= 14:
                                        break
                                    else:
                                        print("Insira uma posição dentro do intervalo.")
                                else:
                                    print("Insira uma posição dentro do intervalo.")
                            else:
                                p1 = p[0]
                                p1 = int(p1)
                                break
                        else:
                            print("Insira uma posição dentro do intervalo.") 
                    else:
                        print("Insira a posição corretamente.")
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
