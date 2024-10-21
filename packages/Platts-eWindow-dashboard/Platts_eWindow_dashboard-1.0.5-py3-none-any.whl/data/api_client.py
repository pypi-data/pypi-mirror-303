import requests
import pandas as pd

class PlattsAPIClient:
    def __init__(self, username, password):
        """
        Initialize the client with the base URL and credentials for fetching the Bearer token.
        
        :param base_url: The base URL for the API.
        :param auth_url: The URL for the authentication endpoint.
        :param username: Your username for authentication.
        :param password: Your password for authentication.
        """
        self.base_url = 'https://api.ci.spglobal.com/tradedata'
        self.auth_url = 'https://api.ci.spglobal.com/auth/api'
        self.username = username
        self.password = password
        self.api_token = None  # This will be fetched via the auth call
        self.get_bearer_token()

    def get_bearer_token(self):
        """
        Authenticate and get the Bearer token using the provided username and password.
        
        :return: The Bearer token.
        """
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        data = {
            'username': self.username,
            'password': self.password
        }
        
        response = requests.post(self.auth_url, headers=headers, data=data)
        
        if response.status_code == 200:
            self.api_token = response.json().get('access_token')  # Adjust based on the actual response structure
            if not self.api_token:
                raise Exception("Failed to obtain Bearer token")
            return self.api_token
        else:
            raise Exception(f"Authentication failed: {response.status_code}, {response.text}")

    def get_headers(self):
        """
        Returns the headers required for API requests, including Authorization.
        """
        if not self.api_token:
            self.get_bearer_token()  # Automatically fetch the token if not already available
        return {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }

    def build_filters(self, filters, operator="AND"):
        """
        Build the Filter string based on a dictionary of field names, operands, and values.
        
        :param filters: A list of filter conditions where each condition is a dictionary with keys:
                        'field': The field name (e.g., 'market')
                        'operator': The operation (e.g., '=', 'IN', 'NOT IN', '>=', '<=', etc.)
                        'value': The value(s) for the field (e.g., 'Crude Oil', or ['Asia Bunker North', 'ASIA Bunker SG'])
        
        :param operator: Logical operator between filter conditions ('AND' or 'OR'). Default is 'AND'.
        
        :return: A string that represents the Filter query for the API.
        """
        filter_list = []
        
        for condition in filters:
            field = condition['field']
            op = condition['operator']
            value = condition['value']

            # Handle 'IN' and 'NOT IN' operators for lists of values
            if op == 'IN':
                value_str = ','.join([f'"{v}"' for v in value])
                filter_list.append(f'{field} IN ({value_str})')
            elif op == 'NOT IN':
                value_str = ','.join([f'"{v}"' for v in value])
                filter_list.append(f'{field} NOT IN ({value_str})')
            elif op == '=':
                filter_list.append(f'{field}:"{value}"')
            else:
                # For other operators like '>=', '<=', etc.
                filter_list.append(f'{field}{op}"{value}"')
        
        # Join all the conditions using the specified operator ('AND' or 'OR')
        return f' {operator} '.join(filter_list)

    def fetch_ewindow_data(self, field=None, query=None, filters=None, sort=None, page_size=1000, page=1):
        """
        Fetch eWindow trade data activity.
        
        :param field: Restrict response to specific fields (e.g., 'market')
        :param query: Filter by a keyword search expression (e.g., 'Brent Financial')
        :param filters: A dictionary where the key is the field name, and the value is a tuple (operand, value).
                        Example: {"order_date": ("=", "2020-10-31"), "price": (">", 100)}
        :param sort: Sort the API response (e.g., 'market:desc')
        :param page_size: Number of records per page (default is 100, max is 1000)
        :param page: Specific page number (default is 1)
        :return: The API response in JSON format.
        """
        endpoint = "/v3/ewindowdata"
        url = f"{self.base_url}{endpoint}"
        
        # Build the filter string if filters are provided
        filter_string = self.build_filters(filters) if filters else None
        print(filter_string)
        params = {
            'Field': field,
            'q': query,
            'Filter': filter_string,
            'Sort': sort,
            'PageSize': page_size,
            'Page': page
        }
        
        response = requests.get(url, headers=self.get_headers(), params=params)
        
        if response.status_code == 200:
            data = response.json()
            if 'results' in data and isinstance(data['results'], list):
                # Convert the list of results to a pandas DataFrame
                return pd.DataFrame(data['results'])
            else:
                raise ValueError("No results found or data format is not as expected")
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

    def fetch_metadata(self, field=None):
        """
        Fetch metadata for eWindow trade data fields.
        
        :param field: Restrict response to specific fields (optional)
        :return: The API response in JSON format.
        """
        endpoint = "/v3/ewindowdata/metadata"
        url = f"{self.base_url}{endpoint}"
        
        params = {
            'Field': field
        }
        
        response = requests.get(url, headers=self.get_headers(), params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch metadata: {response.status_code}, {response.text}")


# Example usage:
if __name__ == '__main__':
    username = ''  # Replace with your username
    password = ''  # Replace with your password

    # Initialize the client
    client = PlattsAPIClient(username, password)

    # Build filters for querying the API
    filters = [
        {
            'field': 'market',
            'operator': '=',
            'value': "EU NSEA PVO"
        },
        {
            'field': 'order_date',
            'operator': '>=',
            'value': '2024-10-17'
        }
    ]

    # Fetch eWindow trade data with filters
    try:
        data = client.fetch_ewindow_data(filters=filters, page_size=1000, page=1)
    except Exception as e:
        print(e)
