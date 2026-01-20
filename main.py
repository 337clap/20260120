# app.py
import streamlit as st
from dataclasses import dataclass
from typing import Dict, List

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="✨ MBTI 한국어 공부법 추천 | K-Study Genie",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# Fancy CSS
# ----------------------------
CUSTOM_CSS = """
<style>
/* Base */
html, body, [class*="css"]  {
  font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', Arial, sans-serif;
}
.main {
  background: radial-gradient(circle at 10% 10%, rgba(255, 107, 129, 0.18), transparent 40%),
              radial-gradient(circle at 90% 20%, rgba(72, 219, 251, 0.18), transparent 45%),
              radial-gradient(circle at 30% 90%, rgba(29, 209, 161, 0.18), transparent 45%),
              linear-gradient(135deg, rgba(142, 68, 173, 0.10), rgba(52, 152, 219, 0.08), rgba(46, 204,
