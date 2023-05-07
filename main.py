import pandas as pd
import numpy as np
import seaborn as sns

dados = pd.read_csv('dados.csv')

#print(dados)

#print(sorted(dados['Anos de Estudo'].unique()))

#print(sorted(dados['UF'].unique()))
#print(sorted(dados['Sexo'].unique()))
#print(sorted(dados['Idade'].unique()))
#print(sorted(dados['Cor'].unique()))

#print(dados.Idade.max())

#print('De %s até %s anos' % (dados.Idade.min(), dados.Idade.max()))

#print('De %s até %s metros' % (dados['Altura'].min(), dados.Altura.max()))



frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize = True) * 100
dist_freq_qualitativas = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem (%)': percentual})
dist_freq_qualitativas.rename(index = {0: 'Masculino', 1: 'Feminio'}, inplace = True)
dist_freq_qualitativas.rename_axis('Sexo', axis='columns', inplace = True)


sexo = {0: 'Masculino',
        1: 'Feminino'}

cor = {0: 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8: 'Parda',
        9: 'Sem declaração'}

#print(dist_freq_qualitativas)

frequencia = pd.crosstab(dados.Sexo, dados.Cor)
frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)

#percentual = pd.crosstab(dados.Sexo, dados.Cor, normalize = True)*100
#percentual.rename(index = sexo, inplace = True)
#percentual.rename(columns = cor, inplace = True)

percentual = pd.crosstab(dados.Sexo, dados.Cor, aggfunc = 'mean', values = dados.Renda)
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)

dados.Renda.min()
dados.Renda.max()

classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E','D','C','B','A']

frequencia = pd.value_counts(pd.cut(x = dados.Renda,
       bins = classes,
       labels = labels,
       include_lowest = True)
                )

percentual = pd.value_counts(pd.cut(x = dados.Renda,
       bins = classes,
       labels = labels,
       include_lowest = True),
        normalize = True
                             )

dist_freq_quantitativas_personalizadas = pd.DataFrame(
        {'Frequencia': frequencia, 'Porcentagem (%)': percentual}
)

#print(dist_freq_quantitativas_personalizadas.sort_index(ascending = False))
n = dados.shape[0]
k = 1 + (10/3) * np.log10(n)
k = int(k.round(0))

frequencia = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = k,
        include_lowest = True
    ),
    sort = False
)

percentual = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = k,
        include_lowest = True
    ),
    sort = False,
    normalize = True
)

dist_freq_quantitativas_amplitude_fixa = pd.DataFrame(
        {'Frequencia': frequencia, 'Porcentagem (%)': percentual}
)

print(dist_freq_quantitativas_amplitude_fixa)
#print(frequencia)
#print(percentual)


