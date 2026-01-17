
import pandas as pd

def load_raw_data(filepath):
    df = pd.read_csv(filepath)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp').set_index('timestamp')
    return df

def clean_time_series(df):
    df = df.interpolate(method='time')
    return df.dropna()
