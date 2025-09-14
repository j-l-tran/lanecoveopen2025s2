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
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Title (optional)
st.title("Lane Cove Open 2025 - Season 2")

# Load HTML
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

# Wrap HTML to take full width and height, and remove internal scrolling
full_html = f"""
<style>
html, body, #root {{
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden; /* prevents internal scrolling */
}}
</style>
{html_content}
"""

# Render HTML; set scrolling=False so Streamlit handles it
components.html(full_html, height=st.experimental_get_query_params().get("height", [800])[0], scrolling=False)
