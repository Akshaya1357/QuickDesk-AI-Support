import streamlit as st
from openai_config import generate_reply

st.set_page_config(page_title="SmartHelp AI", page_icon="🤖")

st.title("🧠 SmartHelp - AI Ticket Assistant")
st.write("Simulate ticket handling with AI-generated replies.")

description = st.text_area("📝 Describe your issue")

if st.button("Generate AI Reply"):
    if description.strip():
        reply, category = generate_reply(description)
        st.success("✅ AI Suggested Reply:")
        st.write(reply)
        st.info(f"🗂️ Predicted Category: **{category}**")
    else:
        st.warning("Please describe your problem above.")
