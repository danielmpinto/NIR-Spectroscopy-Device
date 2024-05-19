import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dados medidos da tensão do aparelho de infravermelho
tensao = np.array([0.73, 0.723333, 0.93, 0.69, 0.7, 0.716667, 0.663333, 0.646667, 0.69, 0.536667, 0.496667, 0.486667, 0.496667, 0.533333])  # Substitua t1, t2, t3 pelos valores medidos

# Dados da glicose medida pelo aparelho invasivo
glicose = np.array([120, 117, 155, 92, 115,126, 106, 102, 121, 117, 114, 108, 106, 114])  # Substitua g1, g2, g3 pelos valores medidos

# Reshape dos dados para o formato necessário para a regressão linear
tensao = tensao.reshape(-1, 1)

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo
modelo.fit(tensao, glicose)

# Coeficientes da regressão
coef_angular = modelo.coef_[0]
intercepto = modelo.intercept_

# Plotando os dados e a reta de regressão
plt.scatter(tensao, glicose, color='blue', label='Dados Medidos')
plt.plot(tensao, modelo.predict(tensao), color='red', label='Regressão Linear')

# Adicionando rótulos e título ao gráfico
plt.xlabel('Tensão do Aparelho de Infravermelho')
plt.ylabel('Glicose medida pelo Aparelho Invasivo')
plt.title('Regressão Linear: Protótipo B')

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
plt.show()

print("Equação da reta: glicose = {:.2f} * tensão + {:.2f}".format(coef_angular, intercepto))