#include <stdio.h>
#include <string.h>
#define c 3
#define l 3

int main() {
  int i, j, f = 0;
  char m[c][l], e, v;

  printf("JOGO DA VELHA\n");
  printf("\n");
  while (f == 0){
    for (i = 0; i < 3; i++) {
        printf("    ");
        for (j = 0; j < 3; j++) {
            m[i][j] = '#';
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
        while(1){
            printf("-> ");
            scanf("%d %d", &i, &j);
            if (i > 2 || j > 2){
                printf("Valores inválidos, insira outro valor.\n");
            }else{
                printf("\n");
                break;
            }
        }
        m[i][j] = v;
        for (i = 0; i < 3; i++) {
            printf("    ");
            for (j = 0; j < 3; j++) {
                printf("%c ", m[i][j]);
            }
            printf("\n");
        }
        printf("\n"); 
    }
    f = 1;
  }
  return 0;
}