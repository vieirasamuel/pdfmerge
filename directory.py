import os
import glob

def get_cwd_dirs():
    cwd = os.getcwd()
    directories = []
    for (dirpath, dirnames, filenames) in os.walk(cwd):
        dirnames[:] = [d for d in dirnames if not d.startswith('.git') and not d.startswith('__pycache__')]
        directories.extend(dirnames)
        break
    return directories

def get_cwd_pdfs(cwd):
    pdfs = glob.glob(os.path.join(cwd, '*.pdf'))
    return pdfs

def get_directory_name(cwd):
    return os.path.basename(cwd)

dirs = get_cwd_dirs()
