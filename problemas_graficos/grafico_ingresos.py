
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\ingresos.csv")

sns.barplot(x="tipo", y="monto", data=df)
total = df["monto"].sum()
print(f"el total es de {total}")

plt.show()

# SNS.SCATTER PLOT  PARA GRAFICO DE DISPERSION (BUENO PARA IA Y PREDICCIONES)
# BOXPLOT PARA GRAFICOS DE BIGOTES
