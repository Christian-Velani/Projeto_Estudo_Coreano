import random as rm
import playsound as ps
import Conectar

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
        6 - Sair
        ''')
    menu = int(input('Escolha: '))
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
    elif menu == 6:
        return -1

def menu_secundario(idioma):
    print('''
        1 - Palavra
        2 - Frase
        3 - Retornar para o Menu Principal
        ''')
    tipo = int(input('Escolha: '))
    if tipo == 1:
        menu_final(idioma, "Palavras")
    elif tipo == 2:
        menu_final(idioma, 'Frases')
    elif tipo == 3:
        mostrar_menu()

def menu_final(idioma, tipo):
    print('''
        1 - Texto
        2 - Aúdio
        3 - Voltar
        ''')
    tipo2 = int(input('Escolha: '))
    if tipo2 == 1:
        exercicio_texto(idioma, tipo)
    elif tipo2 == 2:
        exercicio_audio(idioma, tipo)
    elif tipo2 == 3:
        menu_secundario(idioma)

def adicionar_palavra():
    palavra_coreano = input('Palavra em Coreano a ser adicionada: ')
    palavra_portugues = input('Tradução da Palavra: ')
    adicionar_ao_banco(palavra_coreano, palavra_portugues, 'Palavras')

def adicionar_frase():
    frase_coreano = input('Frase em Coreano a ser adicionada: ')
    frase_portugues = input('Frase da Palavra: ')
    adicionar_ao_banco(frase_coreano, frase_portugues, 'Frases')

def adicionar_ao_banco(coreano, portugues, tipo):
    conexao = Conectar.conectar()
    cursor = conexao.cursor()
    if coreano != None and portugues != None:
        coreano = " ".join(coreano.strip().split())
        portugues = " ".join(coreano.strip().split())
        cursor.execute(f'INSERT INTO {tipo} VALUES(NULL, "{coreano}", "{portugues}")')
        conexao.commit()
    else:
        print('Alguma informação estava incorreta')
        if tipo == 'Palavras':
            adicionar_palavra()
        else:
            adicionar_frase()
    mostrar_menu()

def gerar_exercicio(tipo):
    conexao = Conectar.conectar()
    cursor = conexao.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM {tipo}')
    quantidade = cursor.fetchone()
    if tipo == 'Palavras':
        numero = rm.randint(1, quantidade[0])
        print(numero)
        cursor.execute(f'SELECT COREANO, PORTUGUÊS FROM PALAVRAS WHERE ID = {numero}')
        valores = cursor.fetchone()
        audio = 'Audios/' + 'palavra'+ '_' + str(numero) + '.mp3'
        print(audio)
        exercicio = Exercicio(valores[0], valores[1], audio)
    elif tipo == 'Frases':
        numero = rm.randint(1, quantidade[0])
        cursor.execute(f'SELECT COREANO, PORTUGUÊS FROM FRASES WHERE ID = {numero}')
        valores = cursor.fetchone()
        audio = 'Audios/' + 'frase_' + str(numero) + '.mp3'
        exercicio = Exercicio(valores[0], valores[1], audio)
    return exercicio

def exercicio_texto(idioma, tipo):
    exercicio = gerar_exercicio(tipo)
    if idioma == 'Coreano':
        print(f'Traduza: {exercicio.texto_coreano}')
        resposta = input('Resposta: ')
        if resposta == exercicio.texto_portugues:
            print('Resposta Certa')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
        else:
            print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_portugues}\n Resposta dada: {resposta}')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')
    elif idioma == 'Portugues':
        print(f'Traduza: {exercicio.texto_portugues}')
        resposta = input('Resposta: ')
        if resposta == exercicio.texto_coreano:
            print('Resposta Certa')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
        else:
            print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_coreano}\n Resposta dada: {resposta}')
            salvar(idioma, tipo, 'Texto', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')   
    menu_final(idioma, tipo)

def exercicio_audio(idioma, tipo):
    exercicio = gerar_exercicio(tipo)
    ps.playsound(exercicio.audio)
    escolha = int(input('''
    Escolha:
    1- Ouvir de Novo
    2- Responder
    Escolha: '''))
    if escolha == 1:
        ps.playsound(exercicio.audio)
    elif escolha == 2:
        resposta = input('Resposta: ')
    if idioma == 'Coreano':
        if resposta == exercicio.texto_portugues:
            print('Resposta Certa')
            salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
        else:
            ps.playsound(exercicio_audio)
            print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_portugues}\n Resposta dada: {resposta}')
            salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')
    if idioma == 'Portugues':
        if resposta == exercicio.texto_coreano:
            print('Resposta Certa')
            salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Acerto')
        else:
            print(f'Resposta Errada\nA resposta certa seria {exercicio.texto_coreano}\n Resposta dada: {resposta}')
            salvar(idioma, tipo, 'Aúdio', exercicio.texto_coreano, exercicio.texto_portugues, resposta, 'Erro')   
    menu_final(idioma, tipo)

def salvar(idioma, frase_palavra, tipo_exercicio, coreano, portugues, resposta, resultado):
    conexao = Conectar.conectar()
    cursor = conexao.cursor()
    cursor.execute(f'INSERT INTO RESULTADOS VALUES(NULL, "{idioma}", "{frase_palavra}", "{tipo_exercicio}", "{coreano}", "{portugues}", "{resposta}", "{resultado}")')
    conexao.commit()

def consultar_resultados():
    conexao = Conectar.conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT IDIOMA, FRASE_PALAVRA, TIPO_EXERCICIO, COREANO, PORTUGUES, RESPOSTA, RESULTADO FROM RESULTADOS')
    resultados = conexao.fetchall()
    print('Esses são seus resultados:')
    for resultado in resultados:
        print(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6])

mostrar_menu()