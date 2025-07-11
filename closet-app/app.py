import streamlit as st


st.title("Closet App")

st.write("Add your clothes manually!")

item = st.text_input("Clothing item name")
category = st.selectbox("Category", ["Top", "Bottom", "Shoes", "Outerwear"])
color = st.color_picker("Pick a color")
season = st.multiselect("Season", ["Spring", "Summer", "Fall", "Winter"])

if st.button("Add item"):
    st.success(f"Added: {item} ({category}, {color}, {', '.join(season)})")