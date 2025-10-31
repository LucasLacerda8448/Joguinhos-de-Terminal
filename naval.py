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
    tam = 6 - f  #MUDAR A ORDEM DAS FROTAS DE DECRESCENTE PARA CRESCENTE, OU SEJA, [1] Tam 1; [2] Tam 2; etc
    while True:
        print("-> ", end="")
        p1 = input()
        p = []
        for i in range(len(p1)):
            p.append(p1[i])
        if len(p) == 2:
            if 65 <= ord(p[0]) <= 74 and 48 <= ord(p[1]) <= 57:
                col = ord(p[0]) - 65
                lin = int(p[1])
                if jg[lin][col] == '░░░':
                    reg = lin + 1
                    reg2 = col + 1
                    if f == 1:  #CONTINUAR DAQUI ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        if v == 0:
                            if (reg2 + 3) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(4):
                                    if jg[lin][reg2] == '░░░':
                                        reg2 += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg2 - col) == 5:
                                break
                        else:
                            if (reg + 3) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(4):
                                    if jg[reg][col] == '░░░':
                                        reg += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg - lin) == 5:
                                break 
                    elif f == 2:
                        if v == 0:
                            if (reg2 + 2) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(3):
                                    if jg[lin][reg2] == '░░░':
                                        reg2 += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg2 - col) == 4:
                                break
                        else:
                            if (reg + 2) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(3):
                                    if jg[reg][col] == '░░░':
                                        reg += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg - lin) == 4:
                                break 
                    elif f == 3:
                        if v == 0:
                            if (reg2 + 1) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(2):
                                    if jg[lin][reg2] == '░░░':
                                        reg2 += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg2 - col) == 3:
                                break
                        else:
                            if (reg + 1) > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                for i in range(2):
                                    if jg[reg][col] == '░░░':
                                        reg += 1
                                    else:
                                        print("A unidade escolhida não cabe no espaço escolhido.")
                                        break
                            if (reg - lin) == 3:
                                break  
                    elif f == 4:
                        if v == 0:
                            if reg2 > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                if jg[lin][reg2] == '░░░':
                                    break
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                        else:
                            if reg > 9:
                                print("A unidade escolhida não cabe no espaço escolhido.")
                            else:
                                if jg[reg][col] == '░░░':
                                    break
                                else:
                                    print("A unidade escolhida não cabe no espaço escolhido.")
                    else:
                        break
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            print("Insira a coordenada corretamente.")

    return col, lin

def Posicionar(pf):
    lista = [1, 1, 2, 3, 4]
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
                    print(colors.d_blue + "║")
                else:
                    print(colors.d_blue + "│", end="")
            if i == 9:
                print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
            else:
                print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
        print()
        print("Frota:")
        if lista[0] == 0:
            print(colors.grey + "[1] %dx Porta-avião (O O O O O)" %lista[0], end="")
        else:
            print("[1] %dx Porta-avião (O O O O O)" %lista[0], end="")
        if lista[3] == 0:
            print(colors.grey + "    [4] %dx Navios Comuns (O O)" %lista[3] + colors.fim) 
        else:
            print(colors.fim + "    [4] %dx Navios Comuns (O O)" %lista[3])

        if lista[1] == 0:
            print(colors.grey + "[2] %dx Navio-tanque (O O O O)" %lista[1], end="")
        else:
            print("[2] %dx Navio-tanque (O O O O)" %lista[1], end="")
        if lista[4] == 0:
            print(colors.grey + "     [5] %dx Submarinos (O)" %lista[4] + colors.fim) 
        else:
            print(colors.fim + "     [5] %dx Submarinos (O)" %lista[4]) 

        if lista[2] == 0:
            print(colors.grey + "[3] %dx Contratorpedeiros (O O O)" %lista[2] + colors.fim)
        else:
            print("[3] %dx Contratorpedeiros (O O O)" %lista[2])
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
            c = 6 - fe
            print("    A   B   C   D   E   F   G   H   I   J")
            print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
            for i in range(10):
                print("%d " %i + colors.d_blue + "║", end="")
                for j in range(10):
                    if i == x and j == y:
                        print(colors.yellow + "▐█▌", end="")
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
                c = 6 - fe
                for i in range(10):
                    for j in range(10):
                        if i == lin and j == col:
                            pf[lin][col] = 'O'
                            c -= 1
                            if v == 0 and c != 0:
                                col += 1
                            elif v == 1 and c != 0:
                                lin += 1
                break
    for i in range(20):
        print()

def Posicionar2(pf):
    lista = [1, 2, 2, 2, 4]
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
                    print(colors.d_blue + "║")
                else:
                    print(colors.d_blue + "│", end="")
            if i == 9:
                print("  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝" + colors.fim)
            else:
                print("  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢" + colors.fim)
        print()
        print("Frota:")
        if lista[0] == 0:
            print(colors.grey + "[1] %dx Porta-avião (O O O O O)" %lista[0], end="")
        else:
            print("[1] %dx Porta-avião (O O O O O)" %lista[0], end="")
        if lista[3] == 0:
            print(colors.grey + "    [4] %dx Navios Comuns (O O)" %lista[3] + colors.fim) 
        else:
            print(colors.fim + "    [4] %dx Navios Comuns (O O)" %lista[3])

        if lista[1] == 0:
            print(colors.grey + "[2] %dx Navio-tanque (O O O O)" %lista[1], end="")
        else:
            print("[2] %dx Navio-tanque (O O O O)" %lista[1], end="")
        if lista[4] == 0:
            print(colors.grey + "     [5] %dx Submarinos (O)" %lista[4] + colors.fim) 
        else:
            print(colors.fim + "     [5] %dx Submarinos (O)" %lista[4]) 

        if lista[2] == 0:
            print(colors.grey + "[3] %dx Contratorpedeiros (O O O)" %lista[2] + colors.fim)
        else:
            print("[3] %dx Contratorpedeiros (O O O)" %lista[2])
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
            c = 6 - fe
            print("    A   B   C   D   E   F   G   H   I   J")
            print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
            for i in range(10):
                print("%d " %i + colors.d_blue + "║", end="")
                for j in range(10):
                    if i == x and j == y:
                        print(colors.yellow + "▐█▌", end="")
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
                c = 6 - fe
                for i in range(10):
                    for j in range(10):
                        if i == lin and j == col:
                            pf[lin][col] = 'O'
                            c -= 1
                            if v == 0 and c != 0:
                                col += 1
                            elif v == 1 and c != 0:
                                lin += 1
                break
    for i in range(20):
        print()

def Posicao2(jg):
    while True:
        print("-> ", end="")
        p1 = input()
        p = []
        for i in range(len(p1)):
            p.append(p1[i])
        if len(p) == 2:
            if 65 <= ord(p[0]) <= 74 and 48 <= ord(p[1]) <= 57:
                col = p[0]
                p.remove(col)
                col = ord(col) - 65
                p1 = int(p[0])
                if jg[p1][col] == '#':
                    break
                else:
                    print("A coordenada inserida não pode ser usada.")
            else:
                print("Insira uma coordenada dentro do intervalo.") 
        else:
            print("Insira a coordenada corretamente.")
    print()
    return col, p1

def Verifica(jg):
    r = 0
    for i in range(10):
        for j in range(10):
            if jg[i][j] == 'O':
                r = 1
                break
        if r == 1:
            break
    if r == 1:
        return 'C'
    return 'F'


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
                    print("    A   B   C   D   E   F   G   H   I   J")
                    print(colors.d_blue + "  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗" + colors.fim)
                    for i in range(10):
                        print("%d " %i + colors.d_blue + "║", end="")
                        for j in range(10):
                            if jg2[i][j] == 'X':
                                print(colors.RED + colors.b_yellow + "░" + colors.b_yellow + "▒" + colors.b_yellow + "░" + colors.fim, end="")
                            elif jg2[i][j] == '.':
                                print(colors.grey + "░░░", end="")
                            else:
                                print(colors.b_blue + "%s" %jg2[i][j], end="")
                            
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
                    y, x = Posicao2(jg2)

                    if f2[x][y] == 'O':
                        jg2[x][y] = 'X'
                        f2[x][y] = 'X'
                    else:
                        jg2[x][y] = '.'

                    print("  A B C D E F G H I J")
                    for i in range(10):
                        print("%d " %i, end="")
                        for j in range(10):
                            if jg2[i][j] == 'X':
                                print(colors.red + "X " + colors.fim, end="")
                            elif jg2[i][j] == '.':
                                print(colors.grey + ". " + colors.fim, end="")
                            else:
                                print(colors.blue + "%s " %jg2[i][j] + colors.fim, end="")
                        print()
                    print()


                    if Verifica(f2) == 'C':
                        v = 2
                        print(colors.yellow + "VEZ DO JOGADOR 2")
                        print("Aperte Enter para continuar..." + colors.fim)
                        cont = input()
                    else:
                        print(colors.green + "FIM DE JOGO!!")
                        print("JOGADOR 1 VENCEU!" + colors.fim)
                        print()
                        print("Deseja ver o mapa completo do jogador 1?")
                        print("     [1] Sim      [2] Não")
                        if Escolha(2) == '1':
                            print("  A B C D E F G H I J")
                            for i in range(10):
                                print("%d " %i, end="")
                                for j in range(10):
                                    if f1[i][j] == 'X':
                                        print(colors.red + "X " + colors.fim, end="")
                                    elif f1[i][j] == '*':
                                        print(colors.grey + ". " + colors.fim, end="")
                                    else:
                                        print(colors.green + "%s " %f1[i][j] + colors.fim, end="")
                                print()
                            print()
                        break

                elif v == 2:
                    print("  A B C D E F G H I J")
                    for i in range(10):
                        print("%d " %i, end="")
                        for j in range(10):
                            if jg1[i][j] == 'X':
                                print(colors.red + "X " + colors.fim, end="")
                            elif jg1[i][j] == '.':
                                print(colors.grey + ". " + colors.fim, end="")
                            else:
                                print(colors.blue + "%s " %jg1[i][j] + colors.fim, end="")
                        print()
                    print()
                    print("Escolha as coordenadas que deseja atacar: (letra primeiro, depois o número)")
                    y, x = Posicao2(jg1)

                    if f1[x][y] == 'O':
                        jg1[x][y] = 'X'
                        f1[x][y] = 'X'
                    else:
                        jg1[x][y] = '.'

                    print("  A B C D E F G H I J")
                    for i in range(10):
                        print("%d " %i, end="")
                        for j in range(10):
                            if jg1[i][j] == 'X':
                                print(colors.red + "X " + colors.fim, end="")
                            elif jg1[i][j] == '.':
                                print(colors.grey + ". " + colors.fim, end="")
                            else:
                                print(colors.blue + "%s " %jg1[i][j] + colors.fim, end="")
                        print()
                    print()

                    if Verifica(f1) == 'C':
                        v = 1
                        print(colors.yellow + "VEZ DO JOGADOR 1")
                        print("Aperte Enter para continuar..." + colors.fim)
                        cont = input()
                    else:
                        print(colors.green + "FIM DE JOGO!!")
                        print("JOGADOR 2 VENCEU!" + colors.fim)
                        print()
                        print("Deseja ver o mapa completo do jogador 2?")
                        print("     [1] Sim      [2] Não")
                        if Escolha(2) == '1':
                            print("  A B C D E F G H I J")
                            for i in range(10):
                                print("%d " %i, end="")
                                for j in range(10):
                                    if f2[i][j] == 'X':
                                        print(colors.red + "X " + colors.fim, end="")
                                    elif f2[i][j] == '*':
                                        print(colors.grey + ". " + colors.fim, end="")
                                    else:
                                        print(colors.green + "%s " %f2[i][j] + colors.fim, end="")
                                print()
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

'''
1 bloco: ▐█▌
4x
▐█▌

2x
▐█▌   ▐█▌▐█▌
▐█▌  

2x
▐█▌     ▐█▌▐█▌▐█▌
▐█▌
▐█▌   ▐█▌          ▐█▌    ▐█▌▐█▌    ▐█▌▐█▌
      ▐█▌▐█▌    ▐█▌▐█▌    ▐█▌          ▐█▌

2x
▐█▌▐█▌▐█▌▐█▌    ▐█▌▐█▌  ▐█▌▐█▌▐█▌       ▐█▌
                ▐█▌▐█▌     ▐█▌       ▐█▌▐█▌▐█▌
▐█▌▐█▌   ▐█▌
▐█▌      ▐█▌      ▐█▌▐█▌          ▐█▌▐█▌
▐█▌      ▐█▌▐█▌      ▐█▌▐█▌    ▐█▌▐█▌

1x
▐█▌   ▐█▌▐█▌▐█▌▐█▌▐█▌   ▐█▌   ▐█▌
▐█▌                     ▐█▌▐█▌▐█▌
▐█▌  ▐█▌         ▐█▌                ▐█▌
▐█▌  ▐█▌▐█▌      ▐█▌                ▐█▌   ▐█▌▐█▌
▐█▌     ▐█▌▐█▌   ▐█▌▐█▌▐█▌    ▐█▌▐█▌▐█▌   ▐█▌▐█▌▐█▌

    A   B   C   D   E   F   G   H   I   J
  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗
0 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
1 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
2 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
3 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
4 ║▒▒▒│░░░│   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
5 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
6 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
7 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
8 ║   │   │   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───┼───┼───╢
9 ║   │   │   │   │   │   │   │   │   │   ║
  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝

  print(colors.RED + colors.b_yellow + "░" + colors.b_yellow + "▒" + colors.b_yellow + "░" + colors.fim, end="")
'''
