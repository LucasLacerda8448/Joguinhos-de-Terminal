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

'''

def Posicionar2(pf):
    lista = [4, 2, 2, 2, 1]
    lista_model = [[1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1]]
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
                            print(colors.grey + " [2] %dx Navios Comuns" %lista[1] + colors.d_blue)
                        else:
                            print(colors.fim + " [2] %dx Navios Comuns" %lista[1] + colors.d_blue)
                    elif i == 5:
                        if lista[3] == 0:
                            print(colors.grey + " [4] %dx Navio-tanque" %lista[3] + colors.d_blue) 
                        else:
                            print(colors.fim + " [4] %dx Navio-tanque" %lista[3] + colors.d_blue)
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
                        print(colors.grey + " [1] %dx Submarinos" %lista[0] + colors.fim)
                    else:
                        print(" [1] %dx Submarinos" %lista[0])
                elif i == 4:
                    if lista[2] == 0:
                        print(colors.grey + " [3] %dx Contratorpedeiros" %lista[2] + colors.fim)
                    else:
                        print(" [3] %dx Contratorpedeiros" %lista[2])
                elif i == 5:
                    if lista[4] == 0:
                        print(colors.grey + " [5] %dx Porta-avião" %lista[4] + colors.fim) 
                    else:
                        print(" [5] %dx Porta-avião" %lista[4])
                else:
                    print()
                
        print()
        while True:
            print("Selecione qual unidade posicionar")
            while True:
                fe = int(Escolha(5))
                if lista[fe-1] == 0:
                    print("Você não possui mais esta unidade para posicionar, escolha outra")
                else:
                    lista[fe-1] -= 1
                    break
            
            if fe != 1:
                print("Frota de Tamanho %d:" %fe)
                if fe == 2:
                    if lista_model[0][0] == 0:
                        print(colors.grey + "[1] ■ ■" + colors.fim, end="")
                    else:
                        print("[1] ■ ■", end="")
                    if lista_model[0][1] == 0:
                        print(colors.grey + "   [2] ■")
                        print("              ■" + colors.fim)
                    else:
                        print("   [2] ■")
                        print("              ■")
                    tam = 2
                elif fe == 3:
                    if lista_model[1][0] == 0:
                        print(colors.grey + "[1] ■ ■ ■" + colors.fim, end="")
                    else:
                        print("[1] ■ ■ ■", end="")
                    #CONTINUAR DAQUI    
                    print("    [2] ■ ■""         [3] ■")
                    print("                   ■             ■")
                    print("[4] ■     [5]  ■      [6] ■ ■    ■")
                    print("    ■ ■      ■ ■          ■")
                    tam = 6
                elif fe == 4:
                    tam = 8
                elif fe == 5:
                    tam = 7
                print("Escolha qual modelo deseja utilizar." %fe)
                while True:
                    tam = int(Escolha(tam))
                    if lista_model[fe-2][tam-1] == 0:
                        print("Você não possui mais este modelo para posicionar, escolha outro")
                    else:
                        lista_model[fe-2][tam-1] -= 1
                        model = str(fe) + str(tam)
                        break
            else:
                model = str(fe) + 0    
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
