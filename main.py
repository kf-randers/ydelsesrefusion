import os 
import base64
import pysftp
import fnmatch

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
    filelist = [ f for f in sftp.listdir(REMOTE_DIR) if fnmatch.fnmatch(f, '*.csv') ]
    return filelist, sftp

def habdle_files(files, connection):
    for filename in files:
        # Open file
        with connection.open(os.path.join(REMOTE_DIR, filename).replace("\\","/")) as f:
            # CSV file open as f, do something with it
            # E.g. read into pandas dataframe
            df = pd.read_csv(f, sep=';', engine='python')


file_list, conn = list_all_files()
habdle_files(file_list, conn)