# Conversor de moeda

## 1. Visão geral
Projeto realizado utilizando a linguagem python e majoritariamente a bibliotca customtkinter. O projeto consiste num sistema de conversão de moeda que está conectado a uma API que diponibiliza cotações para moedas de todo mundo. Como solicitado, o sistema realiza conversões de dollar pra real e de real pra dolar. O sistema possui também uma funcionalidade para obter a última taxa cotada e um menu onde o usuário pode escolher uma data inicial e uma data final e o sistema irá trazer 5 cotações do período escolhido.

## 2. Arquitetura
2.1 Backend: Contém a aplicação python

2.2 Frontend: Trata-se de uma janela criada com a linguagem python e a biblioteca customtkinter

2.3 Banco de Dados: Contém o MySQL, responsável pelo armazenamento de dados.

## 3. Como executar o projeto
3.1 Navegar até a pasta projeto e executar o comando python main.py. Processo também pode ser executado através do comando de execução do vscode(ou outra ide).

3.2 Para a realização de testes, basta acessar o diretório 'projeto' e executar o comando 'pytest'
## 4. Bibliotecas utilizdas

4.1 customtkinter - É uma biblioteca python que facilita na criação de interfaces gráficas. Segue o link da documentação - https://customtkinter.tomschimansky.com/documentation/

4.2 tkcalendar - fornece widgets que facilitam a escolha de datas em interfaces gráficas. Link da documentação - https://pypi.org/project/tkcalendar/

4.3 unittest.mock - Utilizada para a realização de testes unitários. Segue link da documentação - https://docs.python.org/3/library/unittest.mock.html

4.4 requests - biblioteca utilizada para requisições HTTP e facilita a interação com API's. Link da documentação - https://pypi.org/project/requests/

4.5 xmltodict  - realiza a conversão de arquivos XML para dicionários python. Segue linke da documentação - https://pypi.org/project/xmltodict/

4.6 mysql.connector - fornece interface para conexão e interação com o banco de dados Mysql. Segue link da documentação - https://pypi.org/project/mysql-connector-python/

## 5. Diagrama de estrutura

![diagrama_conversor](https://github.com/user-attachments/assets/6005f7f7-b1a7-47a6-933e-4ee1700060b2)

A estrutura do projeto se baseia em requisições HTTP através de uma API disponibilizada pelo site https://docs.awesomeapi.com.br/api-de-moedas#formato-de-resposta que fornece cotações atualizadas para moedas do mundo todo. Como mostra o diagrama, o usuário utiliza uma interface gráfica onde ele pode solicitar uma simples conversão de dollar para real e de real para dollar, existe também a possibilidade de buscar um histórico de cotações através das datas escolhidas e, por fim, a interface disponibiliza um botão que vai trazer a última cotação realizada. O sistema faz um intermédio entre o usuário e a API e guarda as informações num banco mysql. 

## 6. Prints do projeto em funcionamento
6.1 Banco de dados recebendo as informações
![mysql_conversoes](https://github.com/user-attachments/assets/5fd776dc-cb0d-433a-bfb5-2d532e377c41)

6.2 tela inicial do projeto
![tela_inicial](https://github.com/user-attachments/assets/b2663433-5fa8-4b79-8336-4a02622b75ca)

6.3 usando o botão de conversão
![conversao_1](https://github.com/user-attachments/assets/3b869c87-cdb9-46b4-abb2-16216096034e)

6.4 histórico de conversões
![historico_conversao](https://github.com/user-attachments/assets/d5b1d2dc-c3f0-40e5-8c82-71f9ae710c1b)

6.5 Obtendo a última taxa
![ultima_taxa](https://github.com/user-attachments/assets/62f505ba-96ec-4135-9c81-a92d9cb5186b)

## 7. Considerações finais
Essa documentação da uma visão geral do projeto e seu funcionamento. Junto com ela, será enviado um vídeo por e-mail mostrando a utilização do programa em funcionamento.

