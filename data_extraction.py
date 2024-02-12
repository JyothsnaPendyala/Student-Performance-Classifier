import pandas as pd
import os

hostname = os.environ.get('DB_HOSTNAME')
print(hostname)
def load_data():
    data = pd.read_csv('data.csv')
    print(data.head())
    return data

load_data()
