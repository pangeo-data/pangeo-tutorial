
import os
import tarfile
import wget


def get_sst_data(data_dir=None):
    if data_dir is None:
        data_dir = os.path.join(os.path.expanduser('~'), '.xarray_tutorial_data')
    
    os.makedirs(data_dir, exist_ok=True)

    remote = 'http://ldeo.columbia.edu/~rpa/sst.tar.gz'

    # download the data
    filename = wget.download(remote, out=data_dir)

    # un tar/zip the file
    cwd = os.getcwd()
    os.chdir(data_dir)
    try:
        with tarfile.open(filename, "r:gz") as file:
            file.extractall()
    finally:
        os.chdir(cwd)

    # remove tar.gz file
    os.remove(filename)

    print(f'\nsst data is in {data_dir}/sst')
