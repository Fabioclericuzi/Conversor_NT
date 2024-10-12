import customtkinter
from tkcalendar import DateEntry
from funcoes_buscar_cotacoes import pegar_cotacao_moeda, conversoes_disponiveis, buscar_ultima_cotacao, buscar_cotacoes_por_data

janela = customtkinter.CTk()
janela.geometry("1000x800") 
customtkinter.set_appearance_mode("dark")

titulo = customtkinter.CTkLabel(janela, text="Conversor de moeda (Real/Dollar)", font=("", 18))
titulo.pack(padx=10, pady=10)

txt_moeda = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem e destino da conversão")
txt_moeda.pack(padx=10, pady=10)


dic_conversoes_disponiveis = conversoes_disponiveis()
def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada] 
    menu_moeda_destino.configure(values=lista_moedas_destino)
    menu_moeda_destino.set(lista_moedas_destino[0])

    
menu_moeda_origem = customtkinter.CTkOptionMenu(janela, values= list(dic_conversoes_disponiveis.keys()), 
                                                 command=carregar_moedas_destino)
menu_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de destino"])
menu_moeda_origem.pack(padx=10, pady=10)
menu_moeda_destino.pack(padx=10, pady=10)


def converter_moeda():
    moeda_origem = menu_moeda_origem.get()
    moeda_destino = menu_moeda_destino.get()
    
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        
        texto_cotacao_moeda.configure(
            text=f"1 {moeda_origem} = {cotacao} {moeda_destino}"
        )
    else:
        texto_cotacao_moeda.configure(text="Preencha ambos os campos.")


botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)
botao_converter.pack(padx=10, pady=10)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="", font=("", 15))
texto_cotacao_moeda.pack(padx=10, pady=10)

titulo_terc = customtkinter.CTkLabel(janela, text="Buscar cotações por data", font=("", 12))
titulo_terc.pack(padx=10, pady=10)

txt_data_inicio = customtkinter.CTkLabel(janela, text="Data de Início")
txt_data_inicio.pack(padx=10, pady=10)

campo_data_inicio = DateEntry(janela, date_pattern='yyyy-mm-dd')  
campo_data_inicio.pack(padx=10, pady=10)

txt_data_final = customtkinter.CTkLabel(janela, text="Data final")
txt_data_final.pack(padx=10, pady=10)

campo_data_final = DateEntry(janela, date_pattern='yyyy-mm-dd')  
campo_data_final.pack(padx=10, pady=10)

def buscar_e_mostrar_cotacoes():
    data_inicio = campo_data_inicio.get_date().strftime('%Y-%m-%d')
    data_final = campo_data_final.get_date().strftime('%Y-%m-%d')

    cotacoes = buscar_cotacoes_por_data(data_inicio, data_final)

    if cotacoes and isinstance(cotacoes, list):
        texto_resultado = "Últimas Cotações (USD para BRL):\n"
        for cotacao in cotacoes:
            data = cotacao.get("create_date", "Data não disponível")
            valor = cotacao.get("bid", "Valor não disponível")
            texto_resultado += f"{data}: {valor}\n"
    else:
        texto_resultado = "Nenhuma cotação encontrada no período ou erro na resposta da API."

    texto_cotacoes.configure(text=texto_resultado)


botao_buscar_por_data = customtkinter.CTkButton(janela, text="Buscar cotações", command=buscar_e_mostrar_cotacoes)
botao_buscar_por_data.pack(padx=10, pady=10)

texto_cotacoes = customtkinter.CTkLabel(janela, text="", font=("", 12))
texto_cotacoes.pack(padx=10, pady=10)

txt_ultima_taxa = customtkinter.CTkLabel(janela, text="Obter última taxa", font=("", 12))
txt_ultima_taxa.pack(padx=10, pady=10)

def mostrar_ultima_cotacao():
    cotacao = buscar_ultima_cotacao()
    if cotacao:
        ultima_cotacao.configure(text=f"Cotação de 1 USD para BRL: {cotacao}")
    else:
        ultima_cotacao.configure(text="Cotação não encontrada")

botao_obter_ult_taxa = customtkinter.CTkButton(janela, text="Última taxa", command=mostrar_ultima_cotacao)
botao_obter_ult_taxa.pack(padx=10, pady=10, expand=True)

ultima_cotacao = customtkinter.CTkLabel(janela, text="", font=("", 12))
ultima_cotacao.pack(padx=10, pady=10)


janela.mainloop()