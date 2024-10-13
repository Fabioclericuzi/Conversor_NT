from unittest.mock import patch
from app import pegar_cotacao_moeda
from funcoes_buscar_cotacoes import conectar_mysql

def test_pegar_cotacao_valida():
    cotacao = pegar_cotacao_moeda("USD", "BRL")
    assert cotacao is not None
    assert float(cotacao) > 0

def test_conexao_banco():
    conexao = conectar_mysql()
    assert conexao is not None
    conexao.close()

@patch('requests.get')
def test_pegar_cotacao_invalida(mock_get):
    mock_get.return_value.json.return_value = {
        "USDBRL": {"bid": None}
    }

    cotacao = pegar_cotacao_moeda("USD", "BRL")
    assert cotacao is None