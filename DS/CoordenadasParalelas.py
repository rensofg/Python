import plotly.express as px
import pandas as pd

# Definindo o conjunto de dados
data = pd.read_csv("wine.csv") 
atributos = ["Alcohol", "Malic_acid", "Ash", "Alcalinity_ash", "Total_phenols", "Flavanoids", "Nonflavanoid_phenols", "Color_intensity"]
atributos_dimensoes_pt = ["Álcool", "Ácido málico", "Cinzas", "Alcalinidade das cinzas", "Fenóis totais", "Flavonoides", "Fenóis não flavonoides"]

# Definindo os nomes dos atributos em português
nomes_atributos_pt = {
    "Alcohol": "Álcool",
    "Malic_acid": "Ácido málico",
    "Ash": "Cinzas",
    "Alcalinity_ash": "Alcalinidade das cinzas",
    "Total_phenols": "Fenóis totais",
    "Flavanoids": "Flavonoides",
    "Nonflavanoid_phenols": "Fenóis não flavonoides",
    "Color_intensity": "Intensidade da cor"}

# Traduzindo os nomes dos atributos para português
data = data.rename(columns=nomes_atributos_pt)

# Gerando o gráfico
fig = px.parallel_coordinates(data, color="Intensidade da cor", dimensions=atributos_dimensoes_pt)
# Exibindo o gráfico
fig.show()
