
import streamlit as st

st.title("Question 5: Dual-LED Shared Ground Rail")

left, right = st.columns(2)

with left:
    st.subheader("Wokwi Circuit")
    st.write("Red LED on Pin 12 and Blue LED on Pin 11")
    st.write("Both LED cathodes connect to the shared GND rail.")

with right:
    st.subheader("Circuit Description")
    st.table({
        "Component": ["Red LED", "Blue LED", "Ground"],
        "Connection": [
            "Arduino Pin 12",
            "Arduino Pin 11",
            "Shared negative rail"
        ]
    })
