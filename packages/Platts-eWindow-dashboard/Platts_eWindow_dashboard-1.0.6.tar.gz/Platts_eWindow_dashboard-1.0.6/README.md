# Platts eWindow Dashboard

**Platts eWindow Dashboard** is a Python-based Dash web application that allows you to visualize and analyze Platts eWindow data. The package provides an interactive dashboard where users can filter data by markets, products, and hubs, and dynamically update the data based on the selected date range.

## Features

- **Interactive Dashboard**: Visualize Platts eWindow data with filtering options for markets, products, hubs, and time ranges.
- **Dynamic Price Type Selection**: Choose between different price types (e.g., `price`, `c1_price`, `c2_price`, `c3_price`) and see changes on the fly.
- **Responsive Dark Mode**: The dashboard is styled with dark mode for a modern, user-friendly interface.
- **User Authentication**: Simply enter your SPGlobal credentials to access the data.

## Installation

To install the Platts eWindow Dashboard, you can use `pip`:

```bash
pip install Platts-eWindow-dashboard
```

Once installed, you can run the dashboard with the following command:

```bash
start-dashboard
```
Once the dashboard is running, open your browser and go to http://127.0.0.1:8050 to access the app.

## Requirements
Python 3.11+
SPGlobal Credentials (optional, if you have access to Platts data)

## Dependencies
The following Python packages are required and will be installed automatically with the package:

Dash: A Python framework for building analytical web applications.
Plotly: Used for interactive graphing and visualizations.
Pandas: Provides data manipulation and analysis tools.
Requests: Handles HTTP requests to the SPGlobal API.
If you want to manually install the dependencies, use:

```bash
pip install dash plotly pandas requests
```

## Authentication
To use the dashboard with live Platts eWindow data, you will need valid SPGlobal credentials. Enter your username and password in the provided fields on the dashboard’s login page.

## Example of Using Filters
Market Filter: Select one or more markets (e.g., EU NSEA PVO, EU FO).
Product Filter: The product list updates dynamically based on the selected market.
Hub Filter: Similar to products, hubs are filtered based on the selected product.
Date Range: Select the desired date range to display data.
Price Type: Choose between price, c1_price, c2_price, or c3_price to update the chart.

Project Structure
The project is organized as follows:

``` graphql
Copy code
your_project_name/
│
├── src/
│   ├── app/
│   │   ├── __init__.py       
│   │   ├── callbacks.py      # Callback functions for Dash interactivity
│   │   ├── dashboard.py      # Main entry point for starting the Dash app
│   │   ├── layout.py         # Layout and UI components for the app
│   ├── data/
│   │   ├── __init__.py       
│   │   ├── api_client.py     # Handles API requests and authentication with SPGlobal/Platts API
│
├── assets/                   # Custom CSS and JS for Dash (dark-theme.css)
│   ├── dark-theme.css        # Custom styles for dark mode #Not used
│
├── setup.py                  # Setup script for packaging and installation
├── requirements.txt          # List of dependencies (optional)
├── README.md                 # Project documentation (this file)
├── MANIFEST.in               # Ensures non-Python files are included in the package
```

## Development
### Running Locally
If you want to contribute or modify the project, you can run it locally with the following steps:

Clone the repository:

``` bash
git clone https://github.com/your-username/Platts-eWindow-dashboard.git
```
Navigate to the project directory:

```bash
cd Platts-eWindow-dashboard
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Run the dashboard locally:

```bash
python -m src.app.dashboard
```

### Customization
You can modify the layout, callbacks, or API client according to your needs by editing the respective files in the src/app and src/data directories.

### Contributing
Feel free to fork the repository and submit pull requests if you have any improvements or bug fixes. Contributions are welcome!

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any inquiries, feel free to contact me at magnum35puc@gmail.com.