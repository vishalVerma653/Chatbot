
from dotenv import load_dotenv 
load_dotenv() 
import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-flash-1.5") 
# model = genai.GenerativeModel("gemini-pro") 
model = genai.GenerativeModel("gemini-2.5-flash") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 

st.set_page_config(page_title="QUERY_ BOT")

    #   --- css is start now ---
st.markdown("""
<style>
header{
            visibility: hidden;
    }
.stApp{
   background-color:#F8F9FA;
   text-color:#212529;
}
.stTextInput  input
            {
            color:black ;
            border:2px solid black !important;
            color:black ;
            border-radius:8px;
             border: none;
    box-shadow: none;
    outline: none;        
              }
    # .stTextInput input:focus{
    #         border:2px solid #ccc !important;
    #         color:black !important;
    #         outline:none !important;
    #         }
           
.stTextInput{
        margin-top: 1.5rem;
         }
            .stButton button{
            margin-top:1rem;
         }
.stButton button{
            border:2px solid black;
            # background-color:#ccc;
            
            }
            
</style>
""",unsafe_allow_html=True)
 



st.header("Thunderbolt-Ai") 
input = st.text_input("what's your doubt " , key = "input")  
submit = st.button("Click Here") 

if submit :
    response = my_output(input) 
    st.subheader("Your Response is")
    st.write(response)

