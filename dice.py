import random

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
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

def main():
    print("------------- ROLL DICE -------------")
    print()
    while True:
        print(colors.yellow + "============== OPÇÕES ==============" + colors.fim)
        print("[1] Rolar um Dado     [2] Instruções")
        print("             [3] Sair")
        e = 0
        while '1' != e != '2' and '3' != e:
            print("-> ", end="")
            e = input()
        print()
        if e == '3':
            print("ENCERRANDO PROGRAMA...")
            break
        elif e == '2':
                print(colors.yellow + "========== INSTRUÇÕES ==========" + colors.fim)
                print()
                print("Para rolar um dado, qualquer que seja, sempre escreva no seguinte formato:")
                print(colors.blue + "                          <num_dado>" + colors.yellow + "D" + colors.blue + "<num_lados>" + colors.fim)
                print("Onde " + colors.blue + "<num_dados>" + colors.fim + " representa a quantidade de dados que deseja rolar;")
                print("E " + colors.blue + "<num_lados>" + colors.fim + " a quantidade de lados que o dado possui, por exemplo, se o valor")
                print("for " + colors.green + "2D6" + colors.fim + " então serão rolados " + colors.green + "2" + colors.fim + " dados de " + colors.green + "6" + colors.fim + " lados.")
                print()
        elif e == '1':
            while True:
                print("Informe o tipo de dado que deseja rolar: ")
                while True:
                    s = 0
                    print("-> ", end="")
                    d = input().split('D')
                    if len(d) == 2:
                        for i in range(2):
                            p = 0
                            for j in d[i]:
                                if 48 <= ord(j) <= 57:
                                    p += 1
                            if p != len(d[i]) or p == 0:
                                print("Por favor, escreva na formatação correta")
                                break
                            else:
                                d[i] = int(d[i])
                                if d[i] >= 1000 or d[i] == 0:
                                    print("Por favor, escreva um valor menor que 1000 e maior que 0")
                                    break
                                else:
                                    s += 1        
                    else:
                        print("Por favor, escreva na formatação correta")
                    if s == 2:
                        print()
                        break
                q = d[0]
                l = d[1]
                t = 0
                c = 1
                print("Resultado:")
                r = random.randint(1, l)
                if r == 1 or r == l:
                    if r == 1:
                        print(colors.red, end="")
                    else:
                        print(colors.green, end="")
                    print("%d" %r, end="")
                    print(colors.fim, end="")
                else:
                    print("%d" %r, end="")
                t += r
                for i in range(q-1):
                    r = random.randint(1, l)
                    t += r
                    if i >= (19 * c):
                        c += 1
                        print(",")
                    else:
                        print(", ", end="")
                    if r == 1 or r == l:
                        if r == 1:
                            print(colors.red, end="")
                        else:
                            print(colors.green, end="")
                        print("%d" %r, end="")
                        print(colors.fim, end="")
                    else:
                        print("%d" %r, end="")
                print()
                print("TOTAL: %d" %t)
                print()
                print("[1] Continuar   [2] Sair")
                e = 0
                if Escolha(2) == '2':
                    print("ENCERRANDO PROGRAMA...")
                    break
            break
    
main()
