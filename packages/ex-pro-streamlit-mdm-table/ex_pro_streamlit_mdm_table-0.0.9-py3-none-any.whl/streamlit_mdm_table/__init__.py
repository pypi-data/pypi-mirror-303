import os
import streamlit.components.v1 as components
import pandas as pd
from typing import List, Dict, Union

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
        # We give the component a simple, descriptive name ("streamlit_mdm_table"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_mdm_table",
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
    _component_func = components.declare_component("streamlit_mdm_table", path=build_dir)


# Create a wrapper function for the component. This is a best practice.
# The wrapper allows us to customize the component's API: we can 
# pre-process its input args, post-process its output value, and add a 
# docstring for users.
# We don't need to preprocess any args in this case, but we'll add a
# docstring to explain how the component works and return the output value
def streamlit_mdm_table(
    task_data: List[Dict[str, str]], 
    linkedin_content: List[Dict[str, str]],
    youtube_content: List[Dict[str, str]],
    google_analytics_content: List[Dict[str, str]],
    poppulo_harmony_content: List[Dict[str, str]],
    poppulo_email_content: List[Dict[str, str]],
    sharepoint_content: List[Dict[str, str]],
    viva_engage_content: List[Dict[str, str]],
    key=None
) -> Union[pd.DataFrame, None]:
    """Create a new instance of "streamlit_mdm_table".

    Parameters
    ----------
    task_data: list
        The list of tasks to be displayed in the table. Contains dictionaries with
        the following keys: "taskId", "monthYear", "taskName", "linkedinId", "youtubeId",
        "gaId", "poppuloHarmonyId", "poppuloEmailId", "sharepointId", "vivaEngageId".
        
    linkedin_content: list
        The list of LinkedIn content to be displayed in the table. Contains dictionaries with
        the following keys: "id", "title".
        
    youtube_content: list
        The list of YouTube content to be displayed in the table. Contains dictionaries with
        the following keys: "id", "title".
        
    google_analytics_content: list
        The list of Google Analytics content to be displayed in the table. Contains dictionaries with
        the following keys: "id", "title".
        
    poppulo_harmony_content: list
        The list of Poppulo Harmony content to be displayed in the table. Contains dictionaries with
        the following keys: "id", "title".
        
    poppulo_email_content: list
        The list of Poppulo Email content to be displayed in the table. Contains dictionaries with
        the following keys: "id", "title".
        
    sharepoint_content: list
        The list of SharePoint content to be displayed in the table. Contains dictionaries with
        the following keys: "id", "title".
        
    viva_engage_content: list
        The list of Viva Engage content to be displayed in the table. Contains dictionaries with
        the following keys: "id", "title".
        
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    pd.DataFrame or None
        The updated list of tasks with the new values. Only returns the list if the user
        clicks "Save Changes". Otherwise, returns None. 

    """
    
    component_value = _component_func(
        data=task_data,
        linkedinContent=linkedin_content,
        youtubeContent=youtube_content,
        googleAnalyticsContent=google_analytics_content,
        poppuloHarmonyContent=poppulo_harmony_content,
        poppuloEmailContent=poppulo_email_content,
        sharepointContent=sharepoint_content,
        vivaEngageContent=viva_engage_content,
        key=key
    )
    
    # Parse the list of dicts as a df
    if component_value is not None:
        df = pd.DataFrame(component_value)
        return df

    return component_value
