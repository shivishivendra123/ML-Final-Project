# 🚗 Predicting Serious Injury in Vehicle Collisions

## 🎯 Project Objective
To build a machine learning model that predicts whether a motor vehicle collision will result in a **serious outcome** (injury or fatality), enabling **proactive risk mitigation** and **resource planning** by the Department of Transportation (DOT).

---

## 📊 Dataset Summary
- **Source**: NYC Vehicle Collision Dataset
- **Size**: 2.1 million rows
- **Target**: `SERIOUS_CRASH` (1 = injury/fatality, 0 = non-serious)
- **Features Used**:
  - Time: `HOUR`, `DAY_OF_WEEK`, `IS_WEEKEND`, `IS_LATE_NIGHT`
  - Location: `BOROUGH_STREET_RISK`
  - Vehicle context: `IS_BIKE_INVOLVED`

---

## 🤖 Models Evaluated

### 1. Logistic Regression
       precision    recall  f1-score   support

       0       0.74      0.98      0.84    102926
       1       0.53      0.06      0.11     37789

accuracy                           0.73    140715







![image](https://github.com/user-attachments/assets/ef703e2c-6810-40e8-aa3d-c6e6748a5027)
