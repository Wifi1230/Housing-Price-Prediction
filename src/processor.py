import pandas as pd
import mysql.connector
from sklearn.model_selection import train_test_split

class DataProcessor:
    def __init__(self):
        self.df = None

    def load_from_mysql(self):
        conn = mysql.connector.connect(
            host="db",
            user="sa",
            password="Tcejorp.v1",
            database="housing_db"
        )
        self.df = pd.read_sql("SELECT * FROM housing", conn)
        conn.close()
        print("Dane pobrane z bazy MySQL!")

    def clean_data(self):
        self.df = self.df.drop(columns=['ocean_proximity'], errors='ignore')
        self.df = self.df.dropna()

    def get_train_test_split(self, target_column):
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        return train_test_split(X, y, test_size=0.2, random_state=42)