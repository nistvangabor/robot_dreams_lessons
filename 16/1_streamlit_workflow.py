#pip install streamlit plotly
#pip freeze > requirements.txt
#streamlit run lessons/16/main.py

import streamlit as st
#magic command, writes anything

st.write({"test":"test"}) 
st.write(True)
st.write(123)
3 + 4 #automatically writes
"hello world!" if False else "bye"

print("test")
#data flow in streamlit: bármikor valamit updatelni kell a képernyőn, a teljes kód újra le fog futni top to bottom
pressed = st.button("Press me") #ennek lesz alapból egy state-je, False. Ha változik a state gombnyomásra, lefut az egész file újra
print("first", pressed)

pressed2 = st.button("Second button")
print("Second", pressed2)