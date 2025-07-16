#Importar a biblioteca de gráficos
import matplotlib.pyplot as plt

#Dados para Gráficos
Celular = ['Iphone', 'Redmi', 'Samsung', 'Motorola']
Quantidade = [ 80 , 65 , 40, 19 ]

#Cria o gráfico de barras
plt.bar(Celular, Quantidade)

#Adiciona título e rótulos
plt.title("Celulares mais roubados")
plt.xlabel("Celular")
plt.ylabel("Quantidade")

#Mostra o gráfico na tela
plt.show()