# 📊 Dataset Information

## Source

**House Sales in King County, USA**
Kaggle: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction

## Overview

- **Rows:** ~21,600 house sale records
- **Columns:** 21 original features
- **Time period:** Homes sold between May 2014 and May 2015
- **Location:** King County, Washington, USA (includes Seattle)

## Original Columns

| Column | Description |
|---|---|
| `id` | Unique identifier for each sale (dropped during cleaning — not predictive) |
| `date` | Date the house was sold |
| `price` | Sale price (target variable) |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `sqft_living` | Living area in square feet |
| `sqft_lot` | Lot size in square feet |
| `floors` | Number of floors |
| `waterfront` | Whether the property has a waterfront view (0/1) |
| `view` | Quality of the view (0–4) |
| `condition` | Overall condition rating (1–5) |
| `grade` | Overall grade based on King County grading system |
| `sqft_above` | Square footage of house apart from basement |
| `sqft_basement` | Square footage of the basement |
| `yr_built` | Year the house was built |
| `yr_renovated` | Year of last renovation (0 if never renovated) |
| `zipcode` | ZIP code |
| `lat` | Latitude |
| `long` | Longitude |
| `sqft_living15` | Living area of the 15 nearest neighbors |
| `sqft_lot15` | Lot size of the 15 nearest neighbors |

## Engineered Features

Created during the feature engineering step:

| Feature | Description |
|---|---|
| `sale_year`, `sale_month` | Extracted from `date` |
| `house_age` | `sale_year - yr_built` |
| `was_renovated` | Binary flag: 1 if `yr_renovated > 0` |
| `total_rooms` | `bedrooms + bathrooms` |
| `living_lot_ratio` | `sqft_living / sqft_lot` |
| `has_basement` | Binary flag: 1 if `sqft_basement > 0` |
| `log_price` | `log1p(price)` — used as the regression target to reduce right-skew |

## Data Quality Notes

- No missing values were present in the raw dataset.
- Duplicate `id`s exist (some houses sold more than once in the 2014–2015 window) — both sales are kept as independent rows.
- A small number of rows had unrealistic `bedrooms` values (e.g. 33) and were removed.
- Extreme outliers in `sqft_lot` were capped using the IQR method (3×IQR upper bound).

## Why `lat`/`long` instead of `zipcode` for location in the app

During modeling, feature importance analysis showed `lat` alone carries roughly **42% importance** in the trained Random Forest, while all 69 one-hot encoded `zipcode_*` columns **combined** only account for about **1.2%**. This is why the deployed app lets users input latitude/longitude directly rather than selecting a zipcode — it reflects what the model actually relies on for location signal.
