#Importar a biblioteca de gráficos
import matplotlib.pyplot as plt

#Dados para Gráficos
categorias = ['Python', 'JavaScript', 'Java']
quantidade = [ 80 , 65 , 40]

#Cria o gráfico de barras
plt.bar(categorias, quantidade)

#Adiciona título e rótulos
plt.title("Linguagens mais usadas")
plt.xlabel("Linguagem")
plt.ylabel("Quantidade")

#Mostra o gráfico na tela
plt.show()