import streamlit as st
import speech_recognition as sr
import re

# Speech-to-text function using Google Web Speech API
def speech_to_text():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        st.info("Listening now...")  # Notification displayed when listening starts
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for background noise
        audio = recognizer.listen(source)  # Capture audio from the microphone

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        st.success("Speech recognized successfully!")
        return text
    except sr.RequestError:
        st.error("API unavailable or unresponsive.")
        return None
    except sr.UnknownValueError:
        st.error("Unable to recognize speech. Please try again.")
        return None

st.title("Speech-to-Text Form with Care Scribe")

def set_text_fields(data):
    # Ensure the data has expected keys
    name = st.text_input("Name", value=data.get("Name", ""))
    email = st.text_input("Email", value=data.get("Email", ""))
    age = st.text_input("Age", value=data.get("Age", ""))
    gender = st.text_input("Gender", value=data.get("Gender", ""))
    address = st.text_input("Address", value=data.get("Address", ""))
    return name, email, age, gender, address

# Input fields for the form
name = st.text_input("Name")
email = st.text_input("Email")
age = st.text_input("Age")
gender = st.text_input("Gender")
address = st.text_input("Address")

def extract_details(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    email = re.findall(email_pattern, text)

    age_pattern = r'(\b\d{1,2}\b)\s?(years old|yrs|years|age)?'
    age = re.findall(age_pattern, text)

    name_pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
    name = re.findall(name_pattern, text)

    gender_pattern = r'\b(Male|Female|Other|male|female|other)\b'
    gender = re.findall(gender_pattern, text)

    address_pattern = r'\d{1,4}\s\w+\s(?:Street|Avenue|Road|Boulevard|Lane)\b'
    address = re.findall(address_pattern, text)

    details = {
        'Name': name[0] if name else None,
        'Age': age[0] if age else None,
        'Address': address[0] if address else None,
        'Gender': gender[0] if gender else None,
        'Email': email[0] if email else None
    }
    
    return details

# Create columns to align buttons (Speak and Submit) horizontally
col1, col2 = st.columns(2)

with col1:
    if st.button("Speak"):
        spoken_text = speech_to_text()
        if spoken_text:
            st.write(f"**Recognized Speech:** {spoken_text}")  # Display recognized speech
            extracted_details = extract_details(spoken_text)
            name, email, age, gender, address = set_text_fields(extracted_details)

with col2:
    submit_button = st.button("Submit")

# On form submission
if submit_button:
    st.success("Form submitted successfully!")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Address:** {address}")