# MIT License

# Copyright (c) 2024 Yuxuan Shao

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Version: 0.2.7

import streamlit as st
import os
import platform
import math
import subprocess
from importlib.metadata import version

from pyerm.database.dbbase import Database
from pyerm.webUI import PYERM_HOME

REPO_URL = "https://github.com/Mr-SGXXX/pyerm"

def home():
    title()
    st.write("---")
    load_db()
    if os.path.exists(st.session_state.db_path) and st.session_state.db_path.endswith('.db'):
        st.markdown('Export Experiment Data')
        if st.checkbox('Download Excel & Result Images as ZIP'):
            download_zip()
        if st.checkbox('Download raw db file'):
            download_db()
    st.write("---")
    clean_cache()


def title():
    st.title('Python Experiment Record Manager WebUI')
    st.markdown(f"**Version**: {version('pyerm')}")
    st.markdown(f"**GitHub Repository**: [{REPO_URL}]({REPO_URL})")
    st.markdown(f"**PyPI**: [PyERM](https://pypi.org/project/pyerm/)")
    st.markdown(f"**License**: MIT")
    st.markdown(f"**Author**: Yuxuan Shao")
    st.markdown(f"**Description**:")
    st.markdown(f"PyERM is a Python package for managing experiment records.")
    st.markdown(f"This is the web user interface of the PyERM.")
    st.markdown(f"**Disclaimer**: This is a demo version. Bugs may exist. Use at your own risk.")

def load_db():
    st.markdown('## Load Database')
    st.markdown("### **(PyERM only supports local SQLite database for now)**")
    db_path = st.text_input("Database Path", value=st.session_state.db_path)
    if st.button('Change Database Path'):
        st.session_state.db_path = db_path
    st.write(f"Current database path: {st.session_state.db_path}")
    if os.path.exists(db_path) and db_path.endswith('.db'):
        st.write(f"Database found succesfully.")
    else:
        st.write(f"Database not found. Please input the correct path.")

def export_data():
    output_dir_path = f"{PYERM_HOME}/.tmp"
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    db_name = os.path.basename(st.session_state.db_path)
    db_name = os.path.splitext(db_name)[0]
    zip_path = os.path.join(output_dir_path, f"{db_name}.zip")
    result1 = subprocess.run(["export_zip", st.session_state.db_path, output_dir_path])
    if result1.returncode == 0:
        with open(zip_path, "rb") as file:
            zip = file.read()
        os.remove(zip_path)
    return zip

def download_zip():
    version = Database(st.session_state.db_path).get_db_version()
    if st.session_state.zip is None or version != st.session_state.last_version:
        st.session_state.zip = export_data()
        st.session_state.last_version = version
    st.download_button(
            label="Download Excel&Images as ZIP",
            data=st.session_state.zip,
            file_name=f"{os.path.basename(os.path.splitext(st.session_state.db_path)[0])}.zip",
            mime="application/zip"
        )
        

def download_db():
    with open(st.session_state.db_path, "rb") as file:
        db = file.read()
    st.download_button(
            label="Download raw db file",
            data=db,
            file_name=f"{os.path.basename(st.session_state.db_path)}",
            mime="application/sqlite3"
        )
    

def clean_cache():
    st.write('## Clean Cache')
    st.write('Cache is used to store temporary files, such as configure files.__')
    st.write(f'Cache folder is located at: **{PYERM_HOME}**')
    st.write(f'Cache folder size: {get_folder_size(PYERM_HOME)}')
    if st.checkbox('I want to clean cache'):
        st.write('This will delete the cache folder and all its contents, which cannot be undone.')
        if st.button('Confirm'):
            subprocess.run(["rm", "-rf", PYERM_HOME])
            st.write('Cache cleaned successfully.')
            
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return format_size(total_size)

def format_size(size_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    if size_bytes == 0:
        return "0 B"
    index = min(len(units) - 1, int(math.log(size_bytes, 1024)))
    size = size_bytes / (1024 ** index)
    return f"{size:.2f} {units[index]}"