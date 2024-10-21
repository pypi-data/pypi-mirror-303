# st-image-cropper

Streamlit component that allows you to show an image with a cropper to select a subpart of the image for further usage

## Installation instructions

```sh
pip install st-image-cropper
```

## Usage instructions

```python
import streamlit as st
from st_image_cropper import st_image_cropper

crop = st_image_cropper(image_url="https://catoftheday.com/archive/2024/June/05.jpg")
st.write(crop)

crop = st_image_cropper(image_path="path/to/image")
st.write(crop)
```