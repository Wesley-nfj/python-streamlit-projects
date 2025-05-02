import streamlit as st
import requests

st.markdown(
    """
  <style>
    .stApp{
        background-image : url("https://i.pinimg.com/736x/00/23/7b/00237ba16f85737d29ef4573594608f9.jpg");
        background-attachment : fixed;
        background-size : cover;
    }    

   </style>                    
     """,
unsafe_allow_html=True
)

def all_currencies():
    api_key= "5b62343eafc614f3f4b0ab11"
    url= f"http://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response= requests.get(url)

    if response.status_code == 200:
        data= response.json()
        return list(data["conversion_rates"].keys())
    
   

def convert_currency(from_currency, to_currency, amount):
    api_key= "5b62343eafc614f3f4b0ab11"
    url= f"http://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response= requests.get(url)

    if response.status_code == 200:
        data= response.json()
    
        if data["result"]== "success":
           conversion_rates= data["conversion_rates"]
           rate= conversion_rates[to_currency]
           converted_amount= rate*amount
           return converted_amount
        else:
          st.error("API returned an unexpected error.")
    else:
       st.error("Failed to fetch result from API.")


st.markdown("### CURRENCY CONVERTER")

currencies= all_currencies()
from_currency= st.selectbox("From Currency",currencies)
to_currency= st.selectbox("To_currency", currencies)
amount= st.number_input("Amount", min_value=0.0, format="%.2f")

if st.button("Convert"):
   converted_amount= convert_currency(from_currency, to_currency, amount)
   
   

   st.markdown(f"""
      <div style="background-color:#d4edda; padding:16px; border-radius:10px; border-left:5px solid #28a745; color:black; font-size:16px;">
        <strong>{amount} {from_currency}</strong> is equivalent to <strong>{converted_amount}{to_currency}</strong>
      </div>

""", unsafe_allow_html=True)

