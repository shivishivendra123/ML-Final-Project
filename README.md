# Predicting Serious Injury in Vehicle Collisions

## Project Objective

To build a machine learning model that predicts whether a motor vehicle collision will result in a serious outcome (injury or fatality), enabling proactive risk mitigation and resource planning by the Department of Transportation (DOT).

---

## Dataset Summary

- **Source**: NYC Vehicle Collision Dataset  
- **Size**: 2.1 million rows  
- **Target**: `SERIOUS_CRASH` (binary: 1 if injury or fatality occurred, 0 otherwise)  
- **Key Features Used**:
  - Time-related: `HOUR`, `DAY_OF_WEEK`, `IS_WEEKEND`, `IS_LATE_NIGHT`
  - Location: `BOROUGH_STREET_RISK`
  - Vehicle & crash data: `IS_BIKE_INVOLVED`, `CONTRIBUTING_FACTOR_VEHICLE_1`

---

## Models Evaluated

### 1. Logistic Regression

```
           precision    recall  f1-score   support

           0       0.74      0.98      0.84    102926
           1       0.53      0.06      0.11     37789

    accuracy                           0.73    140715
   macro avg       0.63      0.52      0.48    140715
weighted avg       0.68      0.73      0.65    140715
```

---

### 2. Random Forest Classifier

```
           precision    recall  f1-score   support

           0       0.75      0.80      0.78    102926
           1       0.35      0.29      0.32     37789

    accuracy                           0.66    140715
   macro avg       0.55      0.55      0.55    140715
weighted avg       0.65      0.66      0.65    140715
```

---

### 3. LightGBM Classifier

**Hyperparameters**:
```python
objective='binary',
n_estimators=350,
scale_pos_weight=3.5,
learning_rate=0.1,
random_state=42
```

**Classification Report**:
```
           precision    recall  f1-score   support

           0       0.85      0.47      0.60    102926
           1       0.35      0.77      0.48     37789

    accuracy                           0.55    140715
   macro avg       0.60      0.62      0.54    140715
weighted avg       0.71      0.55      0.57    140715
```

---

### 4. XGBoost Classifier

**Hyperparameters**:
```python
objective='binary:logistic',
scale_pos_weight=3,
n_estimators=300,
max_depth=10,
learning_rate=0.1,
use_label_encoder=False,
eval_metric='logloss',
random_state=42
```

**Classification Report**:
```
           precision    recall  f1-score   support

           0       0.818     0.585     0.682    102926
           1       0.364     0.646     0.465     37789

    accuracy                           0.601    140715
   macro avg      0.591     0.615     0.574    140715
weighted avg      0.696     0.601     0.624    140715
```

---

## Why These Metrics Are Acceptable

In this project:

- The data is **imbalanced** (non-serious crashes far outnumber serious ones)
- **Accuracy alone is misleading** — a model could achieve 73% accuracy by predicting all zeros
- Our focus is on **Recall for Class 1 (Serious Crashes)**:
  - XGBoost achieves **64.6% recall**, meaning it identifies **~2 out of 3 serious crashes**
- This helps **minimize missed high-risk cases**, which is critical for emergency response

Some loss in precision is acceptable in safety-critical applications — **it's better to over-alert than to miss real danger**.

---

## Key Findings

- **XGBoost outperforms LightGBM** in overall **F1-score** and **accuracy**, while still maintaining good recall for serious crashes (65%).
- **Recall is prioritized** over accuracy to ensure serious crashes are not missed.
- Engineered features like `IS_BIKE_INVOLVED`, `IS_LATE_NIGHT`, `BOROUGH_STREET_RISK`, `IS_WEEKEND`, `DAY_OF_WEEK`, and `CONTRIBUTING_FACTOR_VEHICLE_1` significantly helped improve model performance.

---

## Use Case for DOT

- **Real-time Crash Triage**: Flag high-risk crashes as they are reported for faster EMS dispatch.
- **Hotspot Analysis**: Use cluster detection (KMeans) to identify high-risk locations and improve road safety design.
- **Policy Impact**: Guide decisions around speed enforcement, lighting, and bike lane deployment.

---

## Conclusion

- The serious crash prediction model successfully identifies over 60% of serious crashes in real time.
- **XGBoost is recommended** for deployment due to better generalization and balanced performance.
- This model provides the DOT with a **data-driven, proactive tool** for reducing injuries and saving lives.

---

## Next Steps

- Integrate the model into real-time traffic systems  
- Visualize predictions on interactive maps using `folium`  
- Extend to multi-label injury prediction (pedestrian vs cyclist vs motorist)  
- Collaborate with city planners to deploy model insights on the ground  
