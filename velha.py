def Verifica(j):
    c = 0
    v = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    m = []
    for i in range(9):
        m[i] = j[i]
        if m[i] != 'X' and m[i] != 'O':
            m[i] = '*'

    for i in range(8):
        p1 = m[v[i][0]]
        p2 = m[v[i][1]]
        p3 = m[v[i][2]]

        if p1 == '*' or p2 == '*' or p3 == '*':
            c = 1
            continue
        elif p1 == p2 == p3:
            return p1

    if c == 1:
        return 'C'
    else:
        return 'E'

def main():
    print("JOGO DA VELHA")
    print()
    while True:
        m = []
        mi = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        p = 0
        for i in range(3):
            print("    ", end="")
            for j in range(3):
                m.append('*')
                print("%s ", m[p])
                p = p + 1
            print()
        print()

        e = '/'
        while e != 's' and e != 'n':
            print("Começar jogo? (s/n):")
            print("-> ", end="")
            e = input()
            print()

        if e == 'n':
            print("ENCERRANDO JOGO...")
            break
        else:
            print("O jogador X começa.")
            v = 'X'
            while True:
                print("Insira a posição que deseja jogar:")
                p = 0
                for i in range (3):
                    print("    ")
                    for j in range(3):
                        print("%s ", mi[p])
                        p = p + 1
                    print()
                while True:
                    print("-> ", end="")
                    p1 = int(input())
                    if p1 < 0 or p1 > 8:
                        print("Valores inválidos, insira outro valor.")
                    elif m[p1] == 'X' or m[p1] == 'O':
                        print("A posição inserida ja está ocupada, insira outro valor.")
                    else:
                        print()
                        break

                p = 0
                for i in range(3):
                    print("    ", end="")
                    for j in range(3):
                        if p == p1:
                            m[p] = v
                        print("%s ", m[p])
                        p++;
                    }
                    printf("\n");
                }
                printf("\n");
                r = Verifica(m);
                if (r == 'C'){
                    if (v == 'X'){
                        v = 'O';
                    }else{
                        v = 'X';
                    }
                    printf("Vez do jogador %c.\n", v);
                }else{
                    printf("FIM DE JOGO!\n");
                    if (r == 'X' || r == 'O'){
                        printf("Jogador %c Venceu.\n", r);
                    }else if (r == 'E'){
                        printf("Empate.\n");
                    }
                    printf("\n");
                    break
                }
            }
            e2 = '/';
            while (e2 != 's' && e2 != 'n'){
                printf("Jogar novamente? (s/n):\n");
                printf("-> ");
                scanf("%s", &e2);
                printf("\n");
            }
            if (e2 == 'n'){
                printf("ENCERRANDO JOGO...\n");
                f = 1;
            }else{
                printf("INICIANDO NOVO JOGO...\n");
                printf("\n");
            }
        }
    }

main()
