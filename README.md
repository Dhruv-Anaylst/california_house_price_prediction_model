# 🏠 California House Price Prediction Model

## 📌 Overview

This project is a **Machine Learning model** designed to predict median house prices in California districts based on demographic, geographic, and economic features. It uses the **California Housing dataset** (from the `sklearn.datasets` module) and applies data preprocessing, exploratory data analysis (EDA), and regression modeling techniques to generate accurate predictions.

## 🎯 Objectives

* Perform **data cleaning** and **exploratory data analysis**
* Visualize housing patterns and correlations
* Train and evaluate predictive models
* Compare multiple regression algorithms to find the best-performing one

## 📂 Dataset

* **Source**: [Scikit-learn California Housing dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)
* **Features**:

  * `MedInc`: Median income in block group
  * `HouseAge`: Median house age in block group
  * `AveRooms`: Average number of rooms per household
  * `AveBedrms`: Average number of bedrooms per household
  * `Population`: Block group population
  * `AveOccup`: Average number of household members
  * `Latitude`: Block group latitude
  * `Longitude`: Block group longitude
* **Target**: `MedHouseVal` — Median house value (in \$100,000s)

## 🛠 Tech Stack

* **Programming Language**: Python 🐍
* **Libraries**:

  * `pandas` & `numpy` → Data manipulation
  * `matplotlib` & `seaborn` → Data visualization
  * `scikit-learn` → Model training and evaluation

## 🔍 Workflow

1. **Data Loading & Cleaning**

   * Load dataset
   * Handle missing or inconsistent values (if any)
2. **Exploratory Data Analysis (EDA)**

   * Visualize distributions, correlations, and trends
3. **Feature Engineering**

   * Normalize/scale data
   * Create meaningful features if needed
4. **Model Training**

   * Train multiple regression models (Linear Regression, Decision Tree, Random Forest, etc.)
5. **Model Evaluation**

   * Compare performance using **MAE**, **MSE**, **RMSE**, and **R² score**
6. **Prediction**

   * Predict house values for unseen data

## 📊 Results

* Best model achieved: **Random Forest Regressor** with high R² score and low RMSE
* Strong correlation observed between **median income** and **house value**

## 📦 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/your-username/california_house_price_prediction_model.git

# Navigate to the project directory
cd california_house_price_prediction_model

# Install dependencies
pip install -r requirements.txt

# Run the script
python california_house_price_prediction.py
```

## 📌 Example Output

```
Predicted Median House Value: $245,000
```

## 📅 Future Improvements

* Add **hyperparameter tuning** for better accuracy
* Deploy the model using **Streamlit** or **Flask** for interactive predictions
* Integrate with real-time California housing market data

## 🤝 Contributing

Contributions are welcome!

* Fork the repo
* Create a new branch
* Commit changes
* Open a Pull Request

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

