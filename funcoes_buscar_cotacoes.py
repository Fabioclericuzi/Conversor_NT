import requests
import xmltodict

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

import requests

def buscar_ultima_cotacao():
    url = "http://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cotacao = dados["USDBRL"]["bid"]
        return cotacao
    else:
        print(f"Erro na requisição: {resposta.status_code}")
        return None
    
import requests

def buscar_cotacoes_por_data(data_inicio, data_final):
    url = (
        f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/5"
        f"?start_date={data_inicio.replace('-', '')}&end_date={data_final.replace('-', '')}"
    )

    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()  
    else:
        return None



