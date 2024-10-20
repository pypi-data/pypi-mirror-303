import json
import pandas as pd
from seleniumbase import SB

def _download(url):
    data = _intercept_network_requests(url)
    traces = data['response']['chart']['figure']['data']
    dfs = _create_dataframes(traces)
    merged_df = pd.concat(dfs, axis=1, join='outer')
    return merged_df

def _create_dataframes(traces):
    dfs = []
    for trace in traces:
        # if 'customdata' in trace:
            name = trace['name']
            x = trace['x']
            y = trace['y']

            length = min(len(x), len(y))
            x = x[:length]
            y = y[:length]

            df = pd.DataFrame({ name: pd.to_numeric(y, errors='coerce') }, index=pd.to_datetime(pd.to_datetime(x, format='mixed').date))
            df = df[~df.index.duplicated(keep='first')]
            df.index.name = 'Date'
            dfs.append(df)

    return dfs

def _intercept_network_requests(url):
    with SB(uc=True) as sb:
        sb.uc_open_with_reconnect(url, 4)
        sb.uc_gui_click_captcha()

        sb.refresh()

        response = sb.execute_async_script("""
            var callback = arguments[arguments.length - 1];
            const originalFetch = window.fetch;

            window.fetch = function(...args) {
                return originalFetch.apply(this, args).then(response => {
                    const clonedResponse = response.clone();

                    clonedResponse.text().then(text => {
                        // Check if the last part of the URL is _dash-update-component
                        const urlParts = args[0].split('/');
                        const lastPart = urlParts[urlParts.length - 1];

                        if (lastPart === '_dash-update-component') {
                            callback(text);
                        }
                    });

                    return response;
                });
            };
        """)

        return json.loads(response)
