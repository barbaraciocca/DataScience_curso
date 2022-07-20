#necessário os passos das aulas anteriores, onde são importadas bibliotecas + arquivos csv
notas_ToyStory = notas.query('filmeId==1')
notas_Jumanji = notas.query('filmeId==2')
print(len(notas_ToyStory), len(notas_Jumanji))
# avaliando média dos dois filmes e arredondando nota em 2 casas decimais
print('nota média do Toy Story %.2f' % notas_ToyStory.nota.mean())
print('nota média do Jumanji %.2f' % notas_Jumanji.nota.mean())
# avaliando mediana dos dois filmes e arredondando nota em 2 casas decimais
print('nota média do Toy Story %.2f' % notas_ToyStory.nota.median())
print('nota média do Jumanji %.2f' % notas_Jumanji.nota.median())


# criando uma array
import numpy as np
filme1 = np.append(np.array([2.5]*10),np.array([3.5]*10))
filme2 = np.append(np.array([5]*10),np.array([1]*10))
print(filme1.mean(), filme2.mean())
print(np.median(filme1), np.median(filme2))
# gerando gráfico da distribuição dos filmes 1 e 2
sns.distplot(filme1)
sns.distplot(filme2)
# plotando apenas o histograma
plt.hist(filme1)
plt.hist(filme2)
# plotando de outra forma
plt.boxplot([filme1, filme2])
# plotando com sns dos filmes 1, 2, 3, 4 e 5
sns.boxplot(x='filmeId', y='nota', data = notas.query('filmeId in [1,2,3,4,5]'))
# calculo de desvio padrão com pd e np
print(notas_Jumanji.nota.std(), notas_ToyStory.nota.std())
print(np.std(filme1), np.std(filme2))