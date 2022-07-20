import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tmdb = pd.read_csv('tmdb_5000_movies.csv')
# Avaliando a lingua original de cada filme
print(tmdb.original_language.unique())
# visualizar cada nota única
print(tmdb.vote_average.unique())
# Contar quantas vezes aparece cada lingua
print(tmdb.original_language.value_counts())
# Transformar em um data frame
print(tmdb.original_language.value_counts().to_frame())
# datafrmae onde o meu indice (linguas) se trasforma em coluna
print(tmdb.original_language.value_counts().to_frame().reset_index())
contagem_de_lingua = tmdb.original_language.value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ['original_language','total']
print(contagem_de_lingua.head())
# gráfico de barra, tenho que dizer o que quero em x e y
sns.barplot(x = 'original_language', y = 'total', data = contagem_de_lingua)
# gráfico onde não preciso trabalhar com os dados como no anterior
sns.catplot(x='original_language', kind='count', data = tmdb)
# gráfico de pizza (apenas para conhecimento)
plt.pie(contagem_de_lingua['total'], labels = contagem_de_lingua['original_language'])
# maneira melhor de demonstrar que o inglês é mais utilizado que as outras linguas
total_por_lingua = tmdb['original_language'].value_counts()
total_geral = total_por_lingua.sum()
# o loc serve para localizar as linhas que tenham o valor en
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles
# criaçao de biblioteca 
dados = {
    'lingua' : ['ingles','outros'],
    'total' : [total_de_ingles, total_do_resto]
}
# criaçao de df (subescreveu a variavel)
dados = pd.DataFrame(dados)
print(dados)
# grafico final
sns.barplot(x='lingua', y ='total', data = dados)
# avaliando as demais linguas e excluindo o ingles
filmes_sem_lingua_original_em_ingles = tmdb.query("original_language !='en'")
# fazendo a contagem dos filmes em linguas diferentes do ingles
total_por_lingua_de_outros_filmes = tmdb.query("original_language !='en'").original_language.value_counts()
# grafico dos filmes sem ingles/alteração do tamanho da base
sns.catplot(x='original_language', kind='count', data = filmes_sem_lingua_original_em_ingles, aspect=2)
# ajustando o grafico de lingua que mais apareceu para a que menos apareceu usando a contagem feita antes e selecionando o indice
sns.catplot(x='original_language', kind='count', data = filmes_sem_lingua_original_em_ingles,aspect =2, order = total_por_lingua_de_outros_filmes.index)
# seaborn palette -> para escolher/alterar a cor do gráfico
sns.catplot(x='original_language', kind='count', data = filmes_sem_lingua_original_em_ingles,aspect =2,palette="GnBu_d", order = total_por_lingua_de_outros_filmes.index)