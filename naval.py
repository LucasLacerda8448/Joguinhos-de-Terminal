import os
import random
import time
#os.system('color')

class colors:
    red = '\033[91m'
    RED = '\033[41m'
    green = '\033[32m'
    b_yellow = '\033[93m'
    yellow = '\033[33m'
    d_blue = '\033[34m'
    blue = '\033[94m'
    b_blue = '\033[36m'
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

def Posicao(jg, f, v):
    while True:
        print("-> ", end="")
        p1 = input()
        if len(p1) == 2:
            if 65 <= ord(p1[0]) <= 74 and 48 <= ord(p1[1]) <= 57:
                col = ord(p1[0]) - 65
                lin = int(p1[1])
                if jg[lin][col] == '░░░':
                    if f == 1:
                        break
                    else:
                        reg = lin + 1
                        reg2 = col + 1
                        if v == 0: #Horizontal
                            if (col + f - 1) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(f-1):
                                    if jg[lin][reg2] == '░░░':
                                        reg2 += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg2 - col) == f:
                                break
                        else:
                            if (lin + f - 1) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(f-1):
                                    if jg[reg][col] == '░░░':
                                        reg += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg - lin) == f:
                                break 
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            print("Insira a coordenada corretamente.")

    return col, lin

def Posicionar(pf):
    lista = [4, 3, 2, 1, 1]
    for r in range(11):
        c = 0
        print("    A   B   C   D   E   F   G   H   I   J")
        print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
        for i in range(10):
            print("%d " %i + colors.d_blue + "║", end="")
            for j in range(10):
                if pf[i][j] == 'O':
                    print(colors.green + "▐█▌", end="")
                else:
                    print(colors.blue + "%s" %pf[i][j], end="")

                if j == 9:
                    print(colors.d_blue + "║", end="")
                    if i == 3:
                        print(colors.fim + "        Frota:" + colors.d_blue)
                    elif i == 4:
                        if lista[1] == 0:
                            print(colors.grey + " [2] %dx Navios Comuns [■ ■]" %lista[1] + colors.d_blue)
                        else:
                            print(colors.fim + " [2] %dx Navios Comuns [■ ■]" %lista[1] + colors.d_blue)
                    elif i == 5:
                        if lista[3] == 0:
                            print(colors.grey + " [4] %dx Navio-tanque [■ ■ ■ ■]" %lista[3] + colors.d_blue) 
                        else:
                            print(colors.fim + " [4] %dx Navio-tanque [■ ■ ■ ■]" %lista[3] + colors.d_blue)
                    else:
                        print()
                else:
                    print(colors.d_blue + "│", end="")
            if i == 9:
                print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
            else:
                print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim, end="")
                if i == 3:
                    if lista[0] == 0:
                        print(colors.grey + " [1] %dx Submarinos [■]" %lista[0] + colors.fim)
                    else:
                        print(" [1] %dx Submarinos [■]" %lista[0])
                elif i == 4:
                    if lista[2] == 0:
                        print(colors.grey + " [3] %dx Contratorpedeiros [■ ■ ■]" %lista[2] + colors.fim)
                    else:
                        print(" [3] %dx Contratorpedeiros [■ ■ ■]" %lista[2])
                elif i == 5:
                    if lista[4] == 0:
                        print(colors.grey + " [5] %dx Porta-avião [■ ■ ■ ■ ■]" %lista[4] + colors.fim) 
                    else:
                        print(" [5] %dx Porta-avião [■ ■ ■ ■ ■]" %lista[4])
                else:
                    print()
                
        print()
        print("Selecione qual unidade posicionar")
        while True:
            fe = int(Escolha(5))
            if lista[fe-1] == 0:
                print("Você não possui mais esta unidade para posicionar, escolha outra")
            else:
                lista[fe-1] -= 1
                break
        while True:
            v = 0
            print("Como deseja posicionar sua unidade?")
            print("[1] Verticalmente  [2] Horizontalmente")
            if Escolha(2) == '1':
                v = 1
            print("Informe as coordenadas que deseja posicionar: (letra primeiro, depois o número)")
            col, lin = Posicao(pf, fe, v)
            x = lin
            y = col
            c = fe
            print("    A   B   C   D   E   F   G   H   I   J")
            print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
            for i in range(10):
                print("%d " %i + colors.d_blue + "║", end="")
                for j in range(10):
                    if i == x and j == y:
                        print(colors.yellow + " ■ ", end="")
                        pf[i][j] = 'T'
                        c -= 1
                        if v == 0 and c != 0:
                            y += 1
                        elif v == 1 and c != 0:
                            x += 1
                    else:
                        if pf[i][j] == 'O':
                            print(colors.green + "▐█▌", end="")
                        else:
                            print(colors.blue + "%s" %pf[i][j], end="")
                    if j == 9:
                        print(colors.d_blue + "║")
                    else:
                        print(colors.d_blue + "│", end="")
                if i == 9:
                    print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
                else:
                    print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
            print()
            print("A posição escolhida esta correta?")
            print("   [1] Sim          [2] Não")
            if Escolha(2) == '1':
                for i in range(10):
                    for j in range(10):
                        if pf[i][j] == 'T':
                            pf[i][j] = 'O'
                break
            else:
                for i in range(10):
                    for j in range(10):
                        if pf[i][j] == 'T':
                            pf[i][j] = '░░░'

    for i in range(30):
        print()

def Posicionar2(pf):
    lista = [4, 2, 2, 2, 1]
    cores = [[colors.b_yellow, colors.fim], [colors.b_yellow, colors.fim], [colors.b_yellow, colors.fim], [colors.b_yellow, colors.fim], [colors.b_yellow, colors.fim]]
    fro1 = [['0', '0', '0', '0', ' ', ' ', 'B']]
    fro2 = [['0', '0', '0', '1', ' ', ' ', 'C', ' ', ' ', 'b'], 
            ['0', '0', '1', '0', ' ', 'F', 'b']]
    fro3 = [['0', '0', '2', '0', ' ', 'F', 'f', 'b'],  
            ['1', '0', '0', '1', ' ', 'f', 'C', ' ', ' ', 'b'],  
            ['0', '0', '0', '2', ' ', ' ', 'C', ' ', ' ', 'c', ' ', ' ', 'b'],  
            ['0', '1', '1', '0', ' ', 'c', ' ', 'F', 'b'],  
            ['1', '1', '0', '0', ' ', ' ', 'c', ' ', 'f', 'B'],  
            ['0', '0', '1', '1', ' ', 'F', 'c', ' ', 'b']]
    fro4 = [['0', '0', '3', '0', 'F', 'f', 'f', 'b'],  
            ['0', '0', '1', '1', ' ', 'F', 'c', ' ', 'f', 'b'],  
            ['1', '1', '1', '0', ' ', ' ', 'c', ' ', 'f', 'F', 'b'],  
            ['1', '0', '1', '1', ' ', 'f', 'F', 'c', ' ', ' ', 'b'],  
            ['0', '2', '1', '0', ' ', 'c', ' ', 'c', ' ', 'F', 'b'],  
            ['0', '0', '1', '2', ' ', 'F', 'c', ' ', 'c', ' ', 'b'],  
            ['1', '0', '1', '1', ' ', 'f', 'C', ' ', ' ', 'f', 'b'],  
            ['1', '0', '1', '1', ' ', ' ', 'F', 'c', ' ', 'f', 'b']]
    fro5 = [['0', '0', '4', '0', 'F', 'f', 'f', 'f', 'b'],  
            ['1', '1', '1', '0', ' ', 'f', ' ', 'c', ' ', 'f', 'F', 'b'],  
            ['1', '1', '1', '0', ' ', 'f', 'c', ' ', 'f', 'F', 'b'],  
            ['2', '2', '0', '0', ' ', ' ', ' ', 'c', ' ', ' ', ' ', 'c', ' ', 'f', 'f', 'B'],  
            ['0', '2', '2', '0', ' ', 'c', ' ', 'c', ' ', 'F', 'f', 'b'],  
            ['1', '1', '1', '1', ' ', 'c', ' ', 'f', 'C', ' ', ' ', 'f', 'b'],  
            ['0', '0', '0', '4', ' ', ' ', 'C', ' ', ' ', 'c', ' ', ' ', 'c', ' ', ' ', 'c', ' ', ' ', 'b']]

    for r in range(11):
        for i in range(5):
            if lista[i] == 0:
                cores[i][0] = cores[i][1] = colors.grey
        print("    A   B   C   D   E   F   G   H   I   J" + cores[0][0] + "   ─────────────── %dx Submarinos ──────────────" %lista[0])
        print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + cores[0][1] + "                  [11] ■"  + colors.fim)
        for i in range(10):
            print("%d " %i + colors.d_blue + "║", end="")
            for j in range(10):
                if pf[i][j] == 'O':
                    print(colors.green + "▐█▌", end="")
                else:
                    print(colors.blue + "%s" %pf[i][j], end="")

                if j == 9:
                    print(colors.d_blue + "║", end="")
                else:
                    print(colors.d_blue + "│", end="")
            if i == 0:
                print(cores[1][0] + " ───────────── %dx Navios Comuns ─────────────" %lista[1])
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[1][1] + "               [21] ■   [22] ■ ■"  + colors.fim)
            elif i == 1:
                print(cores[1][1] + "                    ■")
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[2][0] + " ─────────── %dx Contratorpedeiros ───────────" %lista[2] + colors.fim)
            elif i == 2:
                print(cores[2][1] + "     [31] ■ ■ ■   [32] ■ ■        [33] ■")
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[2][1] + "                         ■             ■"  + colors.fim)
            elif i == 3:
                print(cores[2][1] + "     [34] ■    [35]  ■     [36] ■ ■    ■")
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[2][1] + "          ■ ■      ■ ■          ■"  + colors.fim)
            elif i == 4:
                print(cores[3][0] + " ───────────── %dx Navios-Tanque ─────────────" %lista[3])
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[3][1] + " [41] ■ ■ ■ ■  [42] ■ ■  [43]  ■   [44] ■ ■ ■"  + colors.fim)
            elif i == 5:
                print(cores[3][1] + "                    ■ ■      ■ ■ ■        ■")
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[3][1] + " [45] ■  [46] ■ ■"  + colors.fim)
            elif i == 6:
                print(cores[3][1] + "      ■       ■   [47] ■ ■    [48]  ■ ■")
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[3][1] + "      ■ ■     ■          ■ ■      ■ ■"  + colors.fim)
            elif i == 7:
                print(cores[4][0] + " ────────────── %dx Porta-Aviões ─────────────" %lista[4])
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[4][1] + " [51] ■ ■ ■ ■ ■  [52] ■   ■  [53] ■ ■     ■"  + colors.fim)
            elif i == 8:
                print(cores[4][1] + "                      ■ ■ ■       ■ ■ ■   ■")
                print(colors.d_blue + "  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + cores[4][1] + " [54]   ■  [55] ■             ■           ■"  + colors.fim)
            else:
                print(cores[4][1] + "        ■       ■        [56] ■ ■    [57] ■")
                print(colors.d_blue + "  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + cores[4][1] + "    ■ ■ ■       ■ ■ ■           ■ ■       ■"  + colors.fim)
        print()

        while True:
            print("Selecione qual unidade posicionar")
            while True:
                print("-> ", end="")
                es = input()
                if len(es) == 2:
                    if 49 <= ord(es[0]) <= 53 and 49 <= ord(es[1]) <= 56:
                        fe = int(es[0])
                        model = int(es[1])
                        if (fe == model == 1) or (fe == 2 and model <= 2) or (fe == 3 and model <= 6) or (fe == 4 and model <= 8) or (fe == 5 and model <= 7):
                            if lista[fe-1] == 0:
                                print("Você já utilizou todas as frotas desse tipo, escolha outra")
                            elif es in lista:
                                print("Você não possui mais este modelo para posicionar, escolha outro")
                            else:
                                lista[fe-1] -= 1
                                if es == '11' and lista[0] != 0:
                                    break
                                lista.append(es)
                                if fe == 1:
                                    fro = fro1
                                elif fe == 2:
                                    fro = fro2
                                elif fe == 3:
                                    fro = fro3
                                elif fe == 4:
                                    fro = fro4
                                else:
                                    fro = fro5
                                break
            
            print()
            print("    A   B   C   D   E   F   G   H   I   J")
            print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
            for i in range(10):
                print("%d " %i + colors.d_blue + "║", end="")
                for j in range(10):
                    if pf[i][j] == 'O':
                        print(colors.green + "▐█▌", end="")
                    else:
                        print(colors.blue + "%s" %pf[i][j], end="")

                    if j == 9:
                        print(colors.d_blue + "║", end="")
                        if i == 2:
                            print(colors.b_yellow + " Utilize o [■] como ponto de referência para", end="")
                        elif i == 3:
                            print(colors.b_yellow + "           ", end="")
                            
                        elif i == 4:
                            if fe == 2345:
                                sd
                        elif i == 5:
                            if fe == 345:
                                sd
                        elif i == 6:
                            if es == '57':
                                sd
                        elif i == 7:
                            if es == '57':
                                sd
                        print(colors.d_blue)
                    else:
                        print(colors.d_blue + "│", end="")
                if i == 9:
                    print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
                elif i == 2:
                    print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.b_yellow + "         posicionar a frota escolhida" + colors.fim)
                else:
                    print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
            print()

            '''
            ║           [ ]  [ ]  [ ]  [ ]  [ ]
            ╢           5 4  3 2   1
            ║                [ ]  [ ]  [ ]  [ ]
            ╢ 
            ║                     [ ]  [ ]  [ ]
            ╢ 
            ║                          [ ]  [ ]
            ╢ 
            ║                               [ ]

                        [21] ⌂   [22] ⌂ ■
                             ■

                [31] ⌂ ■ ■   [32] ■ ⌂        [33] ⌂
                                    ■             ■
                [34] ■    [35]  ■     [36] ⌂ ■    ■
                     ⌂ ■      ■ ⌂          ■

            [41] ⌂ ■ ■ ■  [42] ⌂ ■  [43]  ■   [44] ■ ⌂ ■
                               ■ ■      ■ ⌂ ■        ■
            [45] ■  [46] ⌂ ■
                 ■       ■   [47] ■ ⌂    [48]  ⌂ ■
                 ⌂ ■     ■          ■ ■      ■ ■

            [51] ⌂ ■ ■ ■ ■  [52] ■   ■  [53] ■ ■     ⌂
                                 ■ ⌂ ■       ■ ⌂ ■   ■
            [54]   ■  [55] ■             ■           ■
                   ■       ■        [56] ■ ⌂    [57] ■
               ■ ■ ⌂       ⌂ ■ ■           ■ ■       ■
            '''

            print("Informe as coordenadas que deseja posicionar: (letra primeiro, depois o número)")
            col, lin = Posicao(pf, fe, v)
            x = lin
            y = col
            c = fe
            print("    A   B   C   D   E   F   G   H   I   J")
            print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
            for i in range(10):
                print("%d " %i + colors.d_blue + "║", end="")
                for j in range(10):
                    if i == x and j == y:
                        print(colors.yellow + " ■ ", end="")
                        pf[i][j] = 'T'
                        c -= 1
                        if v == 0 and c != 0:
                            y += 1
                        elif v == 1 and c != 0:
                            x += 1
                    else:
                        if pf[i][j] == 'O':
                            print(colors.green + "▐█▌", end="")
                        else:
                            print(colors.blue + "%s" %pf[i][j], end="")
                    if j == 9:
                        print(colors.d_blue + "║")
                    else:
                        print(colors.d_blue + "│", end="")
                if i == 9:
                    print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
                else:
                    print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
            print()
            print("A posição escolhida esta correta?")
            print("   [1] Sim          [2] Não")
            if Escolha(2) == '1':
                for i in range(10):
                    for j in range(10):
                        if pf[i][j] == 'T':
                            pf[i][j] = 'O'
                break
            else:
                for i in range(10):
                    for j in range(10):
                        if pf[i][j] == 'T':
                            pf[i][j] = '░░░'

    for i in range(30):
        print()

def Posicao2(jg):
    while True:
        print("-> ", end="")
        p1 = input()
        if len(p1) == 2:
            if 65 <= ord(p1[0]) <= 74 and 48 <= ord(p1[1]) <= 57:
                col = ord(p1[0]) - 65
                lin = int(p1[1])
                if jg[lin][col] == '▒▒▒':
                    break
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            print("Insira a coordenada corretamente.")
    print()

    return col, lin

def Verifica(jg):
    for i in range(10):
        for j in range(10):
            if jg[i][j] == 'O':
                return 'C'
    return 'F'

def Jogar(f_jog, f_ini, jg_ini, v):
    print("    A   B   C   D   E   F   G   H   I   J")
    print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
    for i in range(10):
        print("%d " %i + colors.d_blue + "║", end="")
        for j in range(10):
            if jg_ini[i][j] == 'X':
                print(colors.RED + colors.b_yellow + "░" + colors.b_yellow + "▒" + colors.b_yellow + "░" + colors.fim, end="")
            elif jg_ini[i][j] == '.':
                print(colors.grey + "░░░", end="")
            else:
                print(colors.b_blue + "%s" %jg_ini[i][j], end="")
    
            if j == 9:
                print(colors.d_blue + "║")
            else:
                print(colors.d_blue + "│", end="")
        if i == 9:
            print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
        else:
            print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
    print()
    print("Escolha as coordenadas que deseja atacar: (letra primeiro, depois o número)")
    y, x = Posicao2(jg_ini)
    
    if f_ini[x][y] == 'O':
        jg_ini[x][y] = 'X'
        f_ini[x][y] = 'X'
    else:
        jg_ini[x][y] = '.'

    print("    A   B   C   D   E   F   G   H   I   J")
    print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
    for i in range(10):
        print("%d " %i + colors.d_blue + "║", end="")
        for j in range(10):
            if jg_ini[i][j] == 'X':
                print(colors.RED + colors.b_yellow + "░" + colors.b_yellow + "▒" + colors.b_yellow + "░" + colors.fim, end="")
            elif jg_ini[i][j] == '.':
                print(colors.grey + "░░░", end="")
            else:
                print(colors.b_blue + "%s" %jg_ini[i][j], end="")
    
            if j == 9:
                print(colors.d_blue + "║")
            else:
                print(colors.d_blue + "│", end="")
        if i == 9:
            print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
        else:
            print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
    print()
    
    if Verifica(f_ini) == 'C':
        if v == 1:
            v = 2
        else:
            v = 1
        print(colors.yellow + "VEZ DO JOGADOR %d" %v)
        print("Aperte Enter para continuar..." + colors.fim)
        cont = input()
    else:
        print(colors.green + "FIM DE JOGO!!")
        print("JOGADOR %d VENCEU!" %v + colors.fim)
        print()
        print("Deseja ver o mapa completo do jogador %d?" %v)
        print("     [1] Sim      [2] Não")
        if Escolha(2) == '1':
            print("    A   B   C   D   E   F   G   H   I   J")
            print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
            for i in range(10):
                print("%d " %i + colors.d_blue + "║", end="")
                for j in range(10):
                    if f_jog[i][j] == 'X':
                        print(colors.RED + colors.b_yellow + "░" + colors.b_yellow + "▒" + colors.b_yellow + "░" + colors.fim, end="")
                    elif f_jog[i][j] == '░░░':
                        print(colors.grey + "░░░", end="")
                    else:
                        print(colors.green + "▐█▌" %f_jog[i][j], end="")
            
                    if j == 9:
                        print(colors.d_blue + "║")
                    else:
                        print(colors.d_blue + "│", end="")
                if i == 9:
                    print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
                else:
                    print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
            print()
        v = 3

    return f_ini, jg_ini, v

def main():
    print("------ BATALHA NAVAL ------")
    print()
    while True:
        print("========= OPÇÕES =========")
        print("[1] Jogar   [2] Instruções")
        print("        [3] Sair")
        e = Escolha(3)
        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        elif e == '2':
            print("========== INSTRUÇÕES ==========")
            print()
            print("- Batalha Naval é um jogo onde ambos os jogadores deverão posicionar suas frotas navais em diferentes")
            print("  coordenadas, e após isso cada um deverá adivinhar onde o outro jogador posicionou sua frota. Ganha quem")
            print("  encontrar todas as frotas do outro jogador.")
            print("- Para começar, o jogador será apresentado a quantidade de unidades sua frota possui, juntamente também")
            print("  do tamanho que aquela unidade ocupará no mapa, sendo representado pelo símbolo (O), onde o número de")
            print("  'O's indica o tamanho que a unidade ocupa.")
            print("- Para posicionar sua frota é necessário fornecer as coordenadas em que sua unidade será posicionada, o")
            print("  posicionamento ocorre sempre da esquerda para a direita ou de cima para baixo, ou seja, caso você")
            print("  escolha uma unidade de tamanho 4 e escolha a coordenada 'B3' na vertical, isso significa que a unidade")
            print("  ocupará os espaços B3, B4, B5 e B6, e caso você escolha a coordenada 'B3' na horizontal, a unidade ocupará")
            print("  os espaços B3, C3, D3 e E3.")
            print()
        elif e == '1':
            f1 = []
            f2 = []
            jg1 = []
            jg2 = []
            for i in range(10):
                f1.append([])
                f2.append([])
                jg1.append([])
                jg2.append([])
                for j in range(10):
                    f1[i].append('░░░')
                    f2[i].append('░░░')
                    jg1[i].append('▒▒▒')
                    jg2[i].append('▒▒▒')
            print("Escolha o tipo de frota que desejam utilizar: ")
            print("[1] Frota Padrão       [2] Frota Avançada")
            frota = Escolha(2)

            print(colors.yellow + "JOGADOR 1 POSICIONE SUA FROTA")
            print("Aperte Enter para continuar..." + colors.fim)
            cont = input()
            if frota == '1':
                Posicionar(f1)
            else:
                Posicionar2(f1)
            print(colors.yellow + "JOGADOR 2 POSICIONE SUA FROTA")
            print("Aperte Enter para continuar..." + colors.fim)
            cont = input()
            if frota == '1':
                Posicionar(f2)
            else:
                Posicionar2(f2)

            print(colors.yellow + "PREPARATIVOS ENCERRADOS")
            print("JOGADOR 1 COMEÇA" + colors.fim)
            print()
            v = 1
            while True:
                if v == 1:
                    f2, jg2, v = Jogar(f1, f2, jg2, v)
                elif v == 2:
                    f1, jg1, v = Jogar(f2, f1, jg1, v)
                else:
                    break

            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()
