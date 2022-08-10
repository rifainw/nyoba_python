import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row([
    dbc.Col(
        dbc.Input(
            type="search",placeholder="Search"
        )
    ),
    dbc.Col(
        dbc.Button(
            "Search",color="primary",className="ms-2",n_clicks=0
        ),
        width="auto"
    )
],className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",align="center")

navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(),
                dbc.Col()
            ])
        )
    ])
)