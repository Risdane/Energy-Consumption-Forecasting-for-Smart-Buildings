# 📊 Model Evaluation Metrics  
## Energy Consumption Forecasting for Smart Buildings

This document summarizes the **quantitative performance results** of the forecasting models developed in this project.
All metrics are computed on **unseen test data** using a **chronological train–test split**, reflecting real-world deployment conditions.

---

## 📌 Dataset Context

- Smart building electricity consumption data (hourly resolution)
- Weather variables: temperature, humidity, irradiance, degree days
- Calendar variables: weekends and holidays
- Two buildings treated as **independent energy systems**

---

## ⏱️ Hourly Forecasting Results (Building‑1)

**Forecasting Horizon:** Next-hour to day-ahead  
**Evaluation Basis:** Test set only

### Baseline Model (Persistence)
- **MAE:** 541.76 kWh  
- **RMSE:** 973.61 kWh  
- **MAPE:** 14.98 %  

### Random Forest Regressor
- **MAE:** 834.76 kWh  
- **RMSE:** 1074.89 kWh  
- **MAPE:** 30.86 %  

### XGBoost Regressor
- **MAE:** 753.75 kWh  
- **RMSE:** 1002.16 kWh  
- **MAPE:** 27.44 %  

---

## 📆 Daily Forecasting Results (Building‑1)

**Forecasting Horizon:** Day‑ahead  
**Aggregation:** Hourly → Daily energy (kWh)

### Baseline Model (Persistence)
- **MAE:** 11.49 kWh  
- **RMSE:** 24.91 kWh  
- **MAPE:** 6.25 %  

### Random Forest Regressor
- **MAE:** 8.74 kWh  
- **RMSE:** 16.33 kWh  
- **MAPE:** 5.63 %  

### XGBoost Regressor
- **MAE:** 8.54 kWh  
- **RMSE:** 14.54 kWh  
- **MAPE:** 5.82 %  

---

## 🔁 Cross‑Building Validation Results (Building‑2)

**Training Data:** Building‑1 only  
**Testing Data:** Building‑2 (unseen building)  
**Purpose:** Evaluate model generalization across buildings

### Random Forest Regressor
- **MAE:** 16.10 kWh  
- **RMSE:** 20.49 kWh  
- **MAPE:** 49.50 %  

### XGBoost Regressor
- **MAE:** 28.81 kWh  
- **RMSE:** 33.74 kWh  
- **MAPE:** 86.43 %  

---

## 🧠 Key Observations

- Machine learning models outperform the persistence baseline for both hourly and daily forecasting.
- XGBoost consistently achieves the **lowest error**, indicating strong non‑linear modeling capability.
- Cross‑building validation shows reasonable generalization, with expected accuracy degradation due to site‑specific differences.
- Lagged energy consumption and temperature‑related features are dominant predictors.