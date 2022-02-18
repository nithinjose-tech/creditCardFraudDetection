import streamlit as st
import pandas as pd
import pickle
from PIL import Image
st.write("""
# Credit card fraud detection 
 """)

image = Image.open('Credit-card-fraud.jpg')
st.image(image)
logistic_regressor = open('credit_card.pkl','rb')
regressor = pickle.load(logistic_regressor)
# #Text Input
time = st.text_input("Enter the time",)
v1 = st.text_input("Enter v1")
v2 = st.text_input("Enter v2")
v3 = st.text_input("Enter v3")
v4 = st.text_input("Enter v4")
v5 = st.text_input("Enter v5")
v6 = st.text_input("Enter v6")
v7 = st.text_input("Enter v7")
v8 = st.text_input("Enter v8")
v9 = st.text_input("Enter v9")
v10 = st.text_input("Enter v10")
v11 = st.text_input("Enter v11")
v12 = st.text_input("Enter v12")
v13 = st.text_input("Enter v13")
v14 = st.text_input("Enter v14")
v15 = st.text_input("Enter v15")
v16 = st.text_input("Enter v16")
v17 = st.text_input("Enter v17")
v18 = st.text_input("Enter v18")
v19 = st.text_input("Enter v19")
v20 = st.text_input("Enter v20")
v21 = st.text_input("Enter v21")
v22 = st.text_input("Enter v22")
v23 = st.text_input("Enter v23")
v24 = st.text_input("Enter v24")
v25 = st.text_input("Enter v25")
v26 = st.text_input("Enter v26")
v27 = st.text_input("Enter v27")
v28 = st.text_input("Enter v28")
amount = v28 = st.text_input("Enter amount")


submit = st.button("Predict")

if submit:
	result = regressor.predict([[time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,amount]])
	

if result[0] == 0:
    
    st.write(f'<p style="background-color:gray;color:#33ff33;font-size:24px;border-radius:2%;">This is a legitimate transaction</p>', unsafe_allow_html=True)
else:
    
    st.write(f'<p style="background-color:white;color:red;font-size:24px;border-radius:2%;">This is a fraudulent transaction</p>', unsafe_allow_html=True)

	
	