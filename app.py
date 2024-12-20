import streamlit as st
import os
import random
import time

# Path to the image directory
IMAGE_DIR = "./images/"
WISH_IMAGE_DIR = "./images/wishes/"

def get_random_image(folder):
    if os.path.exists(folder):
        image_files = [f for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if image_files:
            return os.path.join(folder, random.choice(image_files))
    return None

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .stAppHeader, ._profileContainer_gzau3_53,  
    .viewerBadge_container__1QSob, ._profileContainer_gzau3_63,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none !important;
        visibility: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create an image placeholder
image_placeholder = st.empty()

# Display a random image initially
random_image_path = get_random_image(IMAGE_DIR)
if random_image_path:
    image_placeholder.image(random_image_path, use_container_width =True)

time.sleep(5)

christmas_image_path = get_random_image(WISH_IMAGE_DIR)
if christmas_image_path:
    image_placeholder.image(christmas_image_path, use_container_width =True)
    st.title("From :blue[Deanta] :red[Technology Team] :sunglasses:")

