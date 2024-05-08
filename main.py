import os 
import base64
import pysftp
import fnmatch
import numpy as np
import openpyxl

import pandas as pd

from dotenv import load_dotenv

load_dotenv()

SFTP_HOST = os.environ['SFTP_HOST']
SFTP_USER = os.environ['SFTP_USER']
SSH_KEY_BASE64 = os.environ['SSH_KEY_BASE64']
SSH_KEY_PASS = os.environ['SSH_KEY_PASS']
REMOTE_DIR = 'IN'

import warnings
warnings.filterwarnings('ignore','.*Failed to load HostKeys.*')


def write_key_file(path='.'):
    key_data = base64.b64decode(SSH_KEY_BASE64).decode('utf-8')
        
    with open(os.path.join(path, 'key'), 'w') as key_file:
        key_file.write(key_data)

    return os.path.abspath(os.path.join(path, 'key'))

def list_all_files():
    # Trust all host keys - bad practice!
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    key_path = write_key_file()

    # Get connection
    sftp = pysftp.Connection(host=SFTP_HOST, username=SFTP_USER, private_key=key_path, private_key_pass=SSH_KEY_PASS, cnopts=cnopts)

    # filter away directorires and files without file extensions
    filelist = [ f for f in sftp.listdir(REMOTE_DIR) if fnmatch.fnmatch(f, 'yr-ydelsesrefusion-beregning-730-0050-2024-03-03.csv') ]
    return filelist, sftp

def handle_files(files, connection):
    for filename in files:
        # Open file

        connection.get(os.path.join(REMOTE_DIR, filename).replace("\\","/"), "data/"+filename)

        #with connection.open(os.path.join(REMOTE_DIR, filename).replace("\\","/"), filename) as f:
            #print(os.path.join(REMOTE_DIR, filename).replace("\\","/"))
            # CSV file open as f, do something with it
            # E.g. read into pandas dataframe
            #df = pd.read_csv(f, sep=';', engine='python')
            #print(df.head)  

def data_wrangling(files):
    for filename in files:
        df=pd.read_csv("data/"+filename, sep=';', engine='python')

        # Ydelsestyper
        ydelsestyper=df[['Ydelse']].groupby(['Ydelse']).sum().reset_index()
        #print(ydelsestyper.to_string(index=False))

        # Antal ydelsesmodtagere 
        # Beholder første observation pr. Uge x Ydelse x CPR nummer
        df2=df[['Uge','CPR nummer','Ydelse']].groupby(['Uge','Ydelse','CPR nummer']).first().reset_index()
        #print(len(df),len(df2))
        #print(df2.head(10))

        df3=df2.groupby(['Uge','Ydelse'])['CPR nummer'].count()
        df4=df3.reset_index()

        return df4



file_list, conn = list_all_files()
print(file_list, len(file_list))

#handle_files(file_list, conn)


def data_export(df):
    df.to_csv('data/yr-data.csv', index=False)



file_list=['yr-ydelsesrefusion-beregning-730-0050-2024-03-03.csv']
workdata=data_wrangling(file_list)

data_export(workdata)
        
