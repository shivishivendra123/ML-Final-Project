import streamlit as st
import pandas as pd
import pydeck as pdk
import time
import joblib

# Load your test data
X_test = pd.read_csv("/Users/shivendragupta/Desktop/ML Final Project/X_test_ingestion_.csv").rename(columns={"Unnamed: 0": "crash_id"})
X_crash = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes_20250430.csv")  # Must include 'LATITUDE', 'LONGITUDE'

# Load model
model = joblib.load("model.pkl")

# App title
st.set_page_config(layout="wide")
st.title("🚨 Real-Time Crash Reporting (Simulation)")

# Notification/alert placeholder at the very top
alert_placeholder = st.empty()

# Create layout: map on left (wider), serious crash list on right
col1, col2 = st.columns([3, 1])  # Increase map size by giving more weight

# Placeholders for dynamic content
placeholder_map = col1.empty()
placeholder_table = col1.empty()
serious_crashes_placeholder = col2.empty()

# Start button
if st.button("Start Reporting Crashes"):
    crash_points = []        # For map
    serious_crashes = []     # For serious crash list

    for index, row in X_test.iterrows():
        # Get full crash data
        row_crash = X_crash.iloc[row['crash_id']]
        lat = row_crash["LATITUDE"]
        lon = row_crash["LONGITUDE"]

        if pd.isna(lat) or pd.isna(lon):
            continue

        # Predict severity
        severity = model.predict(row.iloc[1:].values.reshape(1, -1))[0]

        # Show alert and record serious crash
        if severity == 1:
            alert_placeholder.error(
                f"🚨 Serious Crash Detected! Location: {row_crash['BOROUGH']} on {row_crash['ON STREET NAME']} ({lat:.4f}, {lon:.4f})"
            )
            serious_crashes.append({
                "borough": row_crash["BOROUGH"],
                "street": row_crash["ON STREET NAME"],
                "latitude": lat,
                "longitude": lon
            })
            serious_crashes_df = pd.DataFrame(serious_crashes)
            serious_crashes_placeholder.dataframe(serious_crashes_df)
        else:
            alert_placeholder.info("Monitoring for new serious crashes...")

        # Add crash to map points
        crash_points.append({
            "lat": lat,
            "lon": lon,
            "severity": "Serious Injury" if severity == 1 else "Not Serious",
            "color": [255, 0, 0] if severity == 1 else [0, 0, 255],
            "borough": row_crash["BOROUGH"],
            "street": row_crash["ON STREET NAME"]
        })

        df_points = pd.DataFrame(crash_points)

        # PyDeck Layer
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df_points,
            get_position='[lon, lat]',
            get_radius=200,
            get_fill_color='color',
            pickable=True
        )

        view_state = pdk.ViewState(latitude=40.75, longitude=-73.95, zoom=10)

        # Update visuals
        placeholder_map.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
        placeholder_table.dataframe(df_points)

        time.sleep(5)

    st.success("✅ All crash reports simulated!")
