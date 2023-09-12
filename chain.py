import streamlit as st

st.title("Conditional Input Boxes")

# Input box for the first text
input_text1 = st.text_input("Enter text in the first input box:")

# Check if input_text1 is not empty
if input_text1:
    # Input box for the second text (enabled only when the first input is not empty)
    input_text2 = st.text_input("Enter text in the second input box:")

    # Display the input from the second input box
    if input_text2:
        st.write(f"You entered in the second input box: {input_text2}")
