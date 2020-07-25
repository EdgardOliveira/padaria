# HEF2 - Team 15
# Objetivo: A padaria Pãozão vende diariamente uma certa quantidade de pães franceses e
# uma quantidade de broas. Cada pãozinho custa R$ 0,80 e a broa custa R$ 2,50. Do total
# arrecadado, 43% corresponde aos custos de fabricação. Do restante, Seu João guarda 15% numa
# conta de poupança e 15% ele converte em Euros para sua viagem Anual. Sabe-se que 1 Euro
# custa R$ 4,60. Com base nestes fatos, faça um programa para ler as quantidades de pães e de
# broas, calcular a venda total de pães e broas, o custo de fabricação, quanto irá guardar na
# poupança e quantos euros irá comprar. Ao final exibir os dados calculados.
#
# Product Owner  : Áurea Melo
# Scrum Master   : Edgard Oliveira      - SCRUM Master
# Scrum Team:
#   Desenvolvedor 1: Janderson Rodrigues- Calcular Total Vendido
#   Desenvolvedor 2: Matheus Nery       - Ler quantidade de pães e broas
#   Desenvolvedor 3: Wanderson Ferreira - Calcular quanto irá guardar
#   Desenvolvedor 4: Gustavo Freitas    - Calcular custo de fabricação
#   Desenvolvedor 5: Edgard Oliveira    - Calcular Euros/ Exibir Resultados


# DEFINIÇÃO DE CONSTANTES
# Preços:
#  Pão-frances: 0.80
#  Broa: 2.50

# Porcentagens:
#  43% custo de fabricação
#  15% poupança -> Converte em Euros para viagem Anual (1 Euro custa 4.6)

# Constantes globais
int_CodigoPao = 1
int_CodigoBroa = 2
flt_CustoPao = 0.8
flt_CustoBroa = 2.5
flt_PercentualCustosFabricacao = 0.43
flt_PercentualGuardarPoupanca = 0.15
flt_CustoEuro = 4.6
flt_PercentualConverterEuros = 0.15

# Variáveis globais
flt_TotalPaes = 0;
flt_TotalBroas = 0;
flt_TotalArrecadado = 0
flt_CustosFabricacao = 0
flt_LucroLiquido = 0;
flt_Poupanca = 0
flt_ValorReservadoEuro = 0
flt_Euros = 0

# Função responsável por totalizar as vendas, totalizar os valores vendidos de pães e broas
# Entrada: qtdePaes --> quantidade de paes vendidos
#          qtdeBroas --> quantidade de broas vendidas
# Saída: (atualizar 3 variáveis globais (totalPaes, totalBroas, totalArrecadado))
def fn_TotalizarVendas(int_QtdePaes, int_QtdeBroas):
    global flt_TotalArrecadado
    global flt_TotalPaes
    global flt_TotalBroas
    flt_TotalPaes = int_QtdePaes * flt_CustoPao
    flt_TotalBroas = int_QtdeBroas * flt_CustoBroa
    flt_TotalArrecadado = flt_TotalPaes + flt_TotalBroas

# Função responsável por calcular os custos de fabricação e calcular o valor de lucro líquido
# Entrada: totalArrecaddo --> valor total arrecadado
# Saída: (atualizar 2 variáveis globais (custosFabricacao e lucroLiquido))
def fn_CalcularCustoFabricacao(flt_TotalArrecadado):
    global flt_CustosFabricacao
    global flt_LucroLiquido
    flt_CustosFabricacao = flt_TotalArrecadado * flt_PercentualCustosFabricacao
    flt_LucroLiquido = flt_TotalArrecadado - flt_CustosFabricacao


# Função responsável por calcular quanto irá guardar na poupança
# Entrada: lucroLiquido
# Saída: atualizar 1 variável global com o valor guardado em poupanca
def fn_CalcularPoupanca(flt_LucroLiquido):
    global flt_Poupanca
    flt_Poupanca = flt_LucroLiquido * flt_PercentualGuardarPoupanca


# Função responsável por calcular a conversão em euros para viagem
# Entrada: Total -->  valor total das vendas (soma de valores de broas e paes) - custos de fabricação
# Saída: Euros --> valor a ser convertido em euros
def fn_CalcularEuros(flt_LucroLiquido, flt_PercentualConverterEuros):
    global flt_ValorReservadoEuro
    global flt_Euros
    flt_ValorReservadoEuro = flt_LucroLiquido * flt_PercentualConverterEuros
    flt_Euros = flt_ValorReservadoEuro / flt_CustoEuro


# Função responsável por exibir os dados calculados
# Entrada:
# Saída:
def fn_ExibirResultados(int_QtdePaes, int_QtdeBroas, flt_TotalPaes, flt_TotalBroas, flt_Poupanca, flt_Euros):
    print("#########################################################################")
    print("# Código\t| Produto\t| Valor Unitário\t| Quantidade\t| Subtotal \t#")
    print("# {0:6d}\t| {1:6s}\t|{2:5.2f}\t\t\t\t| {3:6}\t\t| {4:5.2f}".format(int_CodigoPao, "Pão", flt_CustoPao, int_QtdePaes, flt_TotalPaes))
    print("#-----------------------------------------------------------------------#")
    print("# {0:6d}\t| {1:6s}\t|{2:5.2f}\t\t\t\t| {3:6}\t\t| {4:5.2f}".format(int_CodigoBroa, "Broa", flt_CustoBroa, int_QtdeBroas, flt_TotalBroas))
    print("#---------------------------------------------------------------------- #")
    print("                                          TOTAL ARRECADADO  | {0:5.2f}".format(flt_TotalArrecadado))
    print("#########################################################################")
    print()
    print()
    print("#########################################################################")
    print("# Total Arrecadado: R$ {0:5.2f}".format(flt_TotalArrecadado))
    print("# Custos de fabricação: R$ {0:5.2f}".format(flt_CustosFabricacao))
    print("# Poupança (%): {0:5.2f}%".format(flt_PercentualGuardarPoupanca * 100))
    print("# Guardou na Poupança: R$ {0:5.2f}".format(flt_Poupanca))
    print("# Custo do Euro: R$ {0:5.2f}".format(flt_CustoEuro))
    print("# Conversao Euro (%): {0:5.2f}%".format(flt_PercentualConverterEuros * 100))
    print("# Valor reservado para converter em Euros: R$ {0:5.2f}".format(flt_ValorReservadoEuro))
    print("# Quantidade de Euros: {0:5.2f}".format(flt_Euros))
    print("#########################################################################")


def venda_diaria(int_QtdePaes, int_QtdeBroas):
    fn_TotalizarVendas(int_QtdePaes, int_QtdeBroas)
    fn_CalcularCustoFabricacao(flt_TotalArrecadado)
    fn_CalcularPoupanca(flt_LucroLiquido)
    fn_CalcularEuros(flt_LucroLiquido, flt_PercentualConverterEuros)
    fn_ExibirResultados(int_QtdePaes, int_QtdeBroas, flt_TotalPaes, flt_TotalBroas, flt_Poupanca, flt_Euros)
