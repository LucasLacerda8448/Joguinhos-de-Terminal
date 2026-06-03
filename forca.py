#IMPORTS PADRÕES DO CÓDIGO
import os
import time
import random
import re
import json
#os.system('color')

class colors:
    white = '\033[37m'
    red = '\033[91m'
    dark_red = '\033[31m'
    green = '\033[92m'
    yellow = '\033[33m'
    blue = '\033[94m'
    cyan = '\033[96m'
    purple = '\033[95m'
    dark_purple = '\033[35m'
    grey = '\033[90m'
    fim = '\033[0m'
    RED = '\033[41m'
    b_yellow = '\033[93m'
    d_green = '\033[32m'

#INSTALA AS BIBLIOTECAS NECESSÁRIAS PARA EXECUTAR O CÓDIGO
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import subprocess
import sys
import importlib

try:
    import requests
    import wonderwords
    import translate
except:
    print(colors.yellow + "PARA INICIAR O JOGO É NECESSÁRIO")
    print("INSTALAR ALGUMAS BIBLIOTECAS!" + colors.fim)
    print("Pressione" + colors.blue + " Enter " + colors.fim + "para iniciar a instalação.")
    confirm = input()
    install("requests")
    install("wonderwords")
    install("translate")
    requests = importlib.import_module("requests")
    wonderwords = importlib.import_module("wonderwords")
    translate = importlib.import_module("translate")
from wonderwords import RandomWord
from translate import Translator

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

def limpa():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Gera_tematica(tema):
    tradutorPT = Translator(from_lang="en", to_lang="pt")
    tradutorEN = Translator(from_lang="pt", to_lang="en")
    with open("palavras.json", encoding='utf-8') as palavras:
        if tema == "random":
            tema = random.choice(["Mídia"])
        palavra = json.load(palavras)
        pos = random.randrange(0, len(palavra[tema]))
        word = palavra[tema][pos]
        if tema == "Objeto" or tema == "Animal":
            try:
                desc = requests.get("https://freedictionaryapi.com/api/v1/entries/en/" + tradutorEN.translate(word))
                desc = tradutorPT.translate(desc.json()["entries"][0]["senses"][0]["definition"])
            except:
                desc = colors.red + "ERRO: Não foi possível encontrar a definição da palavra" + colors.fim
        else:
            desc = "O tema escolhido não possui definição de palavras."
    return word, tema, desc

def Gera_aleatoria(lang):
    palavra = RandomWord()
    tradutorPT = Translator(from_lang="en", to_lang="pt")
    word = palavra.word()
    desc = requests.get("https://freedictionaryapi.com/api/v1/entries/en/" + word)
    desc = desc.json()["entries"][0]["senses"][0]["definition"]
    if lang == "PT":
        word = tradutorPT.translate(word)
        desc = tradutorPT.translate(desc)
    return word, desc

def Insere_letra(word, erro, dica):
    Vogais = [
        ['A', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å'],
        ['E', 'È', 'É', 'Ê', 'Ë'],
        ['I', 'Ì', 'Í', 'Î', 'Ï'],
        ['O', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö'],
        ['U', 'Ù', 'Ú', 'Û', 'Ü']
    ]
    word2 = []
    for i in range(len(word)):
        word2.append(word[i][0])
    letra = input()
    letra = letra.upper()
    if len(erro) >= 3 and letra == '1':
        dica = 1
        vogal = 0
    else:
        while True:
            vogal = 0
            for i in Vogais:
                if letra in i:
                    vogal = i
                    break
            if letra in word2 or letra in erro:
                print("A letra inserida já foi usada, informe outra letra por favor")
                print("-> ", end="")
                letra = input()
                letra = letra.upper()
            elif vogal:
                for i in vogal:
                    if i in word2 or i in erro:
                        print("A letra inserida já foi usada, informe outra letra por favor")
                        print("-> ", end="")
                        letra = input()
                        letra = letra.upper()
                        vogal = 2
                        break
                if vogal != 2:
                    break
            else:
                break
    return letra, vogal, dica

def Compara(letra, vogal, word, word2):
    r = 0
    if vogal:
        for i in range(len(word)):
            if word[i] in vogal:
                r = 1
                word2[i][0] = word[i]
    else:
        for i in range(len(word)):
            if letra == word[i]:
                r = 1
                word2[i][0] = word[i]
    return r, word2

def ImprimeJogo(word, erro, tema, desc, dica):
    limpa()
    tam = len(erro)
    if tam == 7:
        cor = colors.dark_purple
    else:
        cor = colors.d_green
    print("Tema: " + colors.yellow + tema + colors.fim)
    print("Letras Descartadas:")
    for i in erro:
        print(colors.red + i + " " + colors.fim, end="")
    print()
    print(colors.yellow + " ╔════════╗")
    print(" ║        " + colors.grey + "│")
    print(colors.yellow + " ║        ", end="")
    if tam > 0:
        print(cor + "☻")
        print(colors.yellow + " ║       " + cor, end="")
        if tam == 2:
            print(" ║", end="")
        elif tam > 2:
            print("/║", end="")
            if tam > 3:
                print("\\", end="")
        print(colors.yellow)
        print(" ║       ", end="")
        if tam > 4:
            print(cor + "/ ", end="")
            if tam > 5:
                print("\\   ", end="")
                if tam == 7:
                    print(colors.red + "ENFORCADO!", end="")
        print(colors.yellow)
    else:
        print()
        print(" ║")
        print(" ║")
    print(" ║")
    print(" ║  " + colors.fim, end="")
    for i in range(len(word)):
        if word[i][0] == 'vazio':
            print("    ", end="")
        else:
            if word[i][1] == ' ':
                print(word[i][0] + " ", end="")
            else:
                print(" %s  " %word[i][0], end="")
    print()
    print(colors.yellow + "═╩═ " + colors.fim, end="")
    for i in range(len(word)):
        print(word[i][1] + " ", end="")
    print()
    if tam >= 3:
        print("Definição da Palavra: ", end="")
        if dica:
            print(desc)
        else:
            print(colors.blue + "Digite '1' para revelar a definição." + colors.fim)

def main():
    while True:
        limpa()
        print("╔═══════════╕")
        print("║     JOGO DA FORCA")
        print("║")
        print("║ [1] Jogar   [2] Sair")
        e = Escolha(2)
        if e == '2':
            print("ENCERRANDO JOGO...")
            break
        else:
            while True:
                limpa()
                print("╔═══════════════════════════╕")
                print("║                     MODOS DE JOGO:")
                print("║")
                print("║ [1] Palavras Temáticas      [2] Palavras Aleatórias " + colors.yellow + "(Requer Internet)" + colors.fim)
                print("║ [3] Palavras Customizadas   [4] Voltar ao Menu")
                e = Escolha(4)
                if e == '4':
                    break
                elif e == '1':
                    limpa()
                    print("Escolha o tema da palavra:")
                    print("[1] Objetos   [2] Comidas")
                    print("[3] Animais   [4] Mídia")
                    print("  [5] Tema Aleatório")
                    e = Escolha(5)
                    tema = "random"
                    if e == '1':
                        tema = "Objeto"
                    elif e == '2':
                        tema = "Comida"
                    elif e == '3':
                        tema = "Animal"
                    elif e == '4':
                        tema = "Mídia"
                    print("GERANDO A PALAVRA...")
                    word, tema, desc = Gera_tematica(tema)
                elif e == '2':
                    limpa()
                    print("Escolha o idioma da palavra aleatória:")
                    print("     [1] Português     [2] Inglês")
                    e = Escolha(2)
                    lang = "PT"
                    if e == '2':
                        lang = "EN"
                    print("GERANDO A PALAVRA...")    
                    word, desc = Gera_aleatoria(lang)
                    tema = "Aleatório"
                else:
                    print("Insira sua palavra/frase customizada: ", end="")
                    word = input()
                    print("Informe o tema da sua palavra/frase: ", end="")
                    tema = input()
                    print("Por fim, forneça uma descrição breve da sua palavra: ", end="")
                    desc = input()
                word = word.upper()
                word2 = []
                j = 0
                for i in word:
                    word2.append([])
                    if 65 <= ord(i) <= 90 or 192 <= ord(i) <= 220:
                        word2[j].append('vazio')
                        word2[j].append('───')
                    else:
                        word2[j].append(i)
                        word2[j].append(' ')
                    j += 1
                erro = []
                dica = 0
                ImprimeJogo(word2, erro, tema, desc, dica)
                print()
                while True:
                    print("Escolha uma letra para adivinhar, ou arrisque escrever a palavra toda")
                    print("-> ", end="")
                    letra, vogal, dica = Insere_letra(word2, erro, dica)
                    if len(letra) <= 1:
                        if letra != '1':
                            r, word2 = Compara(letra, vogal, word, word2)
                            if r == 0:
                                print("A letra " + colors.blue + letra + colors.fim + " foi descartada")
                                erro.append(letra)
                            else:
                                print("Letra " + colors.blue + letra + colors.fim + " adicionado")
                    else:
                        if letra == word:
                            print()
                            print(colors.green + "PALAVRA CORRETA!!" + colors.fim)
                            time.sleep(1)
                            for i in range(len(word)):
                                word2[i][0] = word[i]
                            ImprimeJogo(word2, erro, tema, desc, dica)
                            print()
                            time.sleep(0.5)
                            print("FIM DE JOGO")
                            print()
                            time.sleep(0.5)
                            break
                        else:
                            print(colors.red + "PALAVRA ESCRITA ERRADA!!" + colors.fim)
                            print()
                            time.sleep(1)
                            print("Resposta: %s" %word)
                            print()
                            time.sleep(0.5)
                            print("FIM DE JOGO")
                            print()
                            time.sleep(0.5)
                            break
                    print()
                    ImprimeJogo(word2, erro, tema, desc, dica)
                    print()
                    if len(erro) > 6:
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
                    errado = 1
                    for i in range(len(word)):
                        if word[i] != word2[i][0]:
                            errado = 0
                            break
                    if errado:
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
