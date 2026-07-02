# 🖼️ Results & Screenshots

## Model Performance

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | $71,956 | $134,143 | 0.8572 |
| Random Forest | $68,005 | $130,263 | 0.8653 |

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

<img width="595" height="664" alt="image" src="https://github.com/user-attachments/assets/a9caf701-ebff-4802-a425-04bef82e37eb" />
<img width="1183" height="732" alt="image" src="https://github.com/user-attachments/assets/22b9fff5-438a-4053-8725-ce635ef5562c" />

<img width="1784" height="610" alt="image" src="https://github.com/user-attachments/assets/667ec904-2587-4537-a421-4815daee2b4a" />

<img width="1760" height="664" alt="image" src="https://github.com/user-attachments/assets/df1560a7-6aa2-4c52-bb8d-5fa07f530ef2" />


<img width="1770" height="630" alt="image" src="https://github.com/user-attachments/assets/12cb4c10-7319-4b0f-8326-0088dde534db" />

<img width="1776" height="550" alt="image" src="https://github.com/user-attachments/assets/293e4d16-424f-4f7b-8c9d-b0f8af72aa39" />

<img width="1760" height="559" alt="image" src="https://github.com/user-attachments/assets/4a3050a8-a9a5-470e-b472-c614cb73585e" />
<img width="1686" height="492" alt="image" src="https://github.com/user-attachments/assets/7c13886f-18ac-4655-bc11-74893a81a31a" />



## Sanity Checks

Predictions were validated against real comparable houses in the dataset:

- A 3-bed / 2-bath / 1,800 sqft / 1-floor house near **lat 47.68, long -122.20** (North Seattle area) predicted ~$588k, consistent with the real median (~$508k–$615k range) for similar houses in that area.
- The same profile near a lower-priced King County area predicted a proportionally lower price, confirming the model responds correctly to location once `lat`/`long` are used instead of `zipcode`.

## Known Limitations

- Features not exposed in the app UI (e.g. `condition`, `grade`, `view`, `waterfront`) are filled with dataset-wide median/mode defaults, so predictions for houses that differ significantly from "typical" on those dimensions may be less accurate.
- The dataset only covers sales from May 2014–May 2015, so predictions reflect that period's market, not current King County prices.
