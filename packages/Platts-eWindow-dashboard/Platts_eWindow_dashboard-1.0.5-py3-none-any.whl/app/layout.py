import dash
from dash import dcc, html

# Define the layout of the dashboard with dark mode
layout = html.Div([
    html.H3("Platts Data Dashboard", style={'color': 'white'}),  # White text for the title
    
    # Credentials input section
    html.Div([
        html.Div([
            dcc.Input(id='username', type='text', placeholder="Enter your SPGlobal username", 
                      style={'width': '250px', 'height': '30px', 'borderRadius': '5px', 'backgroundColor': '#333', 'color': 'white', 'border': '1px solid #555'}),
        ], style={'display': 'flex', 'alignItems': 'center', 'paddingRight': '10px'}),
        
        html.Div([
            dcc.Input(id='password', type='password', placeholder="Enter your SPGlobal password", 
                      style={'width': '250px', 'height': '30px', 'borderRadius': '5px', 'backgroundColor': '#333', 'color': 'white', 'border': '1px solid #555'}),
        ], style={'display': 'flex', 'alignItems': 'center', 'paddingRight': '10px'}),
        
        html.Div([
            html.Button('Login', id='login-button', n_clicks=0, 
                        style={'backgroundColor': '#007bff', 'color': 'white', 'border': 'none', 'borderRadius': '5px', 
                               'padding': '10px 20px', 'fontSize': '16px', 'cursor': 'pointer'}),
        ], style={'display': 'flex', 'alignItems': 'center'})
    ], style={'display': 'flex', 'alignItems': 'center', 'padding': '20px', 'border': '1px solid #555', 'borderRadius': '5px', 'backgroundColor': '#222'}),

    # Filters section with typeable dropdowns and date range
    html.Div([
        # Market filter
        html.Div([
            dcc.Dropdown(
                id='market-selector',
                options=[{'label': 'EU NSEA PVO', 'value': 'EU NSEA PVO'}, {'label': 'EU FO', 'value': 'EU FO'}],
                multi=True,
                placeholder="Type or Select Market",
                style={'width': '250px', 'backgroundColor': '#333', 'color': 'white', 'border': '1px solid #555'}
            ),
        ], style={'display': 'flex', 'alignItems': 'center', 'paddingRight': '10px'}),

        # Product filter
        html.Div([
            dcc.Dropdown(
                id='product-selector',
                options=[],
                multi=True,
                placeholder="Type or Select Product",
                style={'width': '250px', 'backgroundColor': '#333', 'color': 'white', 'border': '1px solid #555'}
            ),
        ], style={'display': 'flex', 'alignItems': 'center', 'paddingRight': '10px'}),

        # Hub filter
        html.Div([
            dcc.Dropdown(
                id='hub-selector',
                options=[],
                multi=True,
                placeholder="Type or Select Hub",
                style={'width': '250px', 'backgroundColor': '#333', 'color': 'white', 'border': '1px solid #555'}
            ),
        ], style={'display': 'flex', 'alignItems': 'center', 'paddingRight': '10px'}),

        # Date Range filter
        html.Div([
            dcc.DatePickerRange(
                id='date-range-picker',
                start_date_placeholder_text="Start Date",
                end_date_placeholder_text="End Date",
                display_format='YYYY-MM-DD',
                minimum_nights=0,
                style={'width': '350px', 'backgroundColor': '#333', 'color': 'white', 'borderRadius': '5px', 'border': '1px solid #555'}
            ),
        ], style={'display': 'flex', 'alignItems': 'center', 'paddingRight': '10px'}),

        # Load data button
        html.Div([
            html.Button('Load Data', id='load-data-button', n_clicks=0, 
                        style={'backgroundColor': '#28a745', 'color': 'white', 'border': '1px solid #555', 
                               'padding': '10px 20px', 'fontSize': '16px', 'borderRadius': '5px'}),
        ], style={'display': 'flex', 'alignItems': 'center'})  # Align with dropdowns
    ], style={'display': 'flex', 'alignItems': 'center', 'padding': '20px', 'border': '1px solid #555', 'borderRadius': '5px', 'backgroundColor': '#222', 'marginTop': '10px'}),

    # Price type selector
    html.Div([
        html.Label("Select Price Type", style={'color': 'white'}),
        dcc.RadioItems(
            id='price-type-selector',
            options=[
                {'label': 'Price', 'value': 'price'},
                {'label': 'C1 Price', 'value': 'c1_price'},
                {'label': 'C2 Price', 'value': 'c2_price'},
                {'label': 'C3 Price', 'value': 'c3_price'}
            ],
            value='price',  # Default selection
            labelStyle={'display': 'inline-block', 'marginRight': '10px', 'color': 'white'}
        ),
    ], style={'padding': '10px', 'border': '1px solid #555', 'borderRadius': '5px', 'backgroundColor': '#222', 'marginTop': '10px'}),

    # Maximized Graph for order evolution
    html.Div([
        dcc.Graph(id='order-graph', style={'width': '100%', 'height': '80vh'})  # Graph takes up 80% of the viewport height
    ], style={'padding': '20px', 'border': '1px solid #555', 'borderRadius': '5px', 'backgroundColor': '#222'})
], style={'backgroundColor': '#1f1f1f'})  # Dark background for the overall page
