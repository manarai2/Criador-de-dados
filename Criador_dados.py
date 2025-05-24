import pandas as pd   # Visualização dos dados
from faker import Faker   # Criação dos dados fictícios
import random   # Biblioteca de randomização

# Estabelecimento da região a ser usada na biblioteca faker
faker = Faker ('pt_BR')

dados_gerados = [] # Criar uma lista para colocar os dados

usuario_input = False # Mude para True se quiser alterar a quantidade de linha de dados pelo terminal

def alocar_dados(): # Define função para alocar os dados criados dentro dos loops a seguir
    dados_dicionario = {
        'Nome': nome,
        'CPF': cpf,
        'Idade': idade,
        'Data Nascimento': data,
        'Endereço': endereco,
        'Estado': estado
    }
    dados_gerados.append(dados_dicionario)

# Caso tenha alterado para input True
if usuario_input == True:
    try:
        x = int(input('Quantidade de linhas de dados: '))
    except ValueError:
        print('Digite valor inteiro')
    for _ in range(x):
        nome = faker.name()
        cpf = faker.cpf()
        idade = random.randint(18, 80)  # modificador de randomização com inteiros
        data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
        endereco = faker.address()
        estado = faker.state()

        alocar_dados()

else:
    for _ in range(15):
        # Geração dos dados com a função faker. (...)
        nome = faker.name()
        cpf = faker.cpf()
        idade = random.randint(18, 80)  # modificador de randomização com inteiros
        # Estabelece a idade de nascimento e formatação dessa data
        data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
        endereco = faker.address()
        estado = faker.state()
        # Uso da função para alocar o dicionário na lista
        alocar_dados()



# Define o panda, para visualização dos dados criados
df_dados = pd.DataFrame(dados_gerados)

# limitação da tabela
pd.set_option('display.max_columns', None) # Mostra todas as colunas do dataframe
pd.set_option('display.max_rows', None) # Mostra todas as linhas do dataframe
pd.set_option('display.max_colwidth', None) # Mostra o conteúdo das células na quantidade X
pd.set_option('display.width', None) # Configura largura de tabela, deixando no máximo

print(df_dados)

# Salvar dados para arquivos csv
df_dados.to_csv('Dados_criados.csv', index = False) # index = False -> remove coluna de índice




























