# Predicting Serious Injury in Vehicle Collisions

## Project Objective
To build a machine learning model that predicts whether a motor vehicle collision will result in a **serious outcome** (injury or fatality), enabling **proactive risk mitigation** and **resource planning** by the Department of Transportation (DOT).

---

## Dataset Summary
- **Source**: NYC Vehicle Collision Dataset
- **Size**: 2.1 million rows
- **Target**: `SERIOUS_CRASH` (1 = injury/fatality, 0 = non-serious)
- **Features Used**:
  - Time: `HOUR`, `DAY_OF_WEEK`, `IS_WEEKEND`, `IS_LATE_NIGHT`
  - Location: `BOROUGH_STREET_RISK`
  - Vehicle context: `IS_BIKE_INVOLVED`

---

## Models Evaluated

### 1. Logistic Regression
       precision    recall  f1-score   support

       0       0.74      0.98      0.84    102926
       1       0.53      0.06      0.11     37789

accuracy                           0.73    140715

### 2. Random Forest Classifier
       precision    recall  f1-score   support

       0       0.75      0.80      0.78    102926
       1       0.35      0.29      0.32     37789

accuracy                           0.66    140715
   


### 3. LightGBM Classifier
       precision    recall  f1-score   support

       0       0.85      0.47      0.60    102926
       1       0.35      0.77      0.48     37789

accuracy                           0.55    140715


### 4. XGBoost Classifier
       precision    recall  f1-score   support

       0       0.818     0.585     0.682    102926
       1       0.364     0.646     0.465     37789

accuracy                           0.601    140715


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

## 🛠️ Use Cases for DOT

- ** Real-Time Triage**: Prioritize emergency response for high-risk crashes
- ** Hotspot Detection**: Use KMeans clustering to find streets needing design changes
- ** Policy Guidance**: Plan driver awareness campaigns and infrastructure improvements

---

## Conclusion

- The model helps identify serious crashes with good recall
- **XGBoost** offers the best balance of precision and recall
- Ready for integration with crash reporting tools, dashboards, or alert systems

---

## Next Steps

- Deploy via a real-time alert API or dashboard
- Host folium/pydeck crash maps
- Explore multi-label injury prediction (pedestrian vs cyclist vs motorist)
- Share insights with traffic engineers and city planners




![image](https://github.com/user-attachments/assets/ef703e2c-6810-40e8-aa3d-c6e6748a5027)
