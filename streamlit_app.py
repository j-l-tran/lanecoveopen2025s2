import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text()

components.html(html_content, height=10000, scrolling=True)
