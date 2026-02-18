from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

class HousePriceModel():
    def __init__(self,processor):
        self.processor=processor
        self.pipeline= Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ])
        
    def train(self):
        self.X_train, self.X_test, self.y_train, self.y_test = self.processor.get_train_test_split(
        target_column='median_house_value'
    )
        self.pipeline.fit(self.X_train, self.y_train)

    def evaluate(self):
        trained_model = self.pipeline.named_steps['model']
        print(f"Intercept: {trained_model.intercept_:.2f}")

        for feature, coef in zip(self.X_train.columns, trained_model.coef_):
            print(f"Cecha: {feature:20} | Waga: {coef:.4f}")

        predictions = self.pipeline.predict(self.X_test)
        mse = mean_squared_error(self.y_test, predictions)

        print(f"RMSE modelu: {np.sqrt(mse):.2f}$")
        print(f"R2 score: {r2_score(self.y_test, predictions):.3f}")