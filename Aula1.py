import pandas as pd
notas = pd.read_csv('ratings.csv')
# Renomeando colunas para português
notas.columns = ["usuarioId","filmeId","nota","momento"]
# Imprimir a tabela
print(notas)
# Mostrar as 5 primeiras notas
print(notas.head())
# Saber quantas linhas e colunas eu tenho na tabela
print(notas.shape)
# Ver todos os valores da coluna nota
print(notas['nota'])
# Quais valores estão na coluna nota
print(notas['nota'].unique())
# Contar quantas vezes cada nota apareceu (aparece do mais frequente para o menos)
print(notas['nota'].value_counts())
# Calcular a média de todas as notas
print('Média:', notas['nota'].mean())
# Outra forma de falar sobre a coluna nota
print(notas.nota)
# Calcular a mediana das notas
print('Mediana:',notas.nota.median())
# Histograma de frequencia de notas
notas.nota.plot(kind = 'hist')
# Medidas de descrição dos dados da coluna nota
print(notas.nota.describe())
# Visualizar as medidas de descrição em sns (seaborn)
import seaborn as sns
sns.boxplot(notas.nota)