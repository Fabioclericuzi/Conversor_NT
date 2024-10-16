# Conversor de moeda

## 1. Visão geral
Projeto realizado utilizando a linguagem python e majoritariamente a bibliotca customtkinter. O projeto consiste num sistema de conversão de moeda que está conectado a uma API que diponibiliza cotações para moedas de todo mundo. Como solicitado, o sistema realiza conversões de dollar pra real e de real pra dolar. O sistema possui também uma funcionalidade para obter a última taxa cotada e um menu onde o usuário pode escolher uma data inicial e uma data final e o sistema irá trazer 5 cotações do período escolhido.

## 2. Arquitetura
2.1 Backend: Contém a aplicação python onde é possível acionar os endpoints de conversão, buscar por datas e de obter a última cotação realizada

2.2 Frontend: Trata-se de uma janela criada com a linguagem python e a biblioteca customtkinter

2.3 Banco de Dados: Contém o MySQL, responsável pelo armazenamento de dados.

## 3. Como executar o projeto
3.1 Para rodar o projeto é necessário instalar as dependências com o comando 'pip install -r requirements.txt', criar o schema mysql rodando o comando 'CREATE DATABASE cotacoes', alterar os dados de conexão com seus dados na função conectar_mysql do arquivo funcoes_buscar_cotacoes e rodar o comando 'python app.py' no terminal dentro da pasta projeto.

3.2 Para a realização de testes, basta acessar o diretório 'projeto' e executar o comando 'pytest'
## 4. Bibliotecas utilizadas

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

6.1 tela inicial do projeto
![tela_inicial](https://github.com/user-attachments/assets/b2663433-5fa8-4b79-8336-4a02622b75ca)

6.2 usando o botão de conversão
![conversao_1](https://github.com/user-attachments/assets/3b869c87-cdb9-46b4-abb2-16216096034e)
Esse enpoint disponibiliza um menu onde se pode escolher entre real e dollar e, ao se acionar o botão de conversão, é realizada uma requisição para API que devolve o valor da conversão atual das moedas escolhidas

6.3 histórico de conversões
![historico_cotacoes_correto](https://github.com/user-attachments/assets/246c98c7-3321-42b9-833a-0944b75e77c1)
Esse endpoint trás as conversões através da escolha de datas pelos usuários fazendo uma requisição http para a API que responde com 5 cotações entre as datas escolhidas

6.4 Obtendo a última taxa
![image](https://github.com/user-attachments/assets/ff708153-4916-4a8e-b6b3-aeee4b5c7f72)

esse endpoint carrega a última cotação ao se acionar o botão na interface

## 7. Considerações finais
Essa documentação da uma visão geral do projeto e seu funcionamento. Junto com ela, será enviado um vídeo por e-mail mostrando a utilização do programa em funcionamento.

