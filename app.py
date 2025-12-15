import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import zipfile

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("gemini")

st.set_page_config(page_title="Website Creation", page_icon="🤖")
st.title("Create A Website With One Prompt 😉")

prompt = st.text_area("What is running in your mind?")

if st.button("Send"):
    system_message = """
You are a professional web developer. 
Whenever the user provides a prompt for a website, generate complete, working code.

You MUST output in this EXACT format:

--html--
<full HTML code>
--css--
<full CSS code>
--js--
<full JavaScript code>

No explanation. Just code.
"""

    messages = [
        ("system", system_message),
        ("user", prompt)
    ]

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    response = model.invoke(messages)
    content = response.content

   
    html_code = content.split("--html--")[1].split("--css--")[0].strip()
    css_code = content.split("--css--")[1].split("--js--")[0].strip()
    js_code = content.split("--js--")[1].strip()

    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_code)

    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css_code)

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js_code)

    
    zip_path = "website.zip"
    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    st.success("Files Generated!")

    
    with open(zip_path, "rb") as f:
        st.download_button("Download ZIP", f, file_name="website.zip")
