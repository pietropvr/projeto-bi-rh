import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importando os dados exportados das DUAS queries
df_query1 = pd.read_csv('query_01.csv')
df_query2 = pd.read_csv('query_02.csv')

# 2. Análise Exploratória de Dados (EDA) - Estatísticas Básicas
print("--- Estatísticas Descritivas de Salários Globais ---")
print(f"Média: {df_query1['SALARY'].mean():.2f}")
print(f"Mediana: {df_query1['SALARY'].median():.2f}")
print(f"Valor mínimo: {df_query1['SALARY'].min()}")
print(f"Valor máximo: {df_query1['SALARY'].max()}")

# 3. Criação de Gráficos (Boxplots)

# Gráfico 1: Salários por Departamento (Query 1)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_query1, x='DEPARTMENT_NAME', y='SALARY')
plt.title('Distribuição de Salários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() 

# Gráfico 2: Salários por Região (Query 2)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_query2, x='REGION_NAME', y='SALARY')
plt.title('Distribuição de Salários por Região')
plt.xlabel('Região')
plt.ylabel('Salário')
plt.tight_layout()
plt.show()