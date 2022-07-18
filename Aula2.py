import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
filmes = pd.read_csv('movies.csv')
filmes.columns = ['filmeId','titulo','genero']
notas = pd.read_csv('ratings.csv')
notas.columns = ["usuarioId","filmeId","nota","momento"]

# seleção da média das notas do filme na posição 1 da tabela de filmes
print(notas.query('filmeId==1').nota.mean())
# seleção da média das notas do filme na posição 2 da tabela de filmes
print(notas.query('filmeId==2').nota.mean())

# Todas as notas agrupadas pelo filme com a média das notas
medias_por_filme = notas.groupby('filmeId').mean()['nota']
# Visualizar histograma das medias por filme
medias_por_filme.plot(kind='hist')
sns.boxplot(medias_por_filme)
medias_por_filme.describe()
# Grafico da distribuição onde eu escolho quantas divisões vão ter
sns.distplot(medias_por_filme, bins=10)

# possível gerar os gráficos com pyplot
print(plt.hist(medias_por_filme))
# para colocar título no gráfico
plt.title('Histograma das médias dos filmes')