# 🖼️ Results & Screenshots

## Model Performance

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | $71,956 | $134,143 | 0.8572 |
| Random Forest | $68,005 | $130,263 | 0.8653 |
| Random Forest (Tuned via GridSearchCV/RandomizedSearchCV) | `[fill in your tuned results]` | `[fill in]` | `[fill in]` |

**Interpretation:**
- **R² ≈ 0.86** means the model explains about 86% of the variance in house prices — solid performance for this dataset, in line with typical results reported on King County housing data.
- **MAE ≈ $68,000** means predictions are off by about $68k on average, roughly 12–15% relative to King County's typical home price range.
- **Random Forest outperforms Linear Regression** across all three metrics, which is expected given non-linear relationships between price and features like location (`lat`/`long`) and `grade`.

## Feature Importance (Random Forest)

Top predictive features, by importance:

| Feature | Importance |
|---|---|
| `lat` | ~42% |
| `sqft_living` | ~32% |
| `grade` | ~8% |
| `long` | ~4% |
| `sqft_living15` | ~3% |
| `house_age` | ~2% |

Location (`lat`) and living area (`sqft_living`) together account for roughly 75% of the model's predictive power.

## App Screenshots

`[Add a screenshot of the main prediction panel — estimated price, input table]`

`[Add a screenshot of the location map + "Where your house lands" scatterplot]`

`[Add a screenshot of the factor-by-factor tabs (Bedrooms/Bathrooms/Floors/House Age)]`

`[Add a screenshot of the feature importance chart]`

## Sanity Checks

Predictions were validated against real comparable houses in the dataset:

- A 3-bed / 2-bath / 1,800 sqft / 1-floor house near **lat 47.68, long -122.20** (North Seattle area) predicted ~$588k, consistent with the real median (~$508k–$615k range) for similar houses in that area.
- The same profile near a lower-priced King County area predicted a proportionally lower price, confirming the model responds correctly to location once `lat`/`long` are used instead of `zipcode`.

## Known Limitations

- Features not exposed in the app UI (e.g. `condition`, `grade`, `view`, `waterfront`) are filled with dataset-wide median/mode defaults, so predictions for houses that differ significantly from "typical" on those dimensions may be less accurate.
- The dataset only covers sales from May 2014–May 2015, so predictions reflect that period's market, not current King County prices.
