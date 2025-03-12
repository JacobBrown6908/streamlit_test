import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


st.write("hellow world")

x = st.text_input("favourite movie")
st.write(f"Your Favourite movie is: {x}")

is_click = st.button("Click Me")

st.write("## Markdown Title using hashtags")

import pandas as pd

data = pd.read_csv("rbdata_2linedata.csv")

st.write("This is my battleship data form Math 425")
st.write(data)

st.line_chart(data)