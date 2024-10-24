import streamlit as st
import time

# Simulating speech-to-text (real implementation would require integration with a speech recognition API)
def simulate_speech_to_text():
    st.session_state['name'] = "John Doe"
    st.session_state['email'] = "john.doe@example.com"
    st.session_state['age'] = 28
    st.session_state['gender'] = "Male"
    st.session_state['address'] = "1234 Elm Street"

# Handling form submission
def handle_submit():
    st.success("Form Submitted!")
    st.write("## Submitted Information")
    st.write(f"**Name:** {st.session_state.get('name')}")
    st.write(f"**Email:** {st.session_state.get('email')}")
    st.write(f"**Age:** {st.session_state.get('age')}")
    st.write(f"**Gender:** {st.session_state.get('gender')}")
    st.write(f"**Address:** {st.session_state.get('address')}")

# Main UI
st.title("Speech-to-Form Example")

# Input fields
name = st.text_input("Name", key="name", placeholder="Enter your name")
email = st.text_input("Email", key="email", placeholder="Enter your email")
age = st.number_input("Age", min_value=0, key="age")
gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="gender")
address = st.text_area("Address", key="address", placeholder="Enter your address")

# Buttons: Speak and Submit
speak_button = st.button("Speak", on_click=simulate_speech_to_text)
submit_button = st.button("Submit", on_click=handle_submit)

# Instruction message for the Speak button
st.info("Click 'Speak' to simulate speech recognition and auto-fill the form fields. After that, you can modify any of the fields before submitting.")
