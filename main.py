from src.processor import DataProcessor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def main():
    proc = DataProcessor()
    
    proc.load_from_mysql()
    proc.clean_data()
    
    X_train, X_test, y_train, y_test = proc.get_train_test_split(target_column='median_house_value')
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model wytrenowany na danych z MySQL! Błąd MSE: {mse:.2f}")

if __name__ == "__main__":
    main()