import dash
import dash_core_components as dcc
import dash_html_components as html

idx_str = dash.dash._default_index.replace("<html>", '<html style="background-color: lightblue;">')
app = dash.Dash(index_string=idx_str)

app.layout = html.Div('weed')

if __name__ == '__main__':
    app.run_server(debug=True)
