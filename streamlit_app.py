import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# --- Streamlit Page Config ---
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

# Optional page title in Streamlit
st.title("Lane Cove Open 2025 - Season 2")

# Load index.html
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

# Wrap HTML to remove internal scrolling and fill iframe
full_html = f"""
<style>
html, body, #root {{
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden; /* disable internal scrollbars */
}}
</style>
{html_content}
"""

# Set a large height so Streamlit handles scrolling naturally
components.html(full_html, height=10000, scrolling=False)
