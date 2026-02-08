import pandas as pd
from sklearn.model_selection import train_test_split

class DataProcessor:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print(f"Dane wczytane. Kształt: {self.df.shape}")

    def clean_data(self):
        self.df = self.df.dropna()
        self.df = pd.get_dummies(self.df, columns=['ocean_proximity'])
        print("Czyszczenie zakończone.")

    def get_train_test_split(self, target_column, test_size=0.2):
        X = self.df.drop(target_column, axis=1)
        y = self.df[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)