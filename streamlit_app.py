import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# --- Streamlit page config ---
st.set_page_config(
    page_title="Lane Cove Open 2025 - Season 2",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit menu/footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Title (optional)
st.title("Lane Cove Open 2025 - Season 2")

# Load your HTML
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

# Wrap HTML so that it fills the iframe and removes internal scrolling
full_html = f"""
<style>
html, body, #root {{
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden; /* disables internal scrolling */
}}
</style>
{html_content}
"""

# Set a very tall iframe to allow long content to scroll naturally
components.html(full_html, height=10000, scrolling=False)
