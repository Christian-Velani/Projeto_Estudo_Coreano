import random as rm
import playsound as ps

class Exercicio:
    def __init__(self, texto_coreano, texto_portugues, audio = None):
        self.texto_coreano = texto_coreano
        self.texto_portugues = texto_portugues
        self.audio = audio

def mostrar_menu():
    print('''
        1 - Coreano
        2 - Português
        3 - Adicionar Palavra
        4 - Adicionar Frase
        5 - Consultar Resultados
        7 - Sair
        ''')
    try:
        menu = int(input('Escolha: '))
        if menu >= 1 and menu <= 7:
            encaminhar_menu(menu)
        else:
            raise ValueError
    except ValueError:
        print('Valor Inválido')
        mostrar_menu()

def encaminhar_menu(menu):
    if menu == 1:
        menu_secundario('Coreano')
    elif menu == 2:
        menu_secundario('Portugues')        
    elif menu == 3:
        adicionar_palavra()
    elif menu == 4:
        adicionar_frase()
    elif menu == 5:
        consultar_resultados()
    elif menu == 7:
        exit

def menu_secundario(idioma):
    print('''
        1 - Palavra
        2 - Frase
        3 - Retornar para o Menu Principal
        ''')
    try:
        tipo = int(input('Escolha: '))
        if tipo >= 1 and tipo <= 3:
            if tipo == 1:
                menu_final(idioma, "Palavra")
            elif tipo == 2:
                menu_final(idioma, 'Frase')
            elif tipo == 3:
                mostrar_menu()
        else:
            raise ValueError
    except ValueError:
        print('Valor inválido')
        menu_secundario(idioma)

def menu_final(idioma, tipo):
    print('''
        1 - Texto
        2 - Aúdio
        3 - Voltar
        ''')
    try:
        tipo2 = int(input('Escolha: '))
        if tipo2 >= 1 and tipo2 <= 3:
            if tipo2 == 1:
                exercicio_texto(idioma, tipo)
            elif tipo2 == 2:
                exercicio_audio(idioma, tipo)
            elif tipo2 == 3:
                menu_secundario(idioma)
        else:
            raise ValueError
    except ValueError:
        print('Valor Inválido')
        menu_final(idioma, tipo)

def adicionar_palavra():
    palavra_coreano = input('Palavra em Coreano a ser adicionada: ')
    palavra_portugues = input('Tradução da Palavra: ')
    adicionar_ao_arquivo(palavra_coreano, palavra_portugues, 'Palavra')

def adicionar_frase():
    frase_coreano = input('Frase em Coreano a ser adicionada: ')
    frase_portugues = input('Tradução da Frase: ')
    adicionar_ao_arquivo(frase_coreano, frase_portugues, 'Frase')

def adicionar_ao_arquivo(coreano, portugues, tipo):
    tipo = tipo + 's'
    if coreano != None and portugues != None:
        coreano = " ".join(coreano.strip().split())
        portugues = " ".join(portugues.strip().split())
        with open('palavras.txt', 'a+', encoding="utf-8") as palavras, open('frases.txt', 'a+', encoding="utf-8") as frases:
            if tipo == 'Palavras':
                palavras.write(f'\n{coreano} {portugues}')
            else:
                frases.write(f'\n{coreano}#{portugues}')
    else:
        print('Alguma informação estava incorreta')
        if tipo == 'Palavras':
            adicionar_palavra()
        else:
            adicionar_frase()
    mostrar_menu()

def gerar_exercicio(tipo):
    categoria = tipo + 's'
    with open('palavras.txt', 'r', encoding="utf-8") as palavras, open('frases.txt', 'r', encoding="utf-8") as frases:
        if categoria == 'Palavras':
            p = palavras.readlines()
            quantidade = len(p)
            numero = rm.randint(1, quantidade)
            coreano, portugues = p[numero-1].split()
        else:
            fr = palavras.readlines()
            quantidade = len(fr)
            numero = rm.randint(1, quantidade)
            coreano, portugues = fr[numero-1].split('#')
    audio = 'Audios/' + tipo + ' (' + str(numero) + ')' + '.mp3'
    exercicio = Exercicio(coreano, portugues, audio)
    return exercicio

def exercicio_texto(idioma, tipo):
    exercicio = gerar_exercicio(tipo)
    if idioma == 'Coreano':
        print(f'Traduza: {exercicio.texto_coreano}')
        resposta = input('Resposta: ')
        resposta = " ".join(resposta.strip().split())
        if resposta == exercicio.texto_portugues:
            print('Resposta Certa')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
        else:
            print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_portugues}\n Resposta dada: {resposta}')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')
    elif idioma == 'Portugues':
        print(f'Traduza: {exercicio.texto_portugues}')
        resposta = input('Resposta: ')
        resposta = " ".join(resposta.strip().split())
        if resposta == exercicio.texto_coreano:
            print('Resposta Certa')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
        else:
            print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_coreano}\n Resposta dada: {resposta}')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')   
    menu_final(idioma, tipo)

def exercicio_audio(idioma = None, tipo = None, exerciciore = None):
    if exerciciore == None:
        exercicio = gerar_exercicio(tipo)
    else:
        exercicio = exerciciore
    ps.playsound(exercicio.audio)
    try:
        escolha = int(input('''
        Escolha:
        1- Ouvir de Novo
        2- Responder
        Escolha: '''))
        if escolha >= 1 and escolha <= 2:
            if escolha == 1:
                exercicio_audio(idioma, tipo, exercicio)
            elif escolha == 2:
                resposta = input('Resposta: ')
            if idioma == 'Coreano':
                resposta = " ".join(resposta.strip().split())
                if resposta == exercicio.texto_portugues:
                    print('Resposta Certa')
                    salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
                else:
                    print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_portugues}\n Resposta dada: {resposta}')
                    salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')
            if idioma == 'Portugues':
                resposta = " ".join(resposta.strip().split())
                if resposta == exercicio.texto_coreano:
                    print('Resposta Certa')
                    salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
                else:
                    print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_coreano}\n Resposta dada: {resposta}')
                    salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')   
            menu_final(idioma, tipo)
        else:
            raise ValueError
    except ValueError:
        print('Valor Inválido')
        exercicio_audio(idioma, tipo, exercicio)

def salvar(idioma, frase_palavra, tipo_exercicio, coreano, portugues, resposta, resultado):
    with open('resultados.txt', 'a+', encoding="utf-8") as resultados:
        resultados.write(f'\n{idioma}#{frase_palavra}#{tipo_exercicio}#{coreano}#{portugues}#{resposta}#{resultado}')

def consultar_resultados():
    with open('resultados.txt', 'r', encoding="utf-8") as resultados:
        resultado = resultados.readlines()
        for resultad in resultado:
            print(f' Idioma: {resultado[0]}, Tipo: {resultado[1]}, Tipo de Exercicio: {resultado[2]}, Texto em Coreano: {resultado[3]}, Texto em Português: {resultado[4]}, Resposta: {resultado[5]}, Resultado: {resultado[6]}')
    mostrar_menu()

mostrar_menu()