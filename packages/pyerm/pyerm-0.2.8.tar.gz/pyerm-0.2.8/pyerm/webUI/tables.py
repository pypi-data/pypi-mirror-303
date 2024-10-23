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

import pandas as pd
from PIL import Image
import base64
from io import BytesIO
import streamlit as st
import os
import re
from time import strftime, gmtime

from pyerm.database.utils import delete_failed_experiments
from pyerm.database.dbbase import Database
from pyerm.webUI import PYERM_HOME

def tables():
    title()
    if os.path.exists(st.session_state.db_path) and st.session_state.db_path.endswith('.db'):
        detect_tables()
        st.sidebar.write('## SQL Query')
        if st.sidebar.checkbox('Use Full SQL Sentense For Total DB', False):
            input_full_sql()
        if st.sidebar.checkbox('Use SQL By Columns & Conditions & Tables', False):
            input_sql()
        select_tables()

def detect_tables():
    st.sidebar.markdown('## Detected Tables')
    db = Database(st.session_state.db_path, output_info=False)
    if len(db.table_names) == 0:
        st.write('No tables detected in the database.')
        return
    table_name = st.sidebar.radio('**Table to select**:', db.table_names + db.view_names)
    st.session_state.table_name = table_name

def select_tables():
    # def image_to_base64(img, desc):
    #     buffered = BytesIO(img)
    #     img_str = base64.b64encode(buffered.getvalue()).decode()
    #     return img_str
    
    # def make_image_clickable(image_name, image, desc):
    #     img_str = image_to_base64(image, desc)
    #     if img_str:
    #         return f'<a href="data:image/jpeg;base64,{img_str}" target="_blank" title="{image_name}"><img src="data:image/jpeg;base64,{img_str}" width="100"></a>'
    #     else:
    #         return f'<a href="#" title="None"><img src="#" width="100"></a>'
    
    def fold_detail_row(row, col_name):
        if row[col_name]:
            detail = row[col_name].replace("\n", "<br>")
            return f'<details><summary>Details</summary>{detail}</details>'
        else:
            return 'None'

    db = Database(st.session_state.db_path, output_info=False)
    table_name:str = st.session_state.table_name
    st.write('## Table:', table_name)
    if st.session_state.sql is not None:
        try:
            df = pd.read_sql_query(st.session_state.sql, db.conn)
            st.write(f'### Used SQL: ({st.session_state.sql})')
            st.session_state.sql = None
        except Exception as e:
            st.write('SQL Error:', e)
            st.session_state.sql = None
            return
    else:
        data = db[table_name].select()
        columns = [column[0] for column in db.cursor.description]
        df = pd.DataFrame(data, columns=columns)
    
    
    if st.button('Refresh', key='refresh1'):
        st.session_state.table_name = table_name
        st.rerun()
    
    
    columns_keep = [col for col in df.columns if not col.startswith("image_")]
    
    if table_name == 'experiment_list':
        if st.checkbox('Delete all failed and stuck records'):
            st.write('**Warning: This operation will delete all failed records and their results, which cannot be undone.**')
            if st.button(f"Confirm"):
                delete_failed_experiments(db)
                st.session_state.table_name = table_name
        df['failed_reason'] = df.apply(lambda x: fold_detail_row(x, 'failed_reason'), axis=1)
        df['useful_time_cost'] = df['useful_time_cost'].apply(lambda x: strftime('%H:%M:%S', gmtime(x)) if not pd.isnull(x) else x) 
        df['total_time_cost'] = df['total_time_cost'].apply(lambda x: strftime('%H:%M:%S', gmtime(x)) if not pd.isnull(x) else x)
    # elif table_name.startswith("result_"):
    #     # special process for image columns
    #     pattern = re.compile(r'image_(\d+)')
    #     max_image_num = -1
    #     for name in df.columns:
    #         match = pattern.match(name)
    #         if match:
    #             max_image_num = max(max_image_num, int(match.group(1)))
                
    #     for i in range(max_image_num+1):
    #         if f'image_{i}' in df.columns and not df[f'image_{i}_name'].isnull().all():
    #             df[f'image_{i}'] = df.apply(lambda x: make_image_clickable(x[f'image_{i}_name'], x[f'image_{i}'], desc=f"{x[f'experiment_id']}_{i}"), axis=1)
    #             columns_keep.append(f'image_{i}')
    
    df = df[columns_keep]
    st.write(df.to_html(escape=False, columns=columns_keep), unsafe_allow_html=True)
    if st.button('Refresh', key='refresh2'):
        st.session_state.table_name = table_name
        st.rerun()

def input_sql():
    st.sidebar.write('You can set the columns and condition for construct a select SQL sentense for the current table here.')
    condition = st.sidebar.text_input("Condition", value='', help='The condition for the select SQL sentense.')
    columns = st.sidebar.text_input("Columns", value='*', help='The columns for the select SQL sentense.')
    st.session_state.table_name = st.sidebar.text_input("Table", value=st.session_state.table_name, help='The table, view or query for the select SQL sentense.')
    if st.sidebar.button('Run', key="run_table_sql"):
        st.session_state.sql = f"SELECT {columns} FROM {st.session_state.table_name} WHERE {condition}" if condition else f"SELECT {columns} FROM {st.session_state.table_name}"

def input_full_sql():
    st.sidebar.write('You can input a full SQL sentense here to select what you need and link different tables or views.')
    sql = st.sidebar.text_area('SQL', value=None, height=200)
    if st.sidebar.button('Run', key='run_full_sql'):
        st.session_state.sql = sql
        st.session_state.table_name = 'SQL Query Results'

def title():
    st.title('Tables of the experiment records')
    if os.path.exists(st.session_state.db_path) and st.session_state.db_path.endswith('.db'):
        st.write(f'Database Loaded (In {st.session_state.db_path})')
    else:
        st.write('No database loaded, please load a database first.')



