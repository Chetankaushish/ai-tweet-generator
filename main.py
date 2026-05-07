# ============================================================
# Tweet Generator - Streamlit + Gemini + LangChain
# ============================================================

# --- Imports ---
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# ============================================================
# Page Config
# ============================================================

st.set_page_config(
    page_title="AI Tweet Generator",
    page_icon="🐦"
)

# ============================================================
# API Key
# ============================================================

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# ============================================================
# Gemini Model
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

# ============================================================
# Prompt Template
# ============================================================

tweet_template = """
Generate {number} engaging tweets on the topic: {topic}

Make them:
- Short
- Catchy
- Professional
- Ready for Twitter/X
"""

prompt = PromptTemplate(
    input_variables=["number", "topic"],
    template=tweet_template
)

# ============================================================
# LangChain Chain
# ============================================================

tweet_chain = prompt | llm

# ============================================================
# Streamlit UI
# ============================================================

st.header("🐦 AI Tweet Generator")
st.write("Generate tweets using Gemini AI")

topic = st.text_input("Enter Topic")

number = st.number_input(
    "Number of Tweets",
    min_value=1,
    max_value=10,
    value=1
)

# ============================================================
# Generate Tweets
# ============================================================

if st.button("Generate Tweets"):

    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating Tweets..."):

            response = tweet_chain.invoke({
                "number": number,
                "topic": topic
            })

            st.success("Tweets Generated Successfully!")

            st.write(response.content)
    
