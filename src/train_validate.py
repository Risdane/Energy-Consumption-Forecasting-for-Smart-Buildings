
def time_series_split(df, target='ENERGY', test_ratio=0.2):
    split_idx = int(len(df) * (1 - test_ratio))
    X = df.drop(columns=[target])
    y = df[target]
    return (
        X.iloc[:split_idx], X.iloc[split_idx:],
        y.iloc[:split_idx], y.iloc[split_idx:]
    )
