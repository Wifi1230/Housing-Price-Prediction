from src.processor import DataProcessor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

def main():
    proc = DataProcessor()
    proc.load_from_mysql()
    proc.clean_data()

    X_train, X_test, y_train, y_test = proc.get_train_test_split(
        target_column='median_house_value'
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    print(f"RMSE modelu: {np.sqrt(mse):.2f}$")

    baseline_pred = [y_train.mean()] * len(y_test)
    baseline_mse = mean_squared_error(y_test, baseline_pred)
    print(f"Baseline RMSE: {np.sqrt(baseline_mse):.2f}$")

    print(f"R2 score: {r2_score(y_test, predictions):.3f}")

if __name__ == "__main__":
    main()
