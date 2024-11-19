import streamlit as st
import os

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is *Markdown*")
st.caption("This is a _caption_")
code_example = """
def greet(name):
    print(f"hello {name}")

"""

st.code(code_example, language="python")

st.divider()

#pictures: kell egy mappa static néven, csak így működik
st.image(os.path.join(os.getcwd(), "16/static", "capybara.jpg"))
st.image("./16/static/capybara.jpg", width=400)