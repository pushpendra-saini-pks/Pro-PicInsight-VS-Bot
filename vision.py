from dotenv import load_dotenv
load_dotenv()    ## loading all the environment variables

import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSES 
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

## Initialize our Streamlit app 
st.set_page_config(page_title="VS-BOt")

st.header("Pro-PicInsight VS-Bot")
st.subheader("Ask anything about the image with prompt-PicInsight vision-Bot")

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = []


# # Submit button
# if st.button("Tell me anything about the image with **prompt-PicInsight vision-Bot**"):
#     if image is not None:
#         response = get_gemini_response(input_prompt, image)
#         st.session_state.responses.append((input_prompt, image, response))

# Display all previous responses
for idx, (input_prompt, image, response) in enumerate(st.session_state.responses):
    st.subheader(f"Uploaded Pic {idx + 1}")
    if input_prompt:
        st.write(f"**Input Prompt:** {input_prompt}")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write(f"**Insights:** {response}")

# Re-render the input and image upload fields after displaying the responses
st.text_input("Input Prompt: ", key="input_new")
st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="uploaded_file_new")
if st.button("Submit"):
    new_input = st.session_state.input_new
    new_uploaded_file = st.session_state.uploaded_file_new
    if new_uploaded_file is not None:
        new_image = Image.open(new_uploaded_file)
        new_response = get_gemini_response(new_input, new_image)
        st.session_state.responses.append((new_input, new_image, new_response))
        st.experimental_rerun()
