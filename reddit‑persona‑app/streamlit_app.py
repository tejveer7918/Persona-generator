import streamlit as st
import requests
from backend.render_template import render_persona_html
from html2image import Html2Image  # Make sure 'html2image' is installed in your environment
from io import BytesIO
import os

st.set_page_config(page_title="Reddit Persona Generator", layout="centered")
st.title("🧠 Reddit Persona Generator")
st.caption("Paste a Reddit profile URL below and generate a visual persona.")

API_URL = "http://localhost:8000/persona"

profile_url = st.text_input("🔗 Reddit Profile URL", placeholder="e.g. https://www.reddit.com/user/Hungry-Move-6603")

if st.button("Generate Persona"):
    if not profile_url.strip():
        st.warning("⚠️ Please enter a Reddit profile URL.")
    else:
        username = profile_url.rstrip("/").split("/")[-1]
        with st.spinner("🔍 Generating persona..."):
            try:
                response = requests.get(API_URL, params={"username": username})
                if response.status_code == 200:
                    persona = response.json()
                    html_str = render_persona_html(persona)

                    hti = Html2Image()
                    img_name = f"{username}_persona.png"
                    hti.screenshot(
                        html_str=html_str,
                        save_as=img_name,
                        size=(850, 1100)
                    )

                    st.image(img_name, caption="Persona Card", use_column_width=True)

                    with open(img_name, "rb") as f:
                        st.download_button(
                            label="📸 Download as PNG",
                            data=f,
                            file_name=img_name,
                            mime="image/png"
                        )
                else:
                    st.error(f"❌ API Error {response.status_code}: Failed to generate persona.")
            except Exception as e:
                st.exception(e)
