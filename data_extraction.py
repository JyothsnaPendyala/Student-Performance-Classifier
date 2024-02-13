import pandas as pd
import os
import subprocess

hostname = subprocess.check_output(['git', 'secret', 'reveal', '-p', 'DB_HOSTNAME']).decode().strip()
#hostname = os.environ.get('DB_HOSTNAME')
print(hostname)
def load_data():
    data = pd.read_csv('data.csv')
    print(data.head())
    return data

load_data()
