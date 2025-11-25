import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Conectar ao banco de dados
conn = sqlite3.connect('/home/ubuntu/analiseenergiaiotforbess/data/processed/dados_processados.db')
df = pd.read_sql_query("SELECT * FROM dados_processados", conn)
conn.close()

# Criar diretório para imagens
import os
os.makedirs('/home/ubuntu/analiseenergiaiotforbess/notebooks/images', exist_ok=True)

# 1. Distribuição do Consumo de Energia
plt.figure(figsize=(10, 6))
sns.histplot(df['Energia (kWh)'], bins=30, kde=True)
plt.title('Distribuição do Consumo de Energia (kWh)')
plt.xlabel('Energia (kWh)')
plt.ylabel('Frequência')
plt.savefig('/home/ubuntu/analiseenergiaiotforbess/notebooks/images/distribuicao_energia.png')
plt.close()

# 2. Consumo de Energia ao longo do tempo (dia_criacao)
plt.figure(figsize=(12, 6))
df.groupby('dia_criacao')['Energia (kWh)'].mean().plot(kind='line', marker='o')
plt.title('Consumo Médio de Energia por Dia de Criação')
plt.xlabel('Dia de Criação')
plt.ylabel('Consumo Médio de Energia (kWh)')
plt.grid(True)
plt.savefig('/home/ubuntu/analiseenergiaiotforbess/notebooks/images/consumo_energia_por_dia.png')
plt.close()

# 3. Consumo de Energia por Aviário
plt.figure(figsize=(12, 7))
sns.boxplot(x='aviario', y='Energia (kWh)', data=df, palette='viridis')
plt.title('Consumo de Energia por Aviário')
plt.xlabel('Aviário')
plt.ylabel('Energia (kWh)')
plt.savefig('/home/ubuntu/analiseenergiaiotforbess/notebooks/images/consumo_energia_por_aviario.png')
plt.close()

# 4. Heatmap de Correlação
plt.figure(figsize=(14, 10))
# Selecionar apenas colunas numéricas para correlação
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap de Correlação entre Variáveis Numéricas')
plt.savefig('/home/ubuntu/analiseenergiaiotforbess/notebooks/images/heatmap_correlacao.png')
plt.close()

# 5. Consumo de Energia vs. Peso
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Peso (g)', y='Energia (kWh)', data=df, alpha=0.5)
plt.title('Consumo de Energia (kWh) vs. Peso das Aves (g)')
plt.xlabel('Peso (g)')
plt.ylabel('Energia (kWh)')
plt.grid(True)
plt.savefig('/home/ubuntu/analiseenergiaiotforbess/notebooks/images/energia_vs_peso.png')
plt.close()

# 6. Consumo de Energia por Metro Quadrado
df['kwh_por_m2'] = df['Energia (kWh)'] / df['metros_quadrados']
plt.figure(figsize=(12, 7))
sns.boxplot(x='aviario', y='kwh_por_m2', data=df, palette='plasma')
plt.title('Consumo de Energia por Metro Quadrado (kWh/m²) por Aviário')
plt.xlabel('Aviário')
plt.ylabel('Energia (kWh/m²)')
plt.savefig('/home/ubuntu/analiseenergiaiotforbess/notebooks/images/consumo_energia_por_m2.png')
plt.close()

print('Gráficos gerados e salvos com sucesso!')
