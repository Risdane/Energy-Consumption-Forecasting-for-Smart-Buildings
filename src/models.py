
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def random_forest():
    return RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42
    )

def xgboost():
    return XGBRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=6,
        objective='reg:squarederror',
        random_state=42
    )
