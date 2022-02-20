import streamlit as st
import pandas as pd
import numpy as np
st.title('Uber pickups in NYC')
df=pd.read_csv(r'C:\Users\Hemangi Koli\Downloads\Report_Dashboard\data.csv')
st.write(df)

