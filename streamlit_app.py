# streamlit_app.py
import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Lane Cove Open 2025 - Season 2")

# Load index.html from repo
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

# Render it inside Streamlit
components.html(html_content, height=1200, scrolling=True)
