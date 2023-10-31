# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import dash_daq as daq

app = Dash(__name__)
app.title = "Business CoPilot"


app.layout = html.Div([
    html.Div(
        [
            html.H1("AI Business CoPilot"),
            html.P("Your AI Business CoPilot, built by Catalyst Group Solutions"),
        ], 
        id='header-container'
    ),
    html.Div(
        [
            html.H1("Usage Statistics"),
            html.P("Usage of your CoPilot"),
        ],
        id='left-container'
    ),
    html.Div(
        [
            html.Div(
                [
                    html.H1("Build Your Own Advisor")
                ],
                id='advisor-container'
            ),
            html.Div(
                [
                    html.H2("Personality"),
                    html.P("Describe the personality of your CoPilot"),
                    dcc.Input(id="personality-name", type="text", placeholder="Name your CoPilot"),
                    dcc.Textarea(
                        id='personality-description',
                        value='Share all responses as though you are Yoda',
                        style={'width': '100%'}
                    ),
                    html.Button("Save Personality", id="save-personality-button", n_clicks=0)
                ],
                id='personality-container'
            ),
            html.Div(
                [
                    html.H2("Question"),
                    html.P("Enter a query for your CoPilot"),
                    dcc.Textarea(
                        id='prompt-value',
                        value='Tell me your life story',
                        style={'width': '100%'}
                    )
                ],
                id='prompt-container'
            ),
            html.Button("Generate Response", id="generate-button", n_clicks=0),
        ],
        id='right-container'
    )
])

if __name__ == '__main__':
    app.run(debug=True)
