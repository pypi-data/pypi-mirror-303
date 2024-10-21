import streamlit as st
from st_image_cropper import st_image_cropper

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

st.subheader("Component with constant args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
crop = st_image_cropper(image_url="https://www.defenceturkey.com/files/content/5da4b462d870a.jpg")
st.write(crop)

crop = st_image_cropper(image_path="/Users/59199/Desktop/LHD Demo/AW169-cockpit.jpeg", crop_color="blue", value={"x": 0.1, "y": 0.1, "width": 0.5, "height": 0.5})
st.write(crop)
