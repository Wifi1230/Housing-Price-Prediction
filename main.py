from src.processor import DataProcessor
from trainer import HousePriceModel
from sklearn.metrics import mean_squared_error
import numpy as np

def main():
    proc = DataProcessor()
    proc.load_from_mysql()
    proc.clean_data()

    model=HousePriceModel(proc)
    model.train()
    model.evaluate()

    y_train=model.y_train
    y_test=model.y_test

    baseline_pred = [y_train.mean()] * len(y_test)
    baseline_mse = mean_squared_error(y_test, baseline_pred)
    print(f"Baseline RMSE: {np.sqrt(baseline_mse):.2f}$")

    model.save_model()

if __name__ == "__main__":
    main()
