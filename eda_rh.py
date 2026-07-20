import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importando os dados exportados
df_query1 = pd.read_csv('query_01.csv')

# 2. Análise Exploratória de Dados (EDA) - Estatísticas Básicas
print("--- Estatísticas Descritivas de Salários ---")
print(f"Média: {df_query1['SALARY'].mean():.2f}")
print(f"Mediana: {df_query1['SALARY'].median():.2f}")
print(f"Valor mínimo: {df_query1['SALARY'].min()}")
print(f"Valor máximo: {df_query1['SALARY'].max()}")

# 3. Criação de Gráfico (Boxplot)
plt.figure(figsize=(12, 6))
# Configurando o Boxplot relacionando o nome do departamento e o salário
sns.boxplot(data=df_query1, x='DEPARTMENT_NAME', y='SALARY')

# Ajustes visuais para facilitar a leitura
plt.title('Distribuição de Salários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário')
plt.xticks(rotation=45) # Inclina os nomes dos departamentos
plt.tight_layout()

# Exibe o gráfico
plt.show()