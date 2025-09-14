# streamlit_app.py
import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# --- Streamlit page config ---
st.set_page_config(
    page_title="Lane Cove Open 2025 - Season 2",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title (optional)
st.title("Lane Cove Open 2025 - Season 2")

# Load HTML file
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

# Wrap HTML in a container that fills the iframe
full_html = f"""
<style>
html, body, #root {{
    height: 100%;
    margin: 0;
    padding: 0;
}}
</style>
{html_content}
"""

# Render HTML inside Streamlit
components.html(full_html, height=3000, scrolling=True)
