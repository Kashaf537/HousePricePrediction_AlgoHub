import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

# Configure the page (title shown in browser tab, icon, and wide layout for more space)
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")

# --- Load the trained model and supporting files (saved earlier from the notebook) ---
# model: the trained Random Forest model
# model_features: exact list/order of columns the model expects as input
# feature_defaults: median/mode values for every feature, used to fill in
#                    anything the user doesn't manually input
model = joblib.load('house_price_model.pkl')
model_features = joblib.load('model_features.pkl')
feature_defaults = joblib.load('feature_defaults.pkl')

# Small sample dataset used only for drawing charts (not used for prediction)
data = pd.read_csv('house_data_for_viz.csv')

# --- Page title and short description ---
st.title("🏠 House Price Predictor")
st.caption("Estimate a house's price based on its key features.")

# --- Sidebar: user inputs ---
# lat/long are used instead of zipcode because the model relies almost
# entirely on lat/long to understand location (zipcode barely matters
# to the model, even though it seems like it should) — confirmed via
# feature_importances_.
st.sidebar.header("🔧 House Details")
bedrooms = st.sidebar.number_input("Bedrooms", min_value=1, max_value=15, value=3, step=1)
bathrooms = st.sidebar.number_input("Bathrooms", min_value=1.0, max_value=10.0, value=2.0, step=0.25)
sqft_living = st.sidebar.number_input("Living Area (sqft)", min_value=200, max_value=15000, value=1800, step=50)
floors = st.sidebar.number_input("Floors", min_value=1.0, max_value=4.0, value=1.0, step=0.5)
house_age = st.sidebar.number_input("House Age (years)", min_value=0, max_value=150, value=20, step=1)

st.sidebar.subheader("📍 Location")
st.sidebar.caption("King County spans roughly lat 47.16–47.78, long -122.52 to -121.32")
lat = st.sidebar.number_input("Latitude", min_value=47.10, max_value=47.85, value=47.55, step=0.01, format="%.4f")
long = st.sidebar.number_input("Longitude", min_value=-122.60, max_value=-121.20, value=-122.15, step=0.01, format="%.4f")

# --- Build a single row of input data for the model ---
# Step 1: start with ALL features set to their default (median/mode) value.
#         This ensures the input row has every column the model expects,
#         even ones the user never touches (like grade, condition, view, etc.)
input_df = pd.DataFrame([feature_defaults])[model_features]

# Step 2: overwrite the features the user actually controls
input_df.at[0, 'bedrooms'] = bedrooms
input_df.at[0, 'bathrooms'] = bathrooms
input_df.at[0, 'sqft_living'] = sqft_living
input_df.at[0, 'floors'] = floors
input_df.at[0, 'house_age'] = house_age
input_df.at[0, 'lat'] = lat
input_df.at[0, 'long'] = long

# --- Make the prediction ---
# The model was trained on log(price), not raw price, because price
# is right-skewed (a few very expensive houses distort the scale).
# So we predict in "log space" first, then convert back to real dollars.
prediction_log = model.predict(input_df)[0]
prediction = np.expm1(prediction_log)   # expm1 reverses the earlier log1p() transform

# --- Display the prediction and a summary of user inputs ---
col1, col2 = st.columns([1, 2])  # split the page into a narrow and a wide column

with col1:
    st.metric("💰 Estimated Price", f"${prediction:,.0f}")
    st.write("**Your inputs:**")
    st.dataframe(
        pd.DataFrame({
            'Feature': ['Bedrooms', 'Bathrooms', 'Living Area', 'Floors', 'House Age', 'Latitude', 'Longitude'],
            'Value': [bedrooms, bathrooms, f"{sqft_living} sqft", floors, f"{house_age} yrs", lat, long]
        }),
        hide_index=True
    )

with col2:
    # Map showing exactly where the entered coordinates fall
    st.subheader("📍 Selected Location")
    fig_map = px.scatter_mapbox(
        pd.DataFrame({'lat': [lat], 'lon': [long]}),
        lat='lat', lon='lon',
        zoom=9, height=400,
        mapbox_style="open-street-map"
    )
    fig_map.update_traces(marker=dict(size=14, color='red'))
    st.plotly_chart(fig_map, use_container_width=True)

st.divider()

col3, col4 = st.columns(2)

with col3:
    # Scatterplot of real houses (living area vs price), with the user's
    # predicted house marked as a red star so they can see where it lands
    st.subheader("Where your house lands")
    fig = px.scatter(
        data, x='sqft_living', y='price',
        opacity=0.25,
        labels={'sqft_living': 'Living Area (sqft)', 'price': 'Price ($)'},
        title="Living Area vs Price"
    )
    fig.add_trace(go.Scatter(
        x=[sqft_living], y=[prediction],
        mode='markers',
        marker=dict(color='red', size=16, symbol='star'),
        name='Your house'
    ))
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True)

with col4:
    # Scatterplot of real houses by latitude, colored by price —
    # shows how strongly location (north/south in King County) drives price
    st.subheader("Price by Latitude")
    fig = px.scatter(
        data, x='lat', y='price',
        opacity=0.25, color='price', color_continuous_scale='Viridis',
        labels={'lat': 'Latitude', 'price': 'Price ($)'},
        title="Latitude vs Price"
    )
    fig.add_vline(x=lat, line_dash="dash", line_color="red", annotation_text="Your input")
    fig.update_layout(height=420, coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- Charts showing how price varies with each individual factor ---
st.subheader("📊 How each factor affects price")

tab1, tab2, tab3, tab4 = st.tabs(["🛏️ Bedrooms", "🛁 Bathrooms", "🏢 Floors", "🕰️ House Age"])

with tab1:
    fig = px.box(data, x='bedrooms', y='price', color='bedrooms',
                 labels={'bedrooms': 'Bedrooms', 'price': 'Price ($)'}, title="Price by Number of Bedrooms")
    fig.update_layout(showlegend=False, height=420)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.box(data, x='bathrooms', y='price', color='bathrooms',
                 labels={'bathrooms': 'Bathrooms', 'price': 'Price ($)'}, title="Price by Number of Bathrooms")
    fig.update_layout(showlegend=False, height=420)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    fig = px.box(data, x='floors', y='price', color='floors',
                 labels={'floors': 'Floors', 'price': 'Price ($)'}, title="Price by Floors")
    fig.update_layout(showlegend=False, height=420)
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    fig = px.scatter(data, x='house_age', y='price', opacity=0.2,
                      trendline="ols", trendline_color_override="red",
                      labels={'house_age': 'House Age (years)', 'price': 'Price ($)'},
                      title="Price vs House Age (with trend line)")
    fig.add_vline(x=house_age, line_dash="dash", line_color="green",
                   annotation_text="Your input", annotation_position="top")
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- Feature importance chart ---
st.subheader("🔍 Which factor matters most?")

importances = pd.Series(model.feature_importances_, index=model_features)
key_features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'house_age', 'lat', 'long']
simple_importances = importances[key_features]
simple_importances = simple_importances.sort_values(ascending=True).reset_index()
simple_importances.columns = ['Feature', 'Importance']

fig = px.bar(simple_importances, x='Importance', y='Feature', orientation='h',
             color='Importance', color_continuous_scale='teal', title="Feature Importance")
fig.update_layout(height=350, coloraxis_showscale=False)
st.plotly_chart(fig, use_container_width=True)

st.caption("Note: grade, condition, and other unlisted factors are still set to typical/default values behind the scenes.")