from dash import Dash
import dash
import dash_core_components as dcc
import dash_html_components as html


class CustomDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        print(kwargs)
        return '''
        <!DOCTYPE html>
        <html style="background-color: blue;">

            <head>
                <title>Dash app</title>
            </head>
            <body>

                <div id="custom-header">fran header</div>
                {app_entry}
                {config}
                {scripts}
                <div id="custom-footer">fran footer</div>
            </body>
        </html>
        '''.format(
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'])

app = CustomDash()

app.layout = html.Div('Simple Dash App')

if __name__ == '__main__':
    app.run_server(debug=True)

