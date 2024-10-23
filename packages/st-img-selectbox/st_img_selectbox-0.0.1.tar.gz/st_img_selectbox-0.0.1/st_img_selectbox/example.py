import streamlit as st
from PIL import Image
from st_img_selectbox import st_img_selectbox

# Define the options
options = []
for i in range(1, 6):
    # Create a simple colored image
    img = Image.new('RGB', (50, 50), color=(i*40, i*40, i*40))
    options.append({"image": img, "option": f"Option {i}"})

# Use the custom select box with a custom highlight color
selected_option = st_img_selectbox(
    options=options,
    value="Option 2",
    height=50,
    fontsize=20,
    highlight_color="#bbb",
    key="my_selectbox"
)

st.write("You selected:", selected_option)
