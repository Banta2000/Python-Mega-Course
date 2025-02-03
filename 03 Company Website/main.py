import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

st.set_page_config(layout='wide')

st.title('The Best Company')
st.write('Welcome to the best Company in the world!')

st.header('Our Team')

c1, e1, c2, e2, c3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

idx_1, idx_2, idx_3 = np.array_split(df.index, 3)

with c1:
    for idx, row in df.loc[idx_1].iterrows():
        name = row['first name'].capitalize() + ' ' + row['last name'].capitalize()
        role = row['role']
        st.header(name)
        st.write(role)
        st.image(f"images/{row['image']}")
        
with c2:
    for idx, row in df.loc[idx_2].iterrows():
        name = row['first name'].capitalize() + ' ' + row['last name'].capitalize()
        role = row['role']
        st.header(name)
        st.write(role)
        st.image(f"images/{row['image']}")
        

with c3:
    for idx, row in df.loc[idx_3].iterrows():
        name = row['first name'].capitalize() + ' ' + row['last name'].capitalize()
        role = row['role']
        st.header(name)
        st.write(role)
        st.image(f"images/{row['image']}")
        
