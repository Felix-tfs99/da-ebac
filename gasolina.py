# código de geração do gráfico 
import pandas as pd
import matplotlib.pyplot as plt

gasolina = pd.read_csv('gasolina.csv')
plt.plot(gasolina['venda'])
plt.savefig("gasolina.png")