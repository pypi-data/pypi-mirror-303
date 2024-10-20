import pandas as pd

def process_historical_data(data, interval):
    """Process raw historical data into a pandas DataFrame.

    Args:
        data (list): Raw data from the API.
        interval (str): Data interval to determine if cutoff time should be applied.

    Returns:
        pandas.DataFrame: Processed historical data.
    """
    df = pd.DataFrame(data)
    df.columns = ['Status', 'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s', utc=True)
    df['Timestamp'] = df['Timestamp'].dt.tz_localize(None)
    df = df[['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']]

    # Apply cutoff time only for intraday intervals
    intraday_intervals = ['1m', '3m', '5m', '10m', '15m', '30m', '1h']
    if interval in intraday_intervals:
        cutoff_time = pd.Timestamp('15:29:59').time()
        df = df[df['Timestamp'].dt.time <= cutoff_time]

    df.set_index('Timestamp', inplace=True)
    return df