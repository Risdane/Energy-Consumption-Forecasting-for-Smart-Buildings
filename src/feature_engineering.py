
def add_time_features(df):
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['is_weekend'] = (df['dayofweek'] >= 5).astype(int)
    df['month'] = df.index.month
    return df

def add_lag_features(df, lags=(1, 24)):
    for lag in lags:
        df[f'lag_{lag}'] = df['ENERGY'].shift(lag)
    return df

def add_rolling_features(df, window=24):
    df[f'rolling_mean_{window}'] = df['ENERGY'].rolling(window).mean()
    df[f'rolling_std_{window}'] = df['ENERGY'].rolling(window).std()
    return df

def prepare_hourly_features(df):
    df = add_time_features(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    return df.dropna()

def prepare_daily_features(df):
    daily = df.resample('D').agg({
        'ENERGY': 'sum',
        'T2M': 'mean',
        'RH2M': 'mean',
        'CDD10': 'sum',
        'HDD18_3': 'sum',
        'ALLSKY': 'mean',
        'HOLIDAY': 'max'
    })
    daily['dayofweek'] = daily.index.dayofweek
    daily['is_weekend'] = (daily['dayofweek'] >= 5).astype(int)
    daily['month'] = daily.index.month
    daily['lag_1'] = daily['ENERGY'].shift(1)
    daily['lag_7'] = daily['ENERGY'].shift(7)
    return daily.dropna()
