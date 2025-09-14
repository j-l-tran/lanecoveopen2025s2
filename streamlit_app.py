import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Lane Cove Open 2025 - Season 2", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit menu/footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load HTML
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

# Wrap HTML to remove internal scrolling and dynamically resize
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

<script>
function sendHeight() {{
    const height = document.body.scrollHeight;
    window.parent.postMessage({{type: 'resize', height: height}}, '*');
}}
window.addEventListener('load', sendHeight);
window.addEventListener('resize', sendHeight);
setInterval(sendHeight, 1000); // update in case content grows dynamically
</script>
"""

# Initially set height large enough
iframe_height = 1000

# Render HTML with scrolling disabled; Streamlit scrollbar handles all scrolling
components.html(full_html, height=iframe_height, scrolling=False)
