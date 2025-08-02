import streamlit as st
from openai_config import generate_reply

st.set_page_config(page_title="SmartHelp AI", page_icon="🤖")

st.title("🧠 SmartHelp - AI Ticket Assistant")
st.write("Simulate ticket handling with AI-generated responses.")

st.subheader("📩 Submit a Support Ticket")
subject = st.text_input("Subject")
description = st.text_area("Describe your issue")

if st.button("Generate AI Reply"):
    if description.strip():
        ai_response, category = generate_reply(description)
        st.success("✅ AI Suggested Reply:")
        st.write(ai_response)

        st.info(f"🗂️ Predicted Category: **{category}**")
    else:
        st.warning("Please enter a ticket description.")
