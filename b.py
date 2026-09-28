import streamlit as st

st.title("STUDENT AND JOB PROTOFOLIO")

st.header("Student Information")

# Personal Information
name = st.text_input("Enter your Name")
college = st.text_input("Enter your College Name")
course = st.text_input("Enter your Course")
branch = st.text_input("Enter your Branch")
year = st.selectbox("Select your Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])

# Contact Information
st.header("Contact Information")

email= st.text_input("Enter your Email")
phone = st.text_input("Enter your Phone Number")
linkedin = st.text_input("Enter your LinkedIn Profile")

# Skills
st.header("Skills")

skills = st.text_area(
    "Enter your Skills",
)

# Projects
st.header("Projects")

project = st.text_area(
    "Enter your Projects",
)

# Certifications
st.header("Certifications")

certification = st.text_area(
    "Enter your Certifications",
)

# Career Objective
st.header("Career Objective")

objective = st.text_area(
    "Enter your Career Objective"
)

# Hobbies
st.header("Personal Information")

hobbies = st.text_input(
    "Enter your Hobbies"
)

col1, col2 =st.columns(2)

with col1:
    submit = st.button("Create My protofolio")
with col2:
    cancel= st.button("Cancel")
if submit:
    st.success("protofolio created")
if cancel:
    st.warning("cancel my protofolio")    

