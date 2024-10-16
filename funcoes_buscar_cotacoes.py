import requests
import xmltodict
import mysql.connector
from datetime import datetime

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    link = f"http://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"

    requisicao = requests.get(link)

    cotacao = requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao  


def conversoes_disponiveis():
    with open("conversoes.xml", "rb") as arquivo_conversoes:
        dict_conversoes = xmltodict.parse(arquivo_conversoes)

    conversoes = dict_conversoes["xml"]
    dic_conversoes_disponiveis = {}
    for par_conversoes in conversoes:
        moeda_origem, moeda_destino = par_conversoes.split("-")
        if moeda_origem in dic_conversoes_disponiveis:
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]
    return dic_conversoes_disponiveis   


def buscar_ultima_cotacao():
    url = "http://economia.awesomeapi.com.br/json/last/BRL-USD"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cotacao = dados["BRLUSD"]["bid"]
        return cotacao
    else:
        print(f"Erro na requisição: {resposta.status_code}")
        return None
    

def buscar_cotacoes_por_data(data_inicio, data_final):
    url = (
        f"https://economia.awesomeapi.com.br/json/daily/BRL-USD/5"
        f"?start_date={data_inicio.replace('-', '')}&end_date={data_final.replace('-', '')}"
    )

    resposta = requests.get(url)
    if resposta.status_code == 200:
        cotacoes = resposta.json()
        return formatar_cotacoes(cotacoes)
    else:
        print(f"Erro ao buscar cotações: {resposta.status_code}")
        return []

def formatar_cotacoes(cotacoes):
    lista_formatada = []

    for cotacao in cotacoes:
        timestamp = int(cotacao["timestamp"])
        data = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        lista_formatada.append({"data": data, "bid": cotacao.get("bid")})

    return lista_formatada


    
def conectar_mysql():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="nautico#20",  
        database="cotacoes"   
    )
    return conexao

def salvar_cotacao(valor, tipo):
    conexao = conectar_mysql()
    cursor = conexao.cursor()

    query = "INSERT INTO cotacoes (valor, tipo) VALUES (%s, %s)"
    valores = (valor, tipo)

    cursor.execute(query, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def criar_tabela():
    conexao = conectar_mysql()
    cursor = conexao.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS cotacoes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        valor DECIMAL(10, 5),
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        tipo VARCHAR(50)
    );
    """
    cursor.execute(query)
    conexao.commit()

    cursor.close()
    conexao.close()

criar_tabela()







