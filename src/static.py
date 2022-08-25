import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

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

def build_high_level():
    return html.Div(
        id="images",
        className="images",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Specs-tab",
                        label="High Level Images",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Sensor Output",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )

app.layout = html.Div(
    id="big-app-container",
    children=[
    build_banner(),
    dcc.Interval(
            id="interval-component",
            interval=2 * 1000,  # in milliseconds
            n_intervals=50,  # start at batch 50
            disabled=True,
        ),
        html.Div(
            id="app-container",
            children=[
                build_high_level(),
                html.Div(id="app-content"),
            ],
        ),
])

if __name__ == '__main__':
    app.run_server(debug=True)