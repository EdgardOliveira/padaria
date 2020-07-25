# HEF2 - Team 15
# Objetivo: A padaria Pãozão vende diariamente uma certa quantidade de pães franceses e
# uma quantidade de broas. Cada pãozinho custa R$ 0,80 e a broa custa R$ 2,50. Do total
# arrecadado, 43% corresponde aos custos de fabricação. Do restante, Seu João guarda 15% numa
# conta de poupança e 15% ele converte em Euros para sua viagem Anual. Sabe-se que 1 Euro
# custa R$ 4,60. Com base nestes fatos, faça um programa para ler as quantidades de pães e de
# broas, calcular a venda total de pães e broas, o custo de fabricação, quanto irá guardar na
# poupança e quantos euros irá comprar. Ao final exibir os dados calculados.
#
# Entrada: 864
# Saída: 468
#
# Product Owner  : Áurea Melo
# Scrum Master   : Edgard Oliveira      - SCRUM Sprint Planning/Merge
# Scrum Team:
#   Desenvolvedor 1: Janderson Rodrigues- 
#   Desenvolvedor 2: Matheus Nery       - 
#   Desenvolvedor 3: Wanderson Ferreira - 
#   Desenvolvedor 4: Gustavo Freitas    - 


# DEFINIÇÃO DE CONSTANTES
# Preços:
#  Pão-frances: 0.80
#  Broa: 2.50

# Porcentagens:
#  43% custo de fabricação
#  15% poupança -> Converte em Euros para viagem Anual (1 Euro custa 4.6)

# Função responsável por ler a quantidade de pães e broas
# Entrada: CodigoProduto --> produto que está sendo comprado
#          QtdeProduto --> quantidade do produto que está sendo comprado
# Saída: salvar a compra num array
def fn_LerQuantidades(int_CodigoProduto, int_QtdeProduto):

# Função responsável por calcular a quantidade de vendas de pães e broas
# Entrada: ler o array, somar os valores dos produtos
# Saída: (atualizar 4 variáveis globais (totalPaes, totalBroas, totalValorPaes, totalValorBroas))
def fn_TotalizarVendas():

# Função responsável por calcular os custos de fabricação
# Entrada: QtdePaes -->
#          QtdeBroas -->
# Saída: (atualizar 2 variáveis globais (custosPaes, custosBroa))
def fn_CalularCustos(int_QtdePaes, int_QteBroas):

# Função responsável por calcular quanto irá guardar na poupança
# Entrada: Total -->  valor total das vendas (soma de valores de broas e paes)
#        
# Saída: Poupanca --> valor a ser guardado
def fn_CalularCustos(float_Total):

# Função responsável por calcular a conversão em euros para viagem
# Entrada: Total -->  valor total das vendas (soma de valores de broas e paes)
#        
# Saída: Euros --> valor a ser convertido em euros
def fn_CalularEuros(float_Total):


# Função responsável por exibir os dados calculados
# Entrada: 
# Saída: 
def fn_ExibirResultados(int_QtdePaes, int_QteBroas, float_TotalPaes, float_TotalBroas, float_Poupanca, float_Euros):
