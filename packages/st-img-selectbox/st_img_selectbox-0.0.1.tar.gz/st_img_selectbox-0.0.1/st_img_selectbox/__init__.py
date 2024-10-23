import os
import streamlit.components.v1 as components
import io
import base64
from PIL import Image

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
        "st_img_selectbox",
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
    _component_func = components.declare_component("st_img_selectbox", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def st_img_selectbox(options, value=None, height=None, fontsize=None, highlight_color="blue", key=None):
    """
    Create a new instance of "st_img_selectbox".

    Parameters
    ----------
    options: list of dicts
        Each dict should have keys "image" (PIL Image) and "option" (string)
    value: str or None
        The default selected option
    height: int or None
        Height of the select box
    fontsize: int or None
        Font size of the text
    highlight_color: str
        The color to highlight the selected option (e.g., "blue" or "#ccc")
    key: str or None
        An optional key that uniquely identifies this component.

    Returns
    -------
    str
        The string of the selected option.
    """
    # Prepare options to send to frontend
    serialized_options = []
    for item in options:
        # Get the original image
        original_image = item["image"]
        
        if height is not None:
            target_height = height - 6  # Account for 3px top and bottom margins
            aspect_ratio = original_image.width / original_image.height
            target_width = int(target_height * aspect_ratio)
            resized_image = original_image.resize((target_width, target_height), Image.Resampling.LANCZOS)
        else:
            resized_image = original_image  # Use original image if no height specified
        
        # Convert resized image to base64
        buffered = io.BytesIO()
        resized_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        serialized_options.append({
            "image": img_str,
            "option": item["option"]
        })

    # Call the component with serialized options and other parameters
    component_value = _component_func(
        options=serialized_options,
        value=value,
        height=height,
        fontsize=fontsize,
        highlight_color=highlight_color,  # Pass the highlight_color to frontend
        key=key,
        default=value
    )
    
    return component_value