import pandas as pd

dados = pd.read_csv('dados.csv')

#print(dados)

print(sorted(dados['Anos de Estudo'].unique()))

print(sorted(dados['UF'].unique()))
print(sorted(dados['Sexo'].unique()))
print(sorted(dados['Idade'].unique()))
print(sorted(dados['Cor'].unique()))

print(dados.Idade.max())

print('De %s até %s anos' % (dados.Idade.min(), dados.Idade.max()))

print('De %s até %s metros' % (dados['Altura'].min(), dados.Altura.max()))