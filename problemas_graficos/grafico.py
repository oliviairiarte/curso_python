
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\pedos.csv")

sns.lineplot(x='fecha', y='pedos', data=df)

plt.plot("Marzo",56,"o")
plt.show()
