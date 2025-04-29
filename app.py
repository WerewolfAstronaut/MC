import streamlit as st
import pandas as p
import requests

# st.title("My first weather dashboard")
# st.write("this will show weather soon")
st.markdown("<h1 style='color: green;'>☀️ My Weather Forecast App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: green;'>Check the weather in your favorite city!</h4>", unsafe_allow_html=True)


city = st.selectbox("Choose a city:", ["Colombo","Anuradhapura"])

# 🗺️ City coordinates\z
city_coordinates = {
    "Colombo": {"lat": 6.9271, "lon": 79.8612},
    "Anuradhapura":{"lat":8.3122,"lon":80.4131}
} 

if city:
        latitude =  city_coordinates[city]["lat"]
        longitude =  city_coordinates[city]["lon"]

resp = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,is_day,wind_speed_10m,rain,showers,snowfall,weather_code')
LEGO = resp.json()

if "current" in LEGO:
        TEMP=LEGO["current"]["temperature_2m"]
        st.metric(label='🌡 temperature',value=f"{TEMP}℃")


weather_code =LEGO["current"]["weather_code"]

weather_images={
        "sunny":'https://cdn-icons-png.freepik.com/256/8595/8595797.png?ga=GA1.1.1294351196.1745145812&semt=ais_hybrid',
        "cloudy":'https://cdn-icons-png.freepik.com/256/9189/9189673.png?ga=GA1.1.1294351196.1745145812&semt=ais_hybrid',
        'rainy':"https://cdn-icons-png.freepik.com/256/5996/5996640.png?ga=GA1.1.1294351196.1745145812&semt=ais_hybrid"
}

if weather_code in [0,1]:
        image_url=weather_images["sunny"]
elif weather_code in [2,3]:
        image_url=weather_images["cloudy"]       
elif 50<=weather_code<70 : # rainy
        image_url=weather_images["rainy"]# 🌄 Add a background image

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-photo/photorealistic-view-tree-nature-with-branches-trunk_23-2151478106.jpg?uid=R198072021&ga=GA1.1.1294351196.1745145812&semt=ais_hybrid&w=740");
             background-size: cover;
             background-position: center;
             background-attachment: fixed;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

