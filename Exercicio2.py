#Importar a biblioteca de gráficos
import matplotlib.pyplot as plt

#Dados para Gráficos
Frutas = ['Maçã', 'Abacaxi', 'Uva', 'Pera', 'Goiaba']
Quantidade = [ 80 , 65 , 40, 19 , 38 ]

#Cria o gráfico de barras
plt.bar(Frutas, Quantidade)

#Adiciona título e rótulos
plt.title("Frutas mais consumidas")
plt.xlabel("Frutas")
plt.ylabel("Quantidade")

#Mostra o gráfico na tela
plt.show()