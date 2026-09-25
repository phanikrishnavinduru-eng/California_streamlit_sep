import numpy as np
import joblib
import streamlit as st
import sklearn
obj = joblib.load('california.joblib')
model=obj['model']
cols=obj['column']
st.title('California App')
In=[]
for i in cols:
    v=st.number_input(f'Enter {i} Value:')
    In.append(v)
if st.button('click'):
    #Input =np.array([In])
    out=model.predict([In])
    st.success(f"Median  House Value:{out}")