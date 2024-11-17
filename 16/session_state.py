import streamlit as st

#without session state (doesn't work):
#counter = 0
#
#st.write(f"Counter value: {counter}")
#
#if st.button("Increment Counter"):
#    counter += 1
#    st.write(f"Counter incremented to {counter}")
#else:
#    st.write(f"Counter stays at {counter}")ű


if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter +=1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(f"Counter did not reset")

st.write(f"Counter value: {st.session_state.counter}")


#session is about a user being connected from a browser, each time we refresh the page from the browser
#the session resets