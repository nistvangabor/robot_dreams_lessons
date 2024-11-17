import streamlit as st

st.sidebar.title("This is a sidebar")
st.sidebar.write("You can place elements like sliders, buttons and texts here")
sidebar_input = st.sidebar.text_input("Write something here")


col1, col2 = st.columns([1,1])

col1.write("This is a narrow column.")
col2.write("This is a much wider column with more content. The ratio of 1:8 is clearly visible when you compare the two.")

# You can also add other widgets or elements to further visualize the difference
with col1:
    st.write("This is col1")
    st.button("This is a button for col 1")

with col2:
    st.write("This is col2")
    st.button("This is a button for col 2")
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    with tab1:
        st.write("Tab1")
    with tab2:
        st.file_uploader(label="Upload file")


#containers:
with st.container(border=True):
    st.write("This is inside a container")

#placeholder:

placeholder = st.empty()
placeholder.write("This is an empty placeholder")

#expander:
with st.expander("Expand for more details:"):
    st.write("This is additional information")


#tooltip
st.button("Button with tooltip", help="This should help you to understand this better")

if sidebar_input:
    st.write(f"You enterted this in the sidebar: {sidebar_input}")