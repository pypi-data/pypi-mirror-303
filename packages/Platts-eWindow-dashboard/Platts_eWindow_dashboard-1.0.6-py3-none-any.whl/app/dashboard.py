import dash
from .layout import layout  # Import the layout from layout.py
from .callbacks import register_callbacks  # Import the callbacks from callbacks.py

def main():
    app = dash.Dash(__name__, external_stylesheets=['https://bootswatch.com/4/darkly/bootstrap.min.css'])
    app.layout = layout
    register_callbacks(app)
    app.run_server(debug=True)

if __name__ == "__main__":
    main()
