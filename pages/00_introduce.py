# app.py
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="자기소개 | Profile", page_icon="👋", layout="centered")

st.title("👋 안녕하세요! 저는 ______ 입니다")
st.caption("Streamlit로 만든 간단한 자기소개 웹 앱")

# --- 사이드바: 사진 설정 ---
st.sidebar.header("🖼️ 프로필 사진")
photo_mode = st.sidebar.radio("사진 넣는 방법", ["파일 업로드", "이미지 URL"], horizontal=False)

img = None
if photo_mode == "파일 업로드":
    uploaded = st.sidebar.file_uploader("JPG/PNG 파일을 업로드하세요", type=["jpg", "jpeg", "png"])
    if uploaded is not None:
        img = Image.open(uploaded)
else:
    url = st.sidebar.text_input("이미지 URL", placeholder="https://.../profile.jpg")
    if url:
        try:
            r = requests.get(url, timeout=8)
            r.raise_for_status()
            img = Image.open(BytesIO(r.content))
        except Exception:
            st.sidebar.error("이미지 URL을 불러오지 못했어요. 다른 URL을 넣어주세요.")

# --- 메인: 헤더 + 사진 ---
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    if img is not None:
        st.image(img, caption="Profile Photo", use_container_width=True)
    else:
        st.info("왼쪽 사이드바에서 사진을 업로드하거나 URL을 입력해 주세요.")

with col2:
    st.subheader("🙌 한 줄 소개")
    st.write("반갑습니다! 저는 **문제를 명확히 정의하고 빠르게 실행**하는 것을 좋아해요.")
    st.write("현재는 **______ 분야**에 관심이 많고, **______**을(를) 만들고 있어요.")

st.divider()

# --- 기본 정보 ---
st.subheader("🧾 프로필")
name = st.text_input("이름", value="홍길동")
role = st.text_input("직무/관심 분야", value="데이터 분석가 / ML 엔지니어 (예시)")
location = st.text_input("거주지", value="Seoul, KR")
greeting = st.text_area("간단한 인사말", value="방문해 주셔서 감사합니다! 편하게 연락 주세요 🙂", height=90)

st.markdown(
    f"""
**이름:** {name}  
**분야:** {role}  
**지역:** {location}  

> {greeting}
"""
)

# --- 기술/키워드 ---
st.subheader("🛠️ 기술 스택")
skills = st.multiselect(
    "보유/관심 기술을 선택하세요",
    ["Python", "SQL", "Streamlit", "FastAPI", "React", "Docker", "AWS", "GCP", "PyTorch", "TensorFlow", "Tableau", "Power BI"],
    default=["Python", "Streamlit"],
)
if skills:
    st.write("✅ " + " · ".join(skills))
else:
    st.write("아직 선택된 기술이 없어요.")

# --- 링크 ---
st.subheader("🔗 링크")
c1, c2 = st.columns(2)
with c1:
    github = st.text_input("GitHub", value="https://github.com/yourname")
with c2:
    blog = st.text_input("Blog/Portfolio", value="https://your-site.com")

st.markdown(f"- GitHub: {github}\n- Blog/Portfolio: {blog}")

st.divider()

# --- 연락 ---
st.subheader("✉️ 연락하기")
email = st.text_input("이메일", value="you@example.com")
msg = st.text_area("메시지", placeholder="간단히 남겨주세요!", height=120)

send = st.button("보내기(데모)")
if send:
    if not email.strip():
        st.error("이메일을 입력해 주세요.")
    else:
        # 실제 전송은 하지 않는 데모(개인정보/스팸 방지용)
        st.success("메시지가 저장되었다고 가정할게요! (데모)")
        st.code(f"from={email}\nmessage={msg}")

st.caption("© 2026 • Built with Streamlit")
