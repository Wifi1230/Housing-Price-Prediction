import mysql.connector
import pandas as pd
import time
import numpy as np

def migrate_data():
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host="db",
                user="sa",
                password="Tcejorp.v1",
                database="housing_db"
            )
            cursor = conn.cursor()
            print("Połączono z bazą do migracji!")
            break
        except:
            print(f"Czekam na bazę... ({i+1}/10)")
            time.sleep(2)
    else:
        print("Nie udało się połączyć.")
        return

    print("Przygotowywanie tabeli...")
    cursor.execute("DROP TABLE IF EXISTS housing;")
    cursor.execute("""
        CREATE TABLE housing (
            longitude FLOAT, 
            latitude FLOAT, 
            housing_median_age FLOAT,
            total_rooms FLOAT, 
            total_bedrooms FLOAT, 
            population FLOAT,
            households FLOAT, 
            median_income FLOAT, 
            median_house_value FLOAT,
            ocean_proximity VARCHAR(20)
        );
    """)

    print("Wczytywanie danych z CSV...")
    df = pd.read_csv('data/housing.csv')
    
    df = df.replace({np.nan: None})
    
    sql = "INSERT INTO housing VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = [tuple(x) for x in df.values]
    
    print(f"Wysyłanie {len(values)} wierszy do MySQL (to może chwilę potrwać)...")
    try:
        cursor.executemany(sql, values)
        conn.commit()
        print(f"Migracja zakończona sukcesem! Wgrano {len(df)} wierszy.")
    except mysql.connector.Error as err:
        print(f"Błąd podczas migracji: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    migrate_data()