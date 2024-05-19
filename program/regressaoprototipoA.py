import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dados medidos da tensão do aparelho de infravermelho
tensao = np.array([2.12, 2.19, 2.19, 2.15, 2.08, 2.09, 1.96, 1.72, 1.96, 1.93, 1.61, 1.86, 1.88, 1.72, 2.06, 1.76, 1.89, 1.98, 1.82, 1.86, 1.97, 1.56, 1.75, 2.05])  # Substitua t1, t2, t3 pelos valores medidos

# Dados da glicose medida pelo aparelho invasivo
glicose = np.array([116, 89, 235, 178, 253, 294, 96, 291, 63, 75, 337, 313, 200, 242, 51, 206, 159, 327, 384, 276, 234, 245, 102, 215])  # Substitua g1, g2, g3 pelos valores medidos

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
plt.title('Regressão Linear: Protótipo A')

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
plt.show()

print("Equação da reta: glicose = {:.2f} * tensão + {:.2f}".format(coef_angular, intercepto))

# Calculando o coeficiente de determinação (R²)
r_squared = modelo.score(tensao, glicose)
print("Coeficiente de Determinação (R²):", r_squared)
