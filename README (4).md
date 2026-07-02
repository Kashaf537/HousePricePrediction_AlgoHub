# 🏠 House Price Prediction System

A machine learning project that predicts house prices using regression techniques, built as part of the **AlgoHub Software House** Internship Program (Week 1 — Beginner Track).

Repo: https://github.com/Kashaf537/HousePricePrediction_AlgoHub
Live Demo: `https://housepricepredictionalgoappgit-gqyhjgbuss6unket689zvw.streamlit.app/`
Demo Video: `[Add your video link here]`

📄 See also: [Dataset Information](DATASET.md) • [Installation Guide](INSTALLATION.md) • [Results & Screenshots](RESULTS.md)

---

## 📌 Project Overview

This project predicts residential house prices based on features like living area, number of bedrooms/bathrooms, floors, house age, and location (latitude/longitude). It covers the full ML workflow — data cleaning, feature engineering, model training, evaluation, and deployment as an interactive web app.

**Objective:** Predict house prices using regression techniques.

**Key Concepts Covered:**
- Data Cleaning
- Feature Engineering
- Regression Modeling
- Model Evaluation & Hyperparameter Tuning
- Deployment with Streamlit

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.10 |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn |
| Model Persistence | Joblib |
| Deployment | Streamlit |

---

## 🧹 Workflow

1. **Data Cleaning**
   - Handled duplicate records and invalid entries (e.g. unrealistic bedroom counts)
   - Outlier treatment using the IQR method on `sqft_lot`
   - Parsed and engineered date-based features

2. **Feature Engineering**
   - `house_age` — derived from sale year and year built
   - `was_renovated` — binary flag from `yr_renovated`
   - `total_rooms`, `living_lot_ratio`, `has_basement`
   - Location represented via `lat`/`long` (found to carry far more predictive signal than one-hot encoded `zipcode` — see Future Improvements)

3. **Modeling**
   - **Linear Regression** (baseline)
   - **Random Forest Regressor**
   - Hyperparameter tuning on Random Forest via `GridSearchCV` / `RandomizedSearchCV`
   - Target variable (`price`) log-transformed (`log1p`) to reduce skew; predictions inverse-transformed (`expm1`) for evaluation

4. **Evaluation**
   Full metrics table and comparison charts are in [RESULTS.md](RESULTS.md).

5. **Deployment**
   - Interactive **Streamlit** web app (`housepred_app.py`)
   - Users input key features (bedrooms, bathrooms, living area, floors, house age, latitude, longitude)
   - Real-time price prediction with a live map of the selected location
   - Interactive Plotly visualizations showing how each factor affects price
   - Feature importance chart

---

## 📁 Project Structure

```
HousePricePrediction_AlgoHub/
│
├── kc_house_data.csv
├── house_price_prediction.ipynb
├── housepred_app.py
├── house_price_model.pkl
├── model_features.pkl
├── feature_defaults.pkl
├── house_data_for_viz.csv
├── requirements.txt
├── README.md
├── DATASET.md
├── INSTALLATION.md
├── RESULTS.md
├── .gitignore
└── AlgoHub_Task1_HousePricePrediction.zip
```

---

## 🚀 Future Improvements

- Add Gradient Boosting / XGBoost for comparison against Random Forest
- Add a FastAPI backend to separate the model-serving layer from the UI
- Expand hyperparameter search space and cross-validation folds
- Let users pick a named neighborhood (mapped internally to lat/long) instead of typing raw coordinates, for a friendlier UI

---

## 👤 Author

`[Your Name]`
Internship Project — AlgoHub Software House
`[LinkedIn / GitHub profile links]`

---

## 📄 License

This project is for educational purposes as part of the AlgoHub Software House Internship Program.
