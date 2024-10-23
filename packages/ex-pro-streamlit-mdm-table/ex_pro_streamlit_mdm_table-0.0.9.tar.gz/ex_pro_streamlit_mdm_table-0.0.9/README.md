# streamlit-mdm-table

Streamlit component that allows for easy mapping of tasks and IDs to a table.
This is specific for a project and may not be useful for other projects.
Do not use.

## Installation instructions

Import the wheel file in your project.

## Usage instructions

```python
import streamlit as st

from streamlit_mdm_table import streamlit_mdm_table

value = streamlit_mdm_table(
    tasks, 
    linkedin_content, 
    youtube_content,
    google_analytics_content,
    poppulo_harmony_content,
    poppulo_email_content,
    sharepoint_content,
    viva_engage_content
)

if value is not None:
    st.dataframe(value)
```