
# 🚗 Used Car Selling Price Prediction

### End-to-End Machine Learning | Regression | Gradient Boosting

## 📌 Project Overview

This project develops a machine learning model to predict **used car selling prices** based on vehicle characteristics such as age, mileage, fuel type, transmission, engine capacity, and other relevant features.

The objective is to provide a **data-driven reference price** that can help buyers, sellers, and automotive businesses estimate used car values more consistently.

Multiple regression algorithms were evaluated, and a **Gradient Boosting Regressor** was selected as the final model based on its predictive performance and generalization ability.

## 🎯 Project Objectives

- Explore and analyze factors influencing used car selling prices.
- Perform data cleaning, feature engineering, and preprocessing.
- Develop and compare multiple machine learning regression models.
- Evaluate model performance using MAE, RMSE, and R² Score.
- Optimize the selected model using hyperparameter tuning.
- Build a reusable prediction pipeline for inference on unseen data.

## 📊 Dataset

**Source:** [Car Price Prediction Dataset - Kaggle](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset)

The dataset contains used car information, including:

- **Year:** Vehicle manufacturing year
- **Selling Price:** Used car selling price (target variable)
- **KM Driven:** Total distance traveled
- **Fuel:** Fuel type
- **Seller Type:** Seller category
- **Transmission:** Manual or automatic
- **Owner:** Previous ownership information
- **Mileage:** Vehicle fuel efficiency
- **Engine:** Engine capacity
- **Max Power:** Maximum engine power
- **Seats:** Number of seats

The target variable is `selling_price`, measured in Indian Rupees (₹).

## 🔍 Exploratory Data Analysis

Several insights were identified during EDA:

1. **Selling Price Distribution**
   - Selling prices are right-skewed, with some expensive vehicles creating extreme values.

2. **Vehicle Age**
   - Newer vehicles generally have higher selling prices, while older vehicles tend to depreciate.

3. **Fuel Type**
   - Diesel vehicles generally show higher selling prices than petrol vehicles in the dataset.

4. **Transmission**
   - Automatic vehicles tend to have higher selling prices than manual vehicles.

5. **Outliers**
   - Several numerical features contain outliers, requiring appropriate preprocessing techniques.

## ⚙️ Data Preprocessing

The preprocessing workflow includes:

### Data Cleaning
- Removed duplicate observations.
- Handled missing values.
- Converted numerical features stored as text into appropriate data types.

### Feature Engineering
- Created `car_age` based on the vehicle manufacturing year.
- Extracted the car brand from the vehicle name.

### Feature Selection
- Analyzed feature relationships using Spearman and Kendall correlations.
- Retained relevant numerical and categorical features for modeling.

### Preprocessing Pipeline

**Numerical Features**
- `SimpleImputer(strategy='median')`
- `RobustScaler`

**Categorical Features**
- `SimpleImputer(strategy='most_frequent')`
- `OneHotEncoder(handle_unknown='ignore')`

The transformations were combined using `ColumnTransformer` to ensure consistent preprocessing.

The dataset was divided into:
- **80% Training Data**
- **20% Testing Data**

## 🤖 Machine Learning Models

Several regression algorithms were developed and evaluated:

1. Linear Regression
2. Ridge Regression
3. K-Nearest Neighbors (KNN)
4. Support Vector Regression (SVR)
5. Decision Tree Regressor
6. Random Forest Regressor
7. Gradient Boosting Regressor

### Model Selection

Although Random Forest achieved a lower training error, it showed a larger performance gap between training and testing data.

Gradient Boosting demonstrated more consistent performance and was selected for further optimization.

## 🔧 Hyperparameter Tuning

Hyperparameter tuning was performed using `RandomizedSearchCV` with:

- **15 randomly selected hyperparameter combinations**
- **5-Fold Cross-Validation**
- **R² Score** as the optimization metric

### Best Hyperparameters

| Hyperparameter | Best Value |
|---|---|
| `n_estimators` | 300 |
| `learning_rate` | 0.1 |
| `subsample` | 0.8 |

**Best Cross-Validation R² Score: 0.9017**

This indicates strong predictive performance across the cross-validation folds.

## 📈 Model Evaluation

The final Gradient Boosting model was evaluated before and after hyperparameter tuning.

| Metric | Before Tuning | After Tuning |
|---|---:|---:|
| Train MAE | 80,374 | 64,882 |
| Test MAE | 82,902 | 74,831 |
| Train RMSE | 127,032 | 94,619 |
| Test RMSE | 132,159 | 124,454 |
| Train R² | 0.9429 | 0.9683 |
| Test R² | 0.9204 | 0.9294 |

### Key Findings

- **Test MAE decreased**, indicating more accurate predictions on average.
- **Test RMSE decreased**, demonstrating better control of large prediction errors.
- **Test R² increased from 0.9204 to 0.9294**, indicating improved predictive performance.
- The train-test R² gap increased from approximately 0.0226 to 0.0390, suggesting a greater tendency toward overfitting.

Despite the increased performance gap, the tuned Gradient Boosting model was selected as the final model because it achieved better results on unseen test data.

## 💡 Business Implications

The model can support used car pricing decisions by providing an initial estimated selling price based on vehicle characteristics.

**Potential applications:**
- Assisting sellers in setting competitive prices.
- Helping buyers evaluate whether a vehicle is reasonably priced.
- Supporting automotive businesses with data-driven price estimates.
- Improving consistency in preliminary vehicle valuations.

However, predictions should be treated as **reference prices**, not definitive market valuations.

## ⚠️ Model Limitations

- Some observations still produce relatively large prediction errors.
- Hyperparameter tuning increases the train-test performance gap.
- Important factors such as vehicle physical condition, accident history, service history, location, and current market demand are not included in the dataset.
- Predictions may be less reliable for vehicles that differ substantially from the training data.

## 🚀 Future Improvements

- Incorporate additional vehicle condition and market-related features.
- Explore alternative regression algorithms and ensemble techniques.
- Further reduce overfitting through model optimization.
- Evaluate model performance on more recent market data.
- Monitor prediction accuracy as vehicle prices change over time.

## 🛠️ Tech Stack

**Programming Language**
- Python

**Data Processing**
- Pandas
- NumPy

**Data Visualization**
- Matplotlib
- Seaborn

**Machine Learning**
- Scikit-learn

**Development Tools**
- Jupyter Notebook
- Visual Studio Code
- Git & GitHub

## 🔮 Model Inference

The final trained model is saved and can be used to predict selling prices for new vehicle data.

Example:

```python
prediction = model.predict(data_inf_final)

print(
    f'Predicted Selling Price: '
    f'₹{prediction[0]:,.2f}'
)
```

Example output:

```text
Predicted Selling Price: ₹650,000.00
```

*Note: The example is illustrative. Actual predictions depend on the vehicle characteristics.*

## 🏁 Conclusion

This project successfully developed an end-to-end machine learning solution for predicting used car selling prices.

The tuned **Gradient Boosting Regressor** achieved:

- **Test R² Score: 0.9294**
- **Test MAE: ₹74,831**
- **Test RMSE: ₹124,454**

The results demonstrate that machine learning can provide useful and relatively consistent used car price estimates.

The final model can serve as a foundation for a practical automotive price estimation system, with opportunities for further improvement through additional features and market data.




