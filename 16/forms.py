import streamlit as st
from datetime import datetime

st.title("User info form:")

form_values = {
    "name": None,
    "age": None,
    "gender": None,
    "birthday": None
}
min_date = datetime(1900, 1, 1)
max_date = datetime.now()

with st.form(key="user_info_form", clear_on_submit=True):
    form_values["name"] = st.text_input("Name: ")
    form_values["age"] = st.number_input("Age: ")
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["birthday"] = st.date_input("Birthday: ", min_value=min_date, max_value=max_date)

    submit_button = st.form_submit_button(label="Submit") # nem fut újra semmi amíg nem nyomjuk meg ezt a gombot. 

    if submit_button:
        if not all(form_values.values()):
            st.error("Please fill all required fields!")
        else:
            st.balloons()
            st.success("Form successfully submitted!")
            
