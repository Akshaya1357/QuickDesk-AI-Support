import streamlit as st
from cohere_config import generate_reply

st.set_page_config(page_title="SmartHelp AI", layout="centered")

st.title("🧠 SmartHelp - AI Ticket Assistant")
st.write("Get smart, AI-generated replies for support tickets instantly!")

description = st.text_area("📝 Describe your issue", height=150)

if st.button("Generate Reply"):
    if description.strip():
        with st.spinner("Generating smart reply..."):
            reply, category = generate_reply(description)
            st.success(f"✅ AI Suggested Reply:\n\n{reply}")
            st.info(f"🗂️ Predicted Category: {category}")
    else:
        st.warning("Please enter a ticket description to cont

