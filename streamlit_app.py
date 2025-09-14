import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

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

st.title("Lane Cove Open 2025 - Season 2")

# Load index.html
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

# Wrap HTML to remove internal scrolling
full_html = f"""
<style>
html, body, #root {{
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
}}
</style>
{html_content}
"""

# Use large height so Streamlit handles scrolling naturally
components.html(full_html, height=10000, scrolling=False)
