import streamlit as st
import os
import random
import time

# Path to the image directory
IMAGE_DIR = "./images/"
WISH_IMAGE_DIR = "./images/wishes/"


# Check if the directory exists and contains images
if os.path.exists(IMAGE_DIR):
    image_files = [f for f in os.listdir(IMAGE_DIR)]

    if image_files:
        # Select a random image when the page loads
        random_image = random.choice(image_files)
        image_path = os.path.join(IMAGE_DIR, random_image)
        st.image(image_path, use_container_width =True)

        time.sleep(5)

        wish_image_files = [f for f in os.listdir(WISH_IMAGE_DIR)]
        if wish_image_files:
            random_image = random.choice(wish_image_files)
            image_path = os.path.join(IMAGE_DIR, random_image)
            st.image(image_path, use_container_width =True)



    else:
        st.warning("No image files found in the directory.")
else:
    st.error(f"The directory '{IMAGE_DIR}' does not exist.")
