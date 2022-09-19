import Conectar

conexao = Conectar.conectar()
cursor = conexao.cursor()

def arquivo_palavras():
    tamanho = 0
    with open('palavras.txt', 'a+', encoding='utf-8') as palavras:
        cursor.execute('SELECT * FROM PALAVRAS')
        query = cursor.fetchall()
        for linha in query:
            if tamanho == 0:
                palavras.write(f'{linha[1]} {linha[2]}')
            else:
                palavras.write(f'\n{linha[1]} {linha[2]}')
            tamanho += 1
