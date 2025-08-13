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
    GREEN = '\033[102m'
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

def Posicao(ji):
    while True:
        print("-> ", end="")
        p1 = input()
        p = []
        for i in range(len(p1)):
            p.append(p1[i])
        if len(p) == 2:
            if 65 <= ord(p[0]) <= 81 and 48 <= ord(p[1]) <= 56:
                col = p[0]
                p.remove(col)
                col = ord(col) - 65
                p1 = int(p[0])
                if ji[p1][col] == '|' or ji[p1][col] == '_':
                    break
                else:
                    print("A posição inserida não pode ser usada.")
            else:
                print("Insira uma posição dentro do intervalo.") 
        else:
            print("Insira a posição corretamente.")
    return col, p1

def ImprimeJogo(vj, p1, p2):
    print(colors.yellow + "               PLACAR")
    print(colors.red + "           %d" %p1 + colors.yellow + "     X" + colors.green + "     %d" %p2 + colors.fim)
    print("  A B C D E F G H I J K L M N O P Q")
    for i in range(9):
        print("%d " %i, end="")
        if i == 0:
            for j in range(17):
                if (j % 2) == 0:
                    print(" ", end="")
                else:
                    if vj[i][j] == 'g':
                        print(colors.green + "___" + colors.fim, end="")
                    elif vj[i][j] == 'r':
                        print(colors.red + "___" + colors.fim, end="")
                    else:
                        print(colors.grey + "___" + colors.fim, end="")
            print()
        else:
            for j in range(17):
                if (j % 2) == 0:
                    if vj[i][j] == 'G':
                        print(colors.green + "|" + colors.fim, end="")
                    elif vj[i][j] == 'R':
                        print(colors.red + "|" + colors.fim, end="")
                    else:
                        print(colors.grey + "|" + colors.fim, end="")
                else:
                    if vj[i][j] == 'g':
                        print(colors.green + "___" + colors.fim, end="")
                    elif vj[i][j] == 'r':
                        print(colors.red + "___" + colors.fim, end="")
                    elif vj[i][j] == 'pg':
                        print(colors.GREEN + "___" + colors.fim, end="")
                    elif vj[i][j] == 'pr':
                        print(colors.RED + "___" + colors.fim, end="")
                    else:
                        print(colors.grey + "___" + colors.fim, end="")
            print()
    print()

def Confirma(ji, x, y, p1, p2):
    print(colors.yellow + "               PLACAR")
    print(colors.red + "           %d" %p1 + colors.yellow + "     X" + colors.green + "     %d" %p2 + colors.fim)
    print("  A B C D E F G H I J K L M N O P Q")
    for i in range(9):
        print("%d " %i, end="")
        if i == 0:
            for j in range(17):
                if (j % 2) == 0:
                    print(" ", end="")
                else:
                    if ji[i][j] == 'g':
                        print(colors.green + "___" + colors.fim, end="")
                    elif ji[i][j] == 'r':
                        print(colors.red + "___" + colors.fim, end="")
                    else:
                        if i == x and j == y:
                            print(colors.yellow + "___" + colors.fim, end="")
                        else:
                            print(colors.grey + "___" + colors.fim, end="")
            print()
        else:
            for j in range(17):
                if (j % 2) == 0:
                    if ji[i][j] == 'G':
                        print(colors.green + "|" + colors.fim, end="")
                    elif ji[i][j] == 'R':
                        print(colors.red + "|" + colors.fim, end="")
                    else:
                        if i == x and j == y:
                            print(colors.yellow + "|" + colors.fim, end="")
                        else:
                            print(colors.grey + "|" + colors.fim, end="")
                else:
                    if ji[i][j] == 'g':
                        print(colors.green + "___" + colors.fim, end="")
                    elif ji[i][j] == 'r':
                        print(colors.red + "___" + colors.fim, end="")
                    elif ji[i][j] == 'pg':
                        print(colors.GREEN + "___" + colors.fim, end="")
                    elif ji[i][j] == 'pr':
                        print(colors.RED + "___" + colors.fim, end="")
                    else:
                        if i == x and j == y:
                            print(colors.yellow + "___" + colors.fim, end="")
                        else:
                            print(colors.grey + "___" + colors.fim, end="")
            print()
    print()
    print("A posição escolhida esta correta?")
    print("   [1] Sim          [2] Não")
    if Escolha(2) == '2':
        return 'E'
    return 'C'

def Verifica(ji, x, y, v, p1, p2):
    r = 0
    p = 0
    if ji[x][y] == '|':
        if y > 0:
            if ji[x][y-1] != '_' and ji[x][y-2] != '|' and ji[x-1][y-1] != '_':
                if v == 1:
                    ji[x][y-1] = 'pr'
                    p1 += 1
                    r = 1
                else:
                    ji[x][y-1] = 'pg'
                    p2 += 1
                    r = 2
        if y < 16:
            if ji[x][y+1] != '_' and ji[x][y+2] != '|' and ji[x-1][y+1] != '_':
                if v == 1:
                    ji[x][y+1] = 'pr'
                    p1 += 1
                    r = 1
                else:
                    ji[x][y+1] = 'pg'
                    p2 += 1
                    r = 2
        if v == 1:
            ji[x][y] = 'R'
        else:
            ji[x][y] = 'G'
    else:
        if x < 8:
            if ji[x+1][y+1] != '|' and ji[x+1][y-1] != '|' and ji[x+1][y] != '_':
                if v == 1:
                    ji[x+1][y] = 'pr'
                    p1 += 1
                    r = 1
                else:
                    ji[x+1][y] = 'pg'
                    p2 += 1
                    r = 2
            if v == 1:
                ji[x][y] = 'r'
            else:
                ji[x][y] = 'g'
        if x > 0:
            if ji[x][y-1] != '|' and ji[x][y+1] != '|' and ji[x-1][y] != '_':
                if v == 1:
                    ji[x][y] = 'pr'
                    p1 += 1
                    r = 1
                else:
                    ji[x][y] = 'pg'
                    p2 += 1
                    r = 2
            else:
                if v == 1:
                    ji[x][y] = 'r'
                else:
                    ji[x][y] = 'g'

    for i in range(9):
        for j in range(17):
            if ji[i][j] == '|' or ji[i][j] == '_':
                p = 1
                break
        if p == 1:
            break

    if p == 0:
        r = 3
    return r, p1, p2

def main():
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
        elif e == '2':
            print("========== INSTRUÇÕES ==========")
            print()
            print("- No Jogo das Linhas, será fornecido aos jogadores um pequena tabela 8x8 com pequenos quadrados dentro.")
            print("  A cada turno, os jogadores deverão pintar as linhas da tabela com o objetivo de formar um quadrado pintado,")
            print("  isto é, um quadrado com todos os lados pintados.")
            print("- Caso durante o turno de um jogador, ele complete um quadrado ao pintar a última linha, ele ganhará um ponto")
            print("  e poderá jogar novamente no próximo turno. Ganha, aquele jogador que tiver mais pontos no final, ou em outras")
            print("  palavras, aquele que conseguir preencher mais quadrados até o fim do jogo.")
            print("- O jogo não irá se encerrar até que todas as linhas da tabela sejam pintadas.")
            print("- Para preencher um quadrado, basta que todas as 4 linhas ao seu redor estejam pintadas. A cor em que as linhas")
            print("  estão pintadas não importa, o jogador 2 (verde) pode forma um quadrado mesmo que as outras 3 linhas já estejam")
            print("  pintadas pelo jogador 1 (vermelho), o importante é que durante o seu turno, ele consiga pintar a última linha")
            print("  restante para completar o quadrado, é isso que determina de quem será o quadrado no final.")
            print()
        elif e == '1':
            ji = []
            for i in range(9):
                ji.append([])
                if i == 0:
                    for j in range(17):
                        if (j % 2) == 0:
                            ji[i].append(' ')
                        else:
                            ji[i].append('_')
                else:
                    for j in range(17):
                        if (j % 2) == 0:
                            ji[i].append('|')
                        else:
                            ji[i].append('_')
            print(colors.red + "O JOGADOR 1 COMEÇA" + colors.fim)
            print()
            v = 1
            p1 = 0
            p2 = 0
            ImprimeJogo(ji, p1, p2)
            while True:
                while True:
                    print("Insira a posição que deseja jogar: (letra primeiro, depois o número)")
                    y, x = Posicao(ji)
                    print()
                    c = Confirma(ji, x, y, p1, p2)
                    if c == 'C':
                        break
                r, p1, p2 = Verifica(ji, x, y, v, p1, p2)
                ImprimeJogo(ji, p1, p2)
                if r == 3:
                    print(colors.yellow + "FIM DE JOGO!!" + colors.fim)
                    if p1 > p2:
                        print(colors.red + "O JOGADOR 1 GANHOU!" + colors.fim)
                    elif p2 > p1:
                        print(colors.green + "O JOGADOR 2 GANHOU!" + colors.fim)
                    else:
                        print("EMPATE!!")
                    print()
                    break
                elif r == 2:
                    print(colors.green + "JOGADOR 2 JOGA NOVAMENTE" + colors.fim)
                    print()
                elif r == 1:
                    print(colors.red + "JOGADOR 1 JOGA NOVAMENTE" + colors.fim)
                    print()
                else:
                    if v == 1:
                        v = 2
                        print(colors.green + "VEZ DO JOGADOR 2" + colors.fim)
                    else:
                        v = 1
                        print(colors.red + "VEZ DO JOGADOR 1" + colors.fim)

        print("[1] Jogar Novamente   [2] Sair")
        e2 = Escolha(2)
        if e2 == '2':
            print("ENCERRANDO JOGO...")
            break
        elif e2 == '1':
            print("INICIANDO NOVO JOGO...")
            print()

main()
