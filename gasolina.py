
# código de geração do gráfico
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with sns.axes_style('whitegrid'):
  plt.figure(figsize=(6, 5))
  gasolina_df = pd.read_csv('./gasolina.csv') #criando df
  sns.lineplot(data=gasolina_df, x='dia', y='venda') #DataFrame 'gasolina_df'
  plt.title('Atualizado: Preço Médio de gasolina nos 10 primeiros dias de Julho de 2021, em São Paulo') # Set title on plt object
  plt.xlabel('Dia atualizado') #entitulando
  plt.ylabel('Preço atualizado') #entitulando
  plt.savefig('gasolina.png')
  plt.show()
  
