import os
import time
import random
os.system('color')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[33m'
    grey = '\033[90m'
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

def Palavras():
    aleatorio = ["CASA", "TESOURA", "CARRO", "BALDE", "FACA", "CAVALO", "BANANA", "FOGAO", "PICOLE", "BRANCO", "SERROTE",
                "CHAPEU", "CADEIRA", "BOLA", "AZUL", "ESCADA", "OCULOS", "CHAVE", "DADO", "MALA", "LAMPADA", "REVOLVER", 
                "BARRACA", "CINTO", "PERA", "PENA", "PINCEL", "VESTIDO", "CIGARRO", "BOLO", "SAPO", "TORNEIRA", "SACOLA",
                "PANELA", "COPO", "KILL BILL", "MAZE RUNNER: CORRER OU MORRER", "GRAVATA", "VELA", "VIOLAO", "CABIDE",
                "FOLHA", "CASTELO", "AMARELO", "AVIAO", "CAMA", "DOCE", "ESTOJO", "GELEIA", "PRETO", "JANELA", "NOITE",
                "PAO", "UMBIGO", "VERMELHO", "BASQUETE", "CHAMPANHE", "HETEROSSEXUAL", "HOMOSSEXUAL", "AMENDOIM", "BANHEIRO",
                "ESPARADRAPO", "FORCA", "GALAXIA", "MANJERICAO", "XICARA", "LIVRARIA", "FITA ADESIVA", "PRATO", "SUBMARINO",
                "COMPUTADOR", "MESA DE JANTAR", "PORTA", "GUARDA-ROUPA", "SOL", "LUA", "MERCURIO", "VENUS", "TERRA", "MARTE",
                "JUPITER", "SATURNO", "NETUNO", "URANO", "VERDE", "RODO", "LIXO", "TATU", "VACA", "BOTA", "CAFE", "GATO",
                "BULE", "MOTO", "BOCA", "MEIA", "UVA", "MOLA", "LATA", "ROSA", "VASO", "BICO", "EMA", "TEIA", "FOCA", "LUVA",
                "TETO", "RATO", "PATO", "LOBO", "OVO", "FOGO", "MATO", "SOPA", "DEDO", "BOI", "FADA", "CIDADE DE DEUS",
                "VINGADORES: ULTIMATO", "HOMEM-ARANHA", "HANNAH MONTANA", "MENINAS MALVADAS", "VINGADORES: ERA DE ULTRON",
                "DIVERGENTE", "JOGOS VORAZES", "NARUTO", "POKEMON", "DRAGON BALL", "HARRY POTTER", "MATRIX", "AS BRANQUELAS",
                "EM RITMO DE FUGA", "CLUBE DA LUTA", "TRUQUE DE MESTRE", "ESQUECERAM DE MIM", "THE OFFICE", "FRIENDS",
                "BIG BANG: A TEORIA", "AVATAR: O ULTIMO MESTRE DO AR", "CAPITAO AMERICA: GUERRA CIVIL"]
    midia = ["CIDADE DE DEUS", "VINGADORES: ULTIMATO", "HOMEM-ARANHA", "HANNAH MONTANA", "MENINAS MALVADAS", "KILL BILL",
            "MAZE RUNNER: CORRER OU MORRER", "DIVERGENTE", "JOGOS VORAZES", "NARUTO", "POKEMON", "DRAGON BALL", "HARRY POTTER",
            "MATRIX", "AS BRANQUELAS", "EM RITMO DE FUGA", "CLUBE DA LUTA", "TRUQUE DE MESTRE", "ESQUECERAM DE MIM", "THE OFFICE",
            "FRIENDS", "BIG BANG: A TEORIA", "AVATAR: O ULTIMO MESTRE DO AR", "CAPITAO AMERICA: GUERRA CIVIL", "VINGADORES: ERA DE ULTRON"]
    animais = ["CAVALO", "SAPO", "TATU", "VACA", "GATO", "EMA", "FOCA", "RATO", "PATO", "LOBO", "BOI"]
    comidas = ["BANANA", "PICOLE", "PERA", "BOLO", "GELEIA", "PAO", "CHAMPANHE", "AMENDOIM", "MANJERICAO", "CAFE", "UVA",
                "OVO", "SOPA"]
    geral = ["CASA", "BRANCO", "AZUL", "CASTELO", "AMARELO", "DOCE", "PRETO", "NOITE", "UMBIGO", "VERMELHO", "BASQUETE",
            "HETEROSSEXUAL", "HOMOSSEXUAL", "BANHEIRO", "GALAXIA", "LIVRARIA", "SOL", "LUA", "MERCURIO", "VENUS", "TERRA",
            "MARTE", "JUPITER", "SATURNO", "NETUNO", "URANO", "VERDE", "BOCA", "ROSA", "BICO", "TETO", "FOGO", "MATO",
            "DEDO", "FADA"]
    objetos = ["TESOURA", "CARRO", "BALDE", "FACA", "FOGAO", "SERROTE", "CHAPEU", "CADEIRA", "BOLA", "ESCADA", "OCULOS",
                "CHAVE", "DADO", "MALA", "LAMPADA", "REVOLVER", "BARRACA", "CINTO", "PENA", "PINCEL", "VESTIDO", "CIGARRO",
                "TORNEIRA", "SACOLA", "PANELA", "COPO", "GRAVATA", "VELA", "VIOLAO", "CABIDE", "FOLHA", "AVIAO", "CAMA",
                "ESTOJO", "JANELA", "ESPARADRAPO", "FORCA", "XICARA", "FITA ADESIVA", "PRATO", "SUBMARINO", "COMPUTADOR",
                "MESA DE JANTAR", "PORTA", "GUARDA-ROUPA", "RODO", "LIXO", "BOTA", "BULE", "MOTO", "MEIA", "MOLA", "LATA",
                "VASO", "TEIA", "LUVA"]
    l = random.randint(1, 6)
    if l == 1:
        e = random.choice(aleatorio)
        tema = "Aleatório"
    elif l == 2:
        e = random.choice(midia)
        tema = "Mídia"
    elif l == 3:
        e = random.choice(animais)
        tema = "Animais"
    elif l == 4:
        e = random.choice(comidas)
        tema = "Comidas"
    elif l == 5:
        e = random.choice(geral)
        tema = "Geral"
    else:
        e = random.choice(objetos)
        tema = "Objetos"
    return e, tema

def Compara(letra, lr, lj):
    r = 0
    for i in range(len(lr)):
        if letra == lr[i]:
            r = 1
            lj[i] = letra
    return r

def ImprimeJogo(lj, ld, tema, e):
    print("Tema: " + colors.yellow + "%s" %tema + colors.fim)
    print("Palavras Descartadas: ", end="")
    if len(ld) == 0:
        print()
    else:
        for i in ld:
            print(colors.red + "%s " %i + colors.fim, end="")
        print()
    print("_____")
    print("|   |")
    if e >= 1:
        print("|   O")
        if e == 1:
            print("|")
        elif e == 2:
            print("|   |")
        elif e == 3:
            print("|  /|")
        else:
            print("|  /|\\")
            if e >= 5:
                print("|  / ", end="")
                if e >= 6:
                    if e == 6:
                        print("\\   ")
                    else:
                        print("\\   " + colors.red + "VOCÊ PERDEU" + colors.fim)
                else:
                    print()
            else:
                print("|")
    else:
        print("|")
        print("|")
        print("|")
    print("|")
    print("|", end="")
    cont = 0
    l = 1
    for i in lj:
        print("%s " %i, end="")
        cont += 1
        if cont >= (15 * l):
            if i == ' ':
                print()
                print(" ", end="")
                l += 1
    print()
    
def main():
    print("----------------- JOGO DA FORCA -----------------")
    print()
    while True:
        e = '/'
        while '1' != e != '2' and e != '3':
            print("[1] Palavra pré-gerada   [2] Palavra customizada")
            print("                   [3] Sair")
            print("-> ", end="")
            e = input()
            print()

        if e == '3':
            print("ENCERRANDO JOGO...")
            break
        else:
            if e == '1':
                word, tema = Palavras()
            elif e == '2':
                print("Insira a palavra/frase que deseja utilizar: ", end="")
                word = input()
                print()
                word = word.upper()
                tema = "Personalizado"

            word2 = []
            for i in word:
                if 65 <= ord(i) <= 90:
                    word2.append('_')
                else:
                    word2.append(i)
            print("INICIANDO JOGO")
            print()
            ne = 0
            erro = []
            ImprimeJogo(word2, erro, tema, ne)
            print()
            while True:
                print("Escolha uma letra para adivinhar, ou arrisque escrever a palavra toda")
                print("-> ", end="")
                while True:
                    letra = input()
                    letra = letra.upper()
                    if letra in word2:
                        print("O símbolo inserido ja foi usado, informe outro símbolo por favor")
                        print("-> ", end="")
                    else:
                        break
                print()
                if len(letra) == 1:
                    r = Compara(letra, word, word2)
                    if r == 0:
                        print("O símbolo %s foi descartado" %letra)
                        erro.append(letra)
                        ne += 1
                    else:
                        print("Símbolo %s adicionado" %letra)
                else:
                    if letra == word:
                        print(colors.green + "PALAVRA CORRETA!!" + colors.fim)
                        time.sleep(1)
                        ImprimeJogo(word, erro, tema, ne)
                        print()
                        time.sleep(0.5)
                        print("FIM DE JOGO")
                        print()
                        time.sleep(0.5)
                        break
                    else:
                        print("A palavra escrita está errada")
                        time.sleep(0.5)
                        ne += 1
                print()
                ImprimeJogo(word2, erro, tema, ne)
                print()
                if ne > 6:
                    print(colors.red + "PALAVRA NÃO ENCONTRADA!!" + colors.fim)
                    print()
                    time.sleep(1)
                    print("Resposta: %s" %word)
                    print()
                    time.sleep(0.5)
                    print("FIM DE JOGO")
                    print()
                    time.sleep(0.5)
                    break
                errado = 0
                for i in range(len(word)):
                    if word[i] != word2[i]:
                        errado = 1
                if errado == 0:
                    print(colors.green + "PALAVRA ENCONTRADA!!" + colors.fim)
                    print()
                    time.sleep(1)
                    print("FIM DE JOGO")
                    print()
                    time.sleep(0.5)
                    break

            print("[1] Jogar Novamente   [2] Sair")
            if Escolha(2) == '2':
                print("ENCERRANDO JOGO...")
                break
            else:
                print("INICIANDO NOVO JOGO...")
                print()

main()
