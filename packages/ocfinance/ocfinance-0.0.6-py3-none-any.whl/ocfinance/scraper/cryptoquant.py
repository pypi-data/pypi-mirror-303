import json
from urllib.parse import urlparse
from seleniumbase import SB
import pandas as pd

CRYPTOQUANT_URL = "https://cryptoquant.com/"

def _download(url, **kwargs):
    splits = urlparse(url).path.split('/')
    id = splits[-1]

    # Cryptoquant's own metrics
    if splits[1] == 'asset':
        raise NotImplementedError("Only third party metrics on cryptoquant have been implemented.")

    email = kwargs.get('email')
    password = kwargs.get('password')
    if not email or not password:
        raise TypeError("Email and/or password hasn't been passed")
    data = _get_json(id, email, password)

    columns = data['data']['result']['columns']
    results = data['data']['result']['results']
    column_names = [col['name'] for col in columns]

    return _create_dataframe(results, column_names)

def _create_dataframe(results, column_names):
    df = pd.DataFrame(results, columns=column_names)
    
    date_column = None
    for col in df.columns:
        if col.lower() in ['day', 'date', 'datetime', 'transaction_day']:
            date_column = col
            break
    
    if date_column:
        df[date_column] = pd.to_datetime(df[date_column])
        df.set_index(date_column, inplace=True)
        df.index.name = 'Date'
    else:
        print("Unable to find and parse the date column")
    
    return df

def _get_json(id, email, password):
    with SB(uc=True) as sb:
        sb.uc_open_with_reconnect(CRYPTOQUANT_URL, 4)
        sb.uc_gui_click_captcha()

        response = sb.execute_async_script(f"""
            var callback = arguments[arguments.length - 1];
            
            fetch("https://live-api.cryptoquant.com/api/v1/sign-in", {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json'
                }},
                body: JSON.stringify({{
                    "email": "{email}",
                    "password": "{password}"
                }})
            }}).then(response => {{
                console.log('Response received:', response);
                return response.json();
            }})
            .then(data => {{
                console.log('Data parsed:', data);
                callback(data);
            }})
            .catch(err => {{
                console.log('Error occurred:', err);
                callback({{'error': err.toString()}});
            }});
        """)

        if 'accessToken' in response:
            access_token = response['accessToken']

            data_url = f"https://live-api.cryptoquant.com/api/v1/analytics/{id}"
            
            result = sb.execute_async_script(f"""
                var done = arguments[0];
                
                fetch("{data_url}", {{
                    method: 'GET',
                    headers: {{
                        'Authorization': 'Bearer {access_token}',
                        'Accept': 'application/json'
                    }}
                }}).then(response => response.text())
                .then(data => done(data))
                .catch(err => done({{'error': err.toString()}}));
            """)
        else:
            print(f"Error occurred: {response.get('error')}")
    
    return json.loads(result)
