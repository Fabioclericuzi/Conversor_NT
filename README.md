# Conversor de moeda

## 1. Visão geral
Projeto realizado utilizando a linguagem python e majoritariamente a bibliotca customtkinter. O projeto consiste num sistema de conversão de moeda que está conectado a uma API que diponibiliza cotações para moedas de todo mundo. Como solicitado, o sistema realiza conversões de dollar pra real e de real pra dolar. O sistema possui também uma funcionalidade para obter a última taxa cotada e um menu onde o usuário pode escolher uma data inicial e uma data final e o sistema irá trazer 5 cotações do período escolhido.

## 2. Arquitetura
2.1 Backend: Contém a aplicação python

2.2 Frontend: Trata-se de uma janela criada com a linguagem python e a biblioteca customtkinter

2.3 Banco de Dados: Contém o MySQL, responsável pelo armazenamento de dados.

## 3. Como executar o projeto

Navegar até a pasta projeto e executar o comando python main.py. Processo também pode ser executado através do comando de execução do vscode(ou outra ide).

## 4. Bibliotecas utilizdas

4.1 customtkinter - É uma biblioteca python que facilita na criação de interfaces gráficas. Segue o link da documentação - https://customtkinter.tomschimansky.com/documentation/

4.2 tkcalendar - fornece widgets que facilitam a escolha de datas em interfaces gráficas. Link da documentação - https://pypi.org/project/tkcalendar/

4.3 unittest.mock - Utilizada para a realização de testes unitários. Segue link da documentação - https://docs.python.org/3/library/unittest.mock.html

4.4 requests - biblioteca utilizada para requisições HTTP e facilita a interação com API's. Link da documentação - https://pypi.org/project/requests/

4.5 xmltodict  - realiza a conversão de arquivos XML para dicionários python. Segue linke da documentação - https://pypi.org/project/xmltodict/

4.6 mysql.connector - fornece interface para conexão e interação com o banco de dados Mysql. Segue link da documentação - https://pypi.org/project/mysql-connector-python/

## 5. Diagrama de estrutura

![diagrama_conversor](https://github.com/user-attachments/assets/6005f7f7-b1a7-47a6-933e-4ee1700060b2)




