#include <stdio.h>
#include <string.h>
#define c 3
#define l 3

int main() {
  int i, j, p1, p2, f = 0, f2 = 0;
  char m[c][l], e, v;

  printf("JOGO DA VELHA\n");
  printf("\n");
  while (f == 0){
    for (i = 0; i < 3; i++) {
        printf("    ");
        for (j = 0; j < 3; j++) {
            m[i][j] = '*';
            printf("%c ", m[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    while (e != 's' && e != 'n'){
        printf("Começar? (s/n):\n");
        printf("-> ");
        scanf("%s", &e);
        printf("\n");
    }
    if (e == 'n'){
        printf("ENCERRANDO JOGO...\n");
        f = 1;
    }else{
        printf("O jogador X começa.\n");
        printf("Insira a posição que deseja jogar:\n");
        printf("(As posições vão de [0,0] até [2,2])\n");
        v = 'X';
        while (f2 == 0){
            while(1){
                printf("%c\n", m[0][0]);
                printf("-> ");
                scanf("%d %d", &p1, &p2);
                if (p1 > 2 || p2 > 2){
                    printf("Valores inválidos, insira outro valor.\n");
                }else if(m[p1][p2] != '*'){
                    printf("A posição inserida ja está ocupada, insira outro valor.\n");
                }else{
                    printf("\n");
                    break;
                }
            }
            for (i = 0; i < 3; i++) {
                printf("    ");
                for (j = 0; j < 3; j++) {
                    if (i == p1 && j == p2){
                        m[i][j] = v;
                    }else if (m[i][j] == '*'){
                        m[i][j] = '*';
                    }
                    printf("%c ", m[i][j]);
                }
                printf("\n");
            }
            printf("\n");
            f2 = 1;
        }
    }
    f = 1;
  }
  return 0;
}
