# Dynamic Price Prediction System: A/B Testing & Cannibalization Simulator

**Dynamic Pricing Intelligence • Portfolio Optimization • Market Simulation**

---

This repository provides a robust, transparent, and interactive framework for simulating price changes across multi-product assortments. It captures not only the direct effects of price changes on individual products but also their indirect effects—specifically demand cannibalization—within a product portfolio. Designed for rapid experimentation and safe pre-launch scenario planning, it supports both technical and business audiences.

---

## 🚩 Overview

In multi-SKU environments, individual price changes can shift demand across products, resulting in possible revenue gains (or losses) at the portfolio level. Live pricing experiments are costly and risky. This system enables simulation-based forecasting which helps teams:

- Estimate expected revenue uplift/decline from candidate price strategies.
- Visualize how demand redistributes among SKUs due to cannibalization.
- Test how changes in cross-elasticity assumptions affect results.
- Build intuition and supporting evidence before any real-world rollouts.

---

## 📦 Key Components

- **`main.py`**: Core pipeline – from demand model training, price grid simulation, to multi-SKU A/B testing with customizable cannibalization modeling.
- **`streamlit_app.py`**: Interactive Streamlit UI for scenario experiments, uploading custom datasets, and tweaking cross-elasticity settings.
- **`dataset_generation.py`**: Synthetic data generator creating realistic time-series sales data for demo and testing (`data/simulated_product_sales.csv`).
- **Sample Data**: Ready-to-use sample dataset within the repository.

---

## 📐 Core Functionality

### 1. Per-SKU Demand Model

- **Features**: Price, price ratio, discount_pct, competitor price delta, historical lags, rolling windows, seasonality, and more.
- **Model**: Out-of-the-box, runs XGBoost Regression per-SKU. Easily swap for alternate models.
- **Explainability**: SHAP integration for model transparency.

### 2. Price Simulation (Single-SKU)

- **Process**:
  - Simulate demand/revenue on a range of candidate prices (min → max).
  - Estimate price elasticity from simulated log-price/log-demand regression.
  - Identify revenue-maximizing price points per SKU.

- **Elasticity Calculation**:
  - Uses the slope of the log(price) vs. log(demand) line:\
    If demand = A * price^e → log(demand) = log(A) + e · log(price)

### 3. Multi-Product A/B Simulation & Cannibalization

- **Estimate Own-Price Elasticity**: Per-SKU historical sensitivity using log-log fits.
- **Cross-Elasticity Matrix**: Simple rules or user-uploaded matrices to govern cannibalization intensity across SKUs.
- **Portfolio Simulation**: For any candidate price changes, forecasts both:
  - Direct demand/revenue shifts
  - Indirect cannibalization effects (demand redistributed to/from related products)
- **A/B Comparison**: Simulate “holdout” vs. “test” scenarios and run paired t-tests on simulated revenue uplift.

---

## 📊 Data Requirements

Upload or generate a CSV with these columns:

| Column              | Type    | Description                                        |
|---------------------|---------|----------------------------------------------------|
| `date`              | string  | In YYYY-MM-DD format                               |
| `product_id`        | string  | Unique SKU/Item identifier                         |
| `price`             | float   | Actual selling price                               |
| `demand`            | int     | Units sold                                         |
| `base_price`        | float   | (optional) List price or standard price            |
| `competitor_price`  | float   | (optional) Best or average competitor price        |
| `discount_pct`      | float   | (optional) Discount relative to base price (%)     |
| `seasonality`       | float   | (optional) Time-based index                        |
| `true_elasticity`   | float   | (optional) Known elasticity(used in synthetic data)|

Use provided `dataset_generation.py` for a quickstart with reproducible demo data.

---

## ⚙️ How to Use

1. **Install requirements**  
   `pip install -r requirements.txt`

2. **Run Main Pipeline**  
   `python main.py`
   - Trains demand models, runs price/revenue simulations, outputs reports.

3. **Start Streamlit UI**  
   `streamlit run streamlit_app.py`
   - Try interactive scenario planning with real or synthetic datasets.

4. **Generate Synthetic Data** (optional)  
   `python dataset_generation.py`

---

## 💡 Why Use This Simulator?

- **Risk Reduction**: Vet price change ideas before live A/B rollout.
- **Portfolio Focus**: Capture cannibalization and substitution in complex SKU sets.
- **Customization**: Adjust cross-elasticity structure to reflect unique business/category dynamics.
- **Transparency**: Models are explainable and built on well-understood statistical principles.
- **Speed**: Go from data to insights in minutes.

---

## 📝 References & Inspirations

- ["Simulating Price Experiments for Portfolio Revenue Impact", notebook and blog series]  
- [SHAP: Explainable Machine Learning](https://shap.readthedocs.io/)
- ["Pricing and Revenue Optimization", Robert Phillips]
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 🛠️ Contributing

Pull requests, bug reports, and improvement suggestions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) if available.

---

## 📄 License

Distributed under the MIT license. See [LICENSE](LICENSE) for more info.

---
