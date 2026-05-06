import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# 1. Ler o arquivo CSV
df = pd.read_csv("ecommerce_estatistica.csv")

# 2. Criar a aplicação
app = dash.Dash(__name__)

# 3. Criar alguns gráficos com colunas válidas
fig_marca = px.histogram(df, x="Marca", title="Distribuição por Marca")
fig_material = px.histogram(df, x="Material", title="Distribuição por Material")
fig_preco = px.scatter(df, x="Preço", y="Nota", title="Preço vs Nota")

# 4. Layout da aplicação
app.layout = html.Div(children=[
    html.H1("Dashboard E-commerce"),

    html.Div([
        html.H2("Distribuição por Marca"),
        dcc.Graph(figure=fig_marca)
    ]),

    html.Div([
        html.H2("Distribuição por Material"),
        dcc.Graph(figure=fig_material)
    ]),

    html.Div([
        html.H2("Relação entre Preço e Nota"),
        dcc.Graph(figure=fig_preco)
    ])
])

# 5. Rodar o servidor
if __name__ == "__main__":
    app.run(debug=True)

