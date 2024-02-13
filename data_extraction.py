import pandas as pd
import os
import subprocess

#os.system("sudo apt-get update")
#os.system("sudo apt-get install git-secret")

#hostname = subprocess.check_output(['git', 'secret', 'reveal', '-p', 'DB_HOSTNAME']).decode().strip()
hostname = os.environ['DB_HOSTNAME']
print(hostname)
def load_data():
    data = pd.read_csv('data.csv')
    print(data.head())
    return data

load_data()
