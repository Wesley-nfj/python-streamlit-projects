import streamlit as st
import requests

st.set_page_config(page_title="African Country Facts", layout="centered")

# Title
st.title("🌍 Africa Fact- African Country Facts Explorer")

# Input country
selected_country = st.text_input("Enter the country you want to know info about")

# Button to fetch data
if st.button("Get Facts") and selected_country:
    country = selected_country.strip().title()
    st.write(f"Fetching data for **{country}**...")

    try:
        # API endpoint
        url = f"https://restcountries.com/v3.1/name/{country}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()[0]

            st.subheader(data["name"]["common"])
            st.write(f"**Capital:** {data['capital'][0] if 'capital' in data else 'N/A'}")
            st.write(f"**Region:** {data['region']}")
            st.write(f"**Population:** {data['population']:,}")
            st.write(f"**Languages:** {', '.join(data['languages'].values()) if 'languages' in data else 'N/A'}")
            st.image(data['flags']['png'], caption=f"{country} Flag")
        else:
            st.error("❌ Could not fetch data. Check spelling or try another country.")
    except Exception as e:
        st.error(f"Error: {e}")
