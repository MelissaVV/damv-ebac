

import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with sns.axes_style('whitegrid'):
  plt.figure(figsize=(6, 5))
  gasolina_df = pd.read_csv('./gasolina.csv')
  sns.lineplot(data=gasolina_df, x='dia', y='venda') # Use the DataFrame 'gasolina_df'
  plt.title('Preço Médio de gasolina nos 10 primeiros dias de Julho de 2021, em São Paulo') # Set title on plt object
  plt.xlabel('Dia') # Set xlabel on plt object
  plt.ylabel('Preço') # Set ylabel on plt object
  plt.savefig('gasolina.png')
