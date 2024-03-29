#include <stdio.h>
#include <string.h>

char Verifica(char j[9]){
    int i, c = 0;
    int v[8][3] = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}};
    char p1, p2, p3, m[9];


    for (i = 0; i < 9; i++){
        m[i] = j[i];
        if (m[i] != 'X' && m[i] != 'O'){
            m[i] = '*';
        }
    }

    for (i = 0; i < 8; i++){
        p1 = m[v[i][0]];
        p2 = m[v[i][1]];
        p3 = m[v[i][2]];

        if (p1 == '*' || p2 == '*' || p3 == '*'){
            c = 1;
            continue;
        }else if (p1 == p2 && p2 == p3){
            return p1;
        }
    }
    if (c == 1){
        return 'C';
    }else{
        return 'E';
    }
}

int main() {
    int i, j, p, p1, f = 0, f2;
    char e, e2, v, r, m[9];

    printf("JOGO DA VELHA\n");
    printf("\n");
    while (f == 0){
        char mi[9] = {'0', '1', '2', '3', '4', '5', '6', '7', '8'};
        p = 0;
        for (i = 0; i < 3; i++) {
            printf("    ");
            for (j = 0; j < 3; j++) {
                m[p] = '*';
                printf("%c ", m[p]);
                p++;
            }
            printf("\n");
        }
        printf("\n");

        e = '/';
        while (e != 's' && e != 'n'){
            printf("Começar jogo? (s/n):\n");
            printf("-> ");
            scanf("%s", &e);
            printf("\n");
        }
        if (e == 'n'){
            printf("ENCERRANDO JOGO...\n");
            f = 1;
        }else{
            printf("O jogador X começa.\n");
            v = 'X';
            f2 = 0;
            while (f2 == 0){
                printf("Insira a posição que deseja jogar:\n");
                p = 0;
                for (i = 0; i < 3; i++) {
                    printf("    ");
                    for (j = 0; j < 3; j++) {
                        printf("%c ", mi[p]);
                        p++;
                    }
                    printf("\n");
                }
                while(1){
                    printf("-> ");
                    scanf("%d", &p1);
                    if (p1 < 0 || p1 > 8){
                        printf("Valores inválidos, insira outro valor.\n");
                    }else if(m[p1] == 'X' || m[p1] == 'O'){
                        printf("A posição inserida ja está ocupada, insira outro valor.\n");
                    }else{
                        printf("\n");
                        break;
                    }
                }
                p = 0;
                for (i = 0; i < 3; i++) {
                    printf("    ");
                    for (j = 0; j < 3; j++) {
                        if (p == p1){
                            m[p] = v;
                        }
                        printf("%c ", m[p]);
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
                    f2 = 1;
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
    return 0;
}
