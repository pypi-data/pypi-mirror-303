import os
import streamlit.components.v1 as components
import base64
import streamlit as st
from pathlib import Path

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_image_cropper",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_image_cropper", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def st_image_cropper(image_url=None, image_data=None, image_path=None, default=None, key=None):
    """
    Create a new instance of "st_image_cropper".

    Parameters
    ----------
    image_url : str or None
        The URL of the image to display. If provided, this takes precedence over `image_data` and `image_path`.
    image_data : str or None
        A base64-encoded string representing the image. Use this if you want to embed the image directly.
    image_path : str or None
        A local file path to the image on the server. The image will be read and encoded to a base64 string.
    default : dict or None
        A dictionary specifying the default position and size of the selection rectangle.
        Example: {"x": 0, "y": 0, "width": 100, "height": 100}
    key : str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict or None
        A dictionary containing the selected area's position and size:
        {"x": int, "y": int, "width": int, "height": int}
        Returns `None` if the component hasn't been interacted with yet.
    """
    # If image_path is provided, read the image and encode it to base64
    if image_path:
        try:
            with open(image_path, "rb") as image_file:
                image_bytes = image_file.read()
                encoded = base64.b64encode(image_bytes).decode()
                # Determine the image type based on the file extension
                extension = Path(image_path).suffix.lower()
                if extension == ".png":
                    mime_type = "image/png"
                elif extension in [".jpg", ".jpeg"]:
                    mime_type = "image/jpeg"
                elif extension == ".gif":
                    mime_type = "image/gif"
                else:
                    mime_type = "application/octet-stream"  # Fallback
                # Create a data URI
                image_data = f"data:{mime_type};base64,{encoded}"
        except Exception as e:
            st.error(f"Failed to read image from path: {e}")
            image_data = None

    # Call the component and pass the arguments
    component_value = _component_func(
        image_url=image_url,
        image_data=image_data,
        default=default,
        key=key,
    )

    return component_value