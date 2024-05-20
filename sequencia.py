import random

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

def CriaSequencia():
    l = []
    for i in range(4):
        while True:
            x = random.randint(0, 9)
            if x not in l:
                l.append(x)
                break
    return l

def VerificaSequencia(s, l):
    c = 0
    r = 0
    p = 0
    for i in l:
        if i in s:
            c = c + 1
            if s[p] != l[p]:
                r = r + 1
        p = p + 1
    return c, r

def main():
    print("------- JOGO DA SEQUÊNCIA -------")
    print()
    while True:
        print("============ OPÇÕES ============")
        print("[1] Jogar        [3] Como jogar?")
        print("[2] Instruções   [4] Sair")
        e = 0
        while '1' != e != '2' and '3' != e != '4':
            print("-> ", end="")
            e = input()
        print()
        if e == '4':
            print("ENCERRANDO JOGO...")
            break
        elif e == '3':
            print("========== COMO JOGAR ==========")
            print()
            print("No jogo da sequência, o código irá gerar uma lista de 4 valores aleatórios, o")
            print("objetivo do jogador é adivinhar a sequência correta de números gerados.")
            print("Para isso, a cada tentativa o jogador irá fornecer 4 números que ele acredita")
            print("ser a sequência correta gerada pelo computador.")
            print("Ao final de cada tentativa, o programa irá informar ao jogador caso ele tenha")
            print("acertado algum número e se algum deles estava na posição errada.")
            print("Esse processo irá se repetir até que o jogador acerte todos os valores da sequência")
            print("na ordem correta.")
            print()
        elif e == '2':
            print("========== INSTRUÇÕES ==========")
            print()
            print("- Os valores de uma sequência sempre irão variar de 0 até 9;")
            print("- Um número nunca aparecerá mais de uma vez na mesma sequência;")
            print("- Quando for adivinhar uma sequência, sempre escreva os números separados por um")
            print("  espaço, isto é, invés de escrever '1234' escreva '1 2 3 4'.")
            print()
        elif e == '1':
            s = []
            s = CriaSequencia()
            t = 1
            while True:
                print("TENTATIVA Nº%d" %t)
                print()
                while True:
                    print("Insira a sequência: ", end="")
                    s1 = input().split()
                    e2 = 0
                    for i in s1:
                        if len(i) == 1 and 48 <= ord(i) <= 57:
                            e2 = 1
                        else:
                            e2 = 0
                            break
                    if e2 == 1:
                        if len(s1) == 4:
                            for i in range(4):
                                s1[i] = int(s1[i])
                            break
                        else:
                            print("Por favor insira a quantidade correta de números.")
                    else:
                        print("Entrada inválida")
                        print()
                c, p = VerificaSequencia(s, s1)
                print()
                print("Números acertados: %d" %c)
                print("Números fora de ordem: %d" %p)
                print()
                if c == 4 and p == 0:
                    print("FIM DE JOGO!")
                    print("Sequência correta: ", end="")
                    for i in range(4):
                        print("%d " %s1[i], end="")
                    print()
                    print("Tentativas necessárias: %d" %t)
                    print()
                    break
                else:
                    t = t + 1
            print("[1] Continuar   [2] Sair")
            e = 0
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            
main()
