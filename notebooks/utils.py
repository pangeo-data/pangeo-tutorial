
import requests
import shutil
import tarfile
import os

def download_file(data_dir=None):
    # Make data directory
    if data_dir is None:
        data_dir = os.path.join(os.path.expanduser('~'), '.xarray_tutorial_data')

    os.makedirs(data_dir, exist_ok=True)
    cwd = os.getcwd()
    os.chdir(data_dir)
    
    # Data to download
    url = 'http://ldeo.columbia.edu/~rpa/sst.tar.gz'
    local_filename = url.split('/')[-1]
    
    # Download the data
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    
    # un tar/zip the file
    try:
        with tarfile.open(local_filename, "r:gz") as file:
            file.extractall()
    finally:
        os.chdir(cwd)

    # remove tar.gz file
    os.remove(data_dir + '/' + local_filename)
    
    print(f'\nsst data is in {data_dir}/sst')