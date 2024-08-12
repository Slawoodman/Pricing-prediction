import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, StackingRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline


def prepare_data(df):
    """
    Prepare features and target variable from the DataFrame.

    Parameters:
    df (pd.DataFrame): Input DataFrame with housing data.

    Returns:
    X (pd.DataFrame): Feature matrix.
    y (pd.Series): Target vector.
    """


    df = pd.get_dummies(df, drop_first=True)
    X = df[
        [
            "OverallQual",
            "YearBuilt",
            "TotalBsmtSF",
            "GrLivArea",
            "GarageCars",
            "FullBath",
            "Fireplaces",
            "YearRemodAdd",
            "LotArea",
        ]
    ]
    y = df["SalePrice"]
    return X, y


def scale_features(X_train, X_test):
    """
    Scale features using StandardScaler.

    Parameters:
    X_train (pd.DataFrame): Training feature matrix.
    X_test (pd.DataFrame): Test feature matrix.

    Returns:
    X_train_scaled (np.ndarray): Scaled training feature matrix.
    X_test_scaled (np.ndarray): Scaled test feature matrix.
    """


    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled


def train_and_save_model(X_train_scaled, y_train):
    """
    Training a model using a pipeline and save it to a file.

    Parameters:
    X_train_scaled (np.ndarray): Scaled training feature matrix.
    y_train (pd.Series): Training target vector.
    """


    rf_model = RandomForestRegressor(random_state=42)
    rf_params = {
        "n_estimators": [100, 200, 300],
        "max_depth": [10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    }
    rf_grid_search = GridSearchCV(
        estimator=rf_model,
        param_grid=rf_params,
        cv=5,
        n_jobs=-1,
        scoring="neg_mean_squared_error",
    )
    rf_grid_search.fit(X_train_scaled, y_train)
    best_rf_model = rf_grid_search.best_estimator_

    # Stacking Regressor
    poly = PolynomialFeatures(degree=2)
    k_best = SelectKBest(score_func=f_regression, k=10)
    estimators = [("rf", best_rf_model)]
    stacked_model = StackingRegressor(estimators=estimators, final_estimator=Ridge())

    # Pipeline with Feature Engineering
    pipeline = Pipeline(
        [("poly", poly), ("k_best", k_best), ("stacked_model", stacked_model)]
    )

    model_dir = "server/model"
    model_path = os.path.join(model_dir, "house_prices_model.pkl")
    os.makedirs(model_dir, exist_ok=True)

    pipeline.fit(X_train_scaled, y_train)
    joblib.dump(pipeline, model_path)


def main(df):
    X, y = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    train_and_save_model(X_train_scaled, y_train)
