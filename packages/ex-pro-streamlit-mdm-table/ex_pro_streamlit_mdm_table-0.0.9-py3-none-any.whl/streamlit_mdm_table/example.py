import streamlit as st
from streamlit_mdm_table import streamlit_mdm_table

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run streamlit_mdm_table/example.py`

st.subheader("Component with constant args")

st.write("This is placeholder text that is used to simulate what happens when the page requires to be scrolled down.")
st.write("The component should work as expected, but the page will need to be scrolled down to see the component.")
st.write("This is placeholder text that is used to simulate what happens when the page requires to be scrolled down.")
st.write("The component should work as expected, but the page will need to be scrolled down to see the component.")
st.write("This is placeholder text that is used to simulate what happens when the page requires to be scrolled down.")
st.write("The component should work as expected, but the page will need to be scrolled down to see the component.")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
num_clicks = streamlit_mdm_table()
print(num_clicks)
# st.markdown("You've clicked %s times!" % int(num_clicks))

# st.markdown("---")
# st.subheader("Component with variable args")

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
# name_input = st.text_input("Enter a name", value="Streamlit")
# num_clicks = streamlit_mdm_table(name_input, key="foo")
# # st.markdown("You've clicked %s times!" % int(num_clicks))
