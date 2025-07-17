import streamlit as st
import pandas as pd


st.title("Closet App")

st.write("Add your clothes manually!")

item = st.text_input("Clothing item name")
category = st.selectbox("Category", ["Top", "Bottom", "Shoes", "Outerwear"])
color = st.color_picker("Pick a color")
season = st.multiselect("Season", ["Spring", "Summer", "Fall", "Winter"])

df = pd.DataFrame(columns= ["Item", "Category", "Color", "Season"])

if st.button("Add item"):
    st.success(f"Added: {item} ({category}, {color}, {', '.join(season)})")
    new_row = {'Item': [item], 'Category': [category], 'Color': [color], 'Season': [season], }
    df.loc[len(df)] = new_row

st.dataframe(df)