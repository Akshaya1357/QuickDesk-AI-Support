import streamlit as st
from cohere_config import generate_reply

st.title("🧠 SmartHelp - AI Ticket Assistant")
st.write("Simulate ticket handling with AI-generated replies.")

description = st.text_area("📝 Describe your issue")

if st.button("Generate Reply"):
    if description:
        reply, category = generate_reply(description)
        st.success(f"✅ AI Suggested Reply:\n\n{reply}")
        st.info(f"🗂️ Predicted Category: {category}")
    else:
        st.warning("Please enter a ticket description.")
