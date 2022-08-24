import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("MAV Operated Tunnel Inspection using Object-classification Neural Networks"),
                    html.H6("Software Tool for Analysis of Tunnel Inspected Cracks"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.A(
                        html.Button(children="EXPLORE M.O.T.I.O.N."),
                        href="https://github.com/NEU-Project-MOTION",
                    ),
                    html.A(
                        html.Img(id="logo", src=app.get_asset_url("husky.png")),
                        href="https://ece.northeastern.edu/",
                    ),
                ],
            ),
        ],
    )

app.layout = html.Div(
    id="big-app-container",
    children=[
    build_banner()
])

if __name__ == '__main__':
    app.run_server(debug=True)