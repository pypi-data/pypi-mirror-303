from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from data.api_client import PlattsAPIClient  # Assuming the client is in data/api_client.py
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# This variable will store the client after login
client = None

# Mock data for market-product-hub relationships
MARKET_PRODUCT_MAPPING = {
    "EU NSEA PVO": ["Platts NSEA Ekofisk", "Platts NSEA WTI Midland", "Platts NSEA Forties", "Platts NSEA Johan Sverdrup", "Platts NSEA Brent/Ninian", "Platts NSEA Troll", "Platts NSEA Oseberg", "Platts NSEA Gullfaks", "Platts NSEA DUC", "Platts KEBCO Crg", "Platts NSEA Alvheim","Platts NSEA Asgard", "Platts NSEA Statfjord", "Platts STS NSEA Troll", "Platts STS NSEA Forties", "Platts STS NSEA Forties", "Platts STS NSEA Brent/Ninian", "Platts NSEA Grane Blend", "Platts STS NSEA Ekofisk"],
    "EU FO": ["Platts Marine Fuel", "Platts FO","Platts 0.1 DMA Brg 1-3kt ICE LSGO M1","Platts 0.1 DMA Brg 1-3kt FOB Brg" ]
}

PRODUCT_HUB_MAPPING = {
    "Platts Marine Fuel": ["0.5% Barge"],
    "Platts FO": ["Northwest Europe 3.5% Barge FOB Rotterdam", "Northwest Europe 1% Barge FOB Rotterdam", "3.5% RMK 500 CST Barge"],
    "Platts 0.1 DMA Brg 1-3kt ICE LSGO M1": ["ARA"],
    "Platts 0.1 DMA Brg 1-3kt FOB Brg":["ARA"],
    "Platts NSEA Ekofisk":["FOB Basis Teesside", "CIF Basis Rotterdam", "CFR Basis Rotterdam", "DES Basis Rotterdam"],
    "Platts NSEA WTI Midland":["CIF Basis Rotterdam"],
    "Platts NSEA Forties":["CIF Basis Rotterdam", "FOB Basis Hound Point", "CFR Basis Rotterdam", "DES Basis Rotterdam"],
    "Platts NSEA Johan Sverdrup":["CIF Basis Rotterdam", "FOB Basis Hound Point", "CFR Basis Rotterdam", "DES Basis Rotterdam"],
    "Platts NSEA Troll":["CIF Basis Rotterdam", "FOB Basis Hound Point", "CFR Basis Rotterdam", "DES Basis Rotterdam"],
    "Platts NSEA Oseberg":["CIF Basis Rotterdam", "FOB Basis Hound Point", "CFR Basis Rotterdam", "DES Basis Rotterdam"],
    
}

def register_callbacks(app):
    # Callback to handle user login
    @app.callback(
        [Output('login-button', 'children'),  # Change the text of the button
         Output('login-button', 'disabled'),  # Disable the button
         Output('login-button', 'style')],    # Change the style of the button
        Input('login-button', 'n_clicks'),
        State('username', 'value'),
        State('password', 'value')
    )
    def login_user(n_clicks, username, password):
        global client

        if n_clicks == 0:
            raise PreventUpdate

        if username and password:
            try:
                # Initialize the PlattsAPIClient with the user's credentials
                client = PlattsAPIClient(username=username, password=password)
                # After successful login, disable the button and change its style and text
                return ['Logged In', True, {
                    'backgroundColor': '#ccc', 'color': 'white', 'border': 'none', 'borderRadius': '5px', 
                    'padding': '10px 20px', 'fontSize': '16px', 'cursor': 'not-allowed'
                }]
            except Exception as e:
                print(f"Login failed: {e}")
                raise PreventUpdate
        else:
            raise PreventUpdate

    # Callback to update product options based on selected markets
    @app.callback(
        Output('product-selector', 'options'),
        Input('market-selector', 'value')
    )
    def update_products(selected_markets):
        if not selected_markets:
            raise PreventUpdate

        # Collect products associated with selected markets
        available_products = set()
        for market in selected_markets:
            if market in MARKET_PRODUCT_MAPPING:
                available_products.update(MARKET_PRODUCT_MAPPING[market])

        return [{'label': product, 'value': product} for product in available_products]

    # Callback to update hub options based on selected products
    @app.callback(
        Output('hub-selector', 'options'),
        Input('product-selector', 'value')
    )
    def update_hubs(selected_products):
        if not selected_products:
            raise PreventUpdate

        # Collect hubs associated with selected products
        available_hubs = set()
        for product in selected_products:
            if product in PRODUCT_HUB_MAPPING:
                available_hubs.update(PRODUCT_HUB_MAPPING[product])

        return [{'label': hub, 'value': hub} for hub in available_hubs]

    # Callback to load data based on category selections, date range, and price type
    @app.callback(
        [Output('order-graph', 'figure'),  # Output the figure for the graph
        Output('deal-table', 'data')],    # Output the data for the deal table
        [Input('load-data-button', 'n_clicks'),
        Input('price-type-selector', 'value')],
        [State('market-selector', 'value'),
        State('hub-selector', 'value'),
        State('product-selector', 'value'),
        State('date-range-picker', 'start_date'),
        State('date-range-picker', 'end_date')]
    )
    def load_data(n_clicks, selected_price_type, selected_market, selected_hub, selected_product, start_date, end_date):
        global client

        if n_clicks == 0:
            # Return an empty figure with a dark background before data is loaded
            fig = go.Figure()
            fig.update_layout(
                paper_bgcolor='#1f1f1f',  # Dark background
                plot_bgcolor='#1f1f1f',  # Dark background for the plot area
                font=dict(color='white'),  # White font for labels
                xaxis=dict(showgrid=True, gridcolor='#444', color='white', title_font=dict(color='white'), tickfont=dict(color='white')),  # White axes and gridlines
                yaxis=dict(showgrid=True, gridcolor='#444', color='white', title_font=dict(color='white'), tickfont=dict(color='white')),  # White axes and gridlines
                xaxis_title="Update Time",
                yaxis_title="Price",
                hovermode="closest",
                legend=dict(
                    orientation='h',  # Set legend to horizontal
                    yanchor="bottom",  # Anchor legend at the bottom
                    y=-0.5,  # Adjust to prevent overlap with the chart
                    xanchor="center",
                    x=0.5,
                    traceorder="grouped",  # Group by market maker in the legend
                    font=dict(size=10, color='white'),  # White font for the legend
                    title_text='Market Maker',
                    valign="middle"
                ),
            )
            return fig,[]

        if client is None:
            raise PreventUpdate

        # Build filters based on user selections from the dropdowns
        filters = []
        if selected_market:
            filters.append({'field': 'market', 'operator': 'IN', 'value': selected_market})
        if selected_hub:
            filters.append({'field': 'hub', 'operator': 'IN', 'value': selected_hub})
        if selected_product:
            filters.append({'field': 'product', 'operator': 'IN', 'value': selected_product})
        if start_date and end_date:
            # Apply date range filter using >= for start_date and <= for end_date
            filters.append({'field': 'order_date', 'operator': '>=', 'value': start_date})
            filters.append({'field': 'order_date', 'operator': '<=', 'value': end_date})

        try:
            # Fetch the filtered data with the date range applied
            df = client.fetch_ewindow_data(filters=filters)


            if df.empty:
                # Return an empty figure with dark mode
                return go.Figure(go.Scatter(x=[], y=[], mode='lines+markers')).update_layout(
                    paper_bgcolor='#1f1f1f',  # Dark background
                    plot_bgcolor='#1f1f1f',   # Dark background for the plot area
                    font=dict(color='white'),  # White font for labels
                    xaxis=dict(showgrid=True, gridcolor='#444', color='white', title_font=dict(color='white'), tickfont=dict(color='white')),  # White axes and gridlines
                    yaxis=dict(showgrid=True, gridcolor='#444', color='white', title_font=dict(color='white'), tickfont=dict(color='white')),  # White axes and gridlines
                    xaxis_title="Update Time",
                    yaxis_title="Price",
                    hovermode="closest",
                    legend=dict(
                        orientation='h',  
                        yanchor="bottom",
                        y=-0.5,  
                        xanchor="center",
                        x=0.5,
                        font=dict(size=10, color='white')
                    ),
                ), []

            
            # Ensure order_begin and order_end columns exist in the DataFrame
            if 'order_begin' not in df.columns or 'order_end' not in df.columns:
                raise Exception("order_begin or order_end columns not found in the data")


            # Filter deals where both buyer and seller are filled
            deals_df = df[(df['buyer'].notna()) & (df['seller'].notna()) & (df['buyer'] != '') & (df['seller'] != '')]

            # Sort data by 'order_platts_id' and 'update_time' to ensure correct plotting
            df = df.sort_values(by=['order_platts_id', 'update_time'])

            # Create a gap between data points from different days to prevent them from being connected
            df['update_date'] = pd.to_datetime(df['update_time']).dt.date
            df['gap_marker'] = df['update_date'].diff().ne(pd.Timedelta(0))  # Create a marker for gaps between days
            df.loc[df['gap_marker'], 'update_time'] = None  # Set gaps between days

            # Create new columns for symbol and size based on buyer and seller
            df['symbol'] = ['x-dot' if pd.notna(b) and pd.notna(s) and b.strip() != '' and s.strip() != '' else 'circle-open-dot'
                            for b, s in zip(df['buyer'], df['seller'])]
            df['size'] = [16 if pd.notna(b) and pd.notna(s) and b.strip() != '' and s.strip() != '' else 0
                          for b, s in zip(df['buyer'], df['seller'])]

            # Create a color map for each market_maker
            unique_market_makers = df['market_maker'].unique()
            color_scale = px.colors.qualitative.Plotly  # Use Plotly's default qualitative color scale
            color_map = {market_maker: color_scale[i % len(color_scale)] for i, market_maker in enumerate(unique_market_makers)}

            # Create the figure using go.Figure()
            fig = go.Figure()

            # Keep track of which market_maker has already been added to the legend
            legend_shown = {}

            # Plot each order separately but link them by market_maker for the legend
            for order_id in df['order_platts_id'].unique():
                df_order = df[df['order_platts_id'] == order_id]
                market_maker = df_order['market_maker'].iloc[0]  # Get the market maker for the order
                color = color_map[market_maker]  # Get the color for this market maker

                # Show the legend only for the first order for each market_maker
                show_legend = market_maker not in legend_shown
                legend_shown[market_maker] = True  # Mark the market maker as added to the legend
                print(df_order.head())
                # Plot individual orders, but group by market_maker for the legend
                fig.add_trace(go.Scatter(
                    x=df_order['update_time'],
                    y=df_order[selected_price_type],  # Use the selected price type dynamically
                    mode='lines+markers',  # Both lines and markers
                    name=f"{market_maker}",  # Use only the market_maker name for the legend
                    legendgroup=market_maker,  # Group all orders for this market_maker under the same legend
                    showlegend=show_legend,  # Show legend only for the first order of each market_maker
                    marker=dict(symbol=df_order['symbol'], size=df_order['size'], color=color),
                    line=dict(color=color, shape='hv'),  # Set line color based on market_maker
                    hoverinfo='text',
                    text=[f'''<b>{ot} from {mm}</b><br><b>{selected_price_type.replace("_", " ").capitalize()}:</b> {price}<br><b>Quantity:</b> {qty}<br><b>Product:</b> {pdt}<br><b>Hub:</b> {hub}<br><b>Strip:</b> {strip}<br><b>Laycan:</b> {ds} - {de}<br><b>Buyer:</b> {b if b else 'N/A'}<br><b>Seller:</b> {s if s else 'N/A'}<br><b>Order State:</b> {os}<br><b>Window State:</b> {ws}<br><b>Order Platts ID:</b> {order_id}<br><b>Update Time:</b> {ut}<br>'''
                    for mm, ut, price, qty, b, s, os, ws, strip, ot, ds, de,pdt,hub in zip(
                        df_order['market_maker'], 
                        df_order['update_time'], 
                        df_order[selected_price_type], 
                        df_order['order_quantity'], 
                        df_order['buyer'], 
                        df_order['seller'], 
                        df_order['order_state'], 
                        df_order['window_state'], 
                        df_order['strip'], 
                        df_order['order_type'], 
                        df_order['order_begin'], 
                        df_order['order_end'],
                        df_order['product'], 
                        df_order['hub'], 
                    )],
                     # Styling the hover label
                    hoverlabel=dict(
                        font_size=14,            # Increase font size
                        namelength=-1            # Show full name without truncating
                    )
                    ))
            fig.update_layout(dragmode='pan', xaxis_rangeslider_visible=True)

            # Update layout of the figure for dark mode
            fig.update_layout(
                paper_bgcolor='#1f1f1f',  # Dark background
                plot_bgcolor='#1f1f1f',  # Dark background for the plot area
                font=dict(color='white'),  # White font for labels
                xaxis=dict(showgrid=True, gridcolor='#444', color='white', title_font=dict(color='white'), tickfont=dict(color='white')),  # White axes and gridlines
                yaxis=dict(showgrid=True, gridcolor='#444', color='white', title_font=dict(color='white'), tickfont=dict(color='white')),  # White axes and gridlines
                xaxis_title="Update Time",
                yaxis_title=selected_price_type.replace('_', ' ').capitalize(),  # Dynamic y-axis label
                hovermode="closest",
                legend=dict(
                    orientation='h',  # Set legend to horizontal
                    yanchor="top",  # Anchor legend at the bottom
                    xanchor="center",
                    x=0.5,
                    traceorder="grouped",  # Group by market maker in the legend
                    font=dict(size=10, color='white'),  # White font for the legend
                    valign="middle"
                ),
            )
            clean_deals_df = clean_deals_data(deals_df)
            return fig, clean_deals_df.to_dict('records')
        
        except Exception as e:
            print(f"Error fetching data: {e}")
            return go.Figure(go.Scatter(x=[], y=[], mode='lines+markers', title="Error fetching data"))



# Clean data to ensure only valid types are passed to the DataTable
def clean_deals_data(deals_df):
    # Convert all non-stringable objects to strings
    for col in deals_df.columns:
        deals_df[col] = deals_df[col].apply(lambda x: str(x) if pd.notna(x) else "")
    return deals_df
