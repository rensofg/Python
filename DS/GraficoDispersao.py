import plotly.express as px
import pandas as pd

# Criando um DataFrame com os dados
df = pd.read_csv("wine.csv")

# Renomeando as colunas
df = df.rename(columns={
    "Alcohol": "Álcool",
    "Malic_acid": "Ácido málico",
    "Ash": "Cinzas",
    "Alcalinity_ash": "Alcalinidade das cinzas",
    "Total_phenols": "Fenóis totais",
    "Flavanoids": "Flavonoides",
    "Nonflavanoid_phenols": "Fenóis não flavonoides",
    "Color_intensity": "Intensidade da cor"})

# Gerando o gráfico de dispersão
fig = px.scatter(df, x="Ácido málico", y="Álcool", color="Intensidade da cor", size="Flavonoides",
                 labels={"Ácido málico": "Ácido málico (g/L)", "Álcool": "Álcool (% vol.)", 
                         "Intensidade da cor": "Intensidade da cor", "Flavonoides": "Flavonoides (mg/L)"})

# Exibindo o gráfico
fig.show()
