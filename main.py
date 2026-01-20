# app.py
# Streamlit MBTI 한국어 공부법 추천 웹앱 ✨🇰🇷
# 실행: streamlit run app.py

import random
import textwrap
import streamlit as st

st.set_page_config(
    page_title="✨MBTI 한국어 공부법 추천 | K-Study Spark",
    page_icon="🇰🇷",
    layout="wide",
)

# ----------------------------
# 데이터: MBTI별 추천 (간단하지만 꽤 실용적으로)
# ----------------------------
MBTI_DATA = {
    "INTJ": {
        "tagline": "전략가 🧠📈",
        "core": [
            "학습 로드맵을 먼저 설계하고(4주/8주) 체크리스트로 진행하기 ✅",
            "문법은 ‘규칙 → 예문 → 변형’ 구조로 정리(노션/옵시디언 추천) 🗂️",
            "오답노트는 ‘원인(개념/주의/패턴)’까지 분류해서 재발 방지 🔁",
        ],
        "routine": [
            "20분 문법(개념+예문 5개) → 15분 작문(짧게) → 10분 복습(오답) ⏱️",
            "주 1회 ‘실전 모의(읽기/듣기)’로 진도 검증 📊",
        ],
        "tools": ["Anki(반복학습) 🃏", "Notion/Obsidian 📚", "TOPIK 기출 🔥"],
        "mission": ["오늘은 연결어미 3개로 5문장 만들기 🔗", "뉴스 1문단 요약하고 키워드 5개 뽑기 🗞️"],
    },
    "INTP": {
        "tagline": "논리 탐구자 🔍💡",
        "core": [
            "‘왜 이런 표현을 쓰지?’를 파고드는 ‘질문 노트’를 만들기 ❓",
            "문법을 ‘개념 맵(도식)’으로 연결해서 체계화하기 🧩",
            "한 문장을 여러 버전으로 바꿔보며 변형 놀이하기 🎛️",
        ],
        "routine": [
            "15분 탐구(문법/표현) → 15분 예문 변형 10개 → 10분 스피킹(혼잣말) 🎙️",
            "주 2회 좋아하는 주제(게임/과학/영화)로 글 150자 쓰기 📝",
        ],
        "tools": ["개념도 도구(Miro 등) 🗺️", "YouTube 자막 학습 🎬", "사전/용례 검색 🔎"],
        "mission": ["‘-잖아(요)’로 상황 3개 만들기 😄", "한 문장에 높임 표현 2개 넣어보기 🙇"],
    },
    "ENTJ": {
        "tagline": "리더형 🚀🏆",
        "core": [
            "목표를 수치화: ‘TOPIK 점수/말하기 3분/작문 200자’ 🎯",
            "시간을 블록으로 쪼개서 ‘훈련’처럼 진행(루틴화) 🧱",
            "피드백을 빨리 받는 구조(튜터/교환 파트너) 만들기 🤝",
        ],
        "routine": [
            "10분 듣기 쉐도잉 → 15분 말하기(타이머) → 15분 작문(템플릿) 🕒",
            "주 1회 ‘발표’(3분 스피치) 녹음 후 개선 포인트 3개 기록 🎤",
        ],
        "tools": ["스피치 타이머 ⏲️", "녹음 앱 🎧", "교정(튜터/언어교환) 🧑‍🏫"],
        "mission": ["오늘 ‘설득’ 주제로 60초 스피치 녹음하기 📣", "자주 틀리는 조사 5개만 집중 교정 🧷"],
    },
    "ENTP": {
        "tagline": "아이디어 폭발 💥😎",
        "core": [
            "토론/밈/드라마로 ‘재밌게’ 몰입하기 🎭",
            "새 표현을 바로 ‘드립/대화’에 써서 내 것으로 만들기 🗣️",
            "한 주제에 대해 찬반 5개씩 말해보기(순발력 훈련) ⚡",
        ],
        "routine": [
            "10분 짧은 영상(자막) → 10분 표현 뽑기 → 15분 즉흥 스피킹 🎬🎙️",
            "주 2회 ‘토론 카드’로 스피킹 배틀(혼자도 가능) 🃏",
        ],
        "tools": ["짧은 클립(쇼츠) 📱", "대화 주제 카드 💬", "표현 수집 노트 ✍️"],
        "mission": ["오늘 유행어 1개를 상황극으로 3번 쓰기 🤣", "‘근데/그래서/아무튼’으로 이야기 이어가기 🧵"],
    },

    "INFJ": {
        "tagline": "깊은 공감 🌙💞",
        "core": [
            "감정/의미 중심으로 단어를 익히기(예: ‘그리움’, ‘뭉클하다’) 🥹",
            "일기/편지 형태로 자연스럽게 작문하기 ✉️",
            "대화에서는 ‘공감 표현 세트’를 만들어두기 🙌",
        ],
        "routine": [
            "10분 감정 어휘 → 15분 일기 5문장 → 10분 소리 내어 읽기 📖",
            "주 1회 ‘짧은 편지’ 쓰고 표현 5개 리사이클 ♻️",
        ],
        "tools": ["감정 어휘 리스트 💗", "일기 템플릿 📓", "낭독/쉐도잉 🎧"],
        "mission": ["‘마음이 놓이다/뭉클하다’로 문장 3개 만들기 💓", "오늘 고마웠던 일 3개를 한국어로 적기 🌷"],
    },
    "INFP": {
        "tagline": "감성 창작자 🎨🦋",
        "core": [
            "좋아하는 노래/시/드라마 대사를 ‘나만의 문장’으로 재창작하기 🎶",
            "단어는 스토리로 묶기(캐릭터/장면) 🧚",
            "완벽주의 금지! ‘초안 → 다듬기’로 진행하기 ✨",
        ],
        "routine": [
            "10분 대사 따라쓰기 → 15분 내 버전으로 바꾸기 → 10분 읽기/발음 🌈",
            "주 1회 ‘짧은 창작’(100~150자) 업그레이드 🚀",
        ],
        "tools": ["드라마 대사 캡처 🖼️", "가사/대사 노트 🎵", "표현 스티커북 🧷"],
        "mission": ["오늘 좋아하는 장면을 5문장으로 요약하기 🎬", "‘~같다’ 비유로 문장 3개 만들기 🌟"],
    },
    "ENFJ": {
        "tagline": "따뜻한 코치 🤗🌟",
        "core": [
            "스터디/친구와 함께 ‘상호 피드백’ 구조 만들기 👥",
            "설명하는 방식으로 배우기(누군가에게 가르친다고 생각) 🧑‍🏫",
            "정중/배려 표현을 ‘상황별’로 세트화하기 🙇‍♀️",
        ],
        "routine": [
            "10분 표현 암기 → 10분 롤플레이 → 15분 대화/피드백 🗣️",
            "주 1회 ‘상황극’(카페/면접/병원) 완성하기 🏥☕",
        ],
        "tools": ["역할극 스크립트 🎭", "피드백 체크리스트 ✅", "언어교환 🤝"],
        "mission": ["‘혹시 ~해도 될까요?’로 요청 5개 만들기 🙏", "칭찬 표현 5개를 실제 대화에 쓰기 🌼"],
    },
    "ENFP": {
        "tagline": "에너지 요정 🧡✨",
        "core": [
            "짧고 재미있는 콘텐츠로 ‘자주’ 노출(짧은 학습의 누적) 📱",
            "단어는 이미지/이모지와 함께 외우기 🧠💫",
            "대화는 ‘즉흥’이 강점! 말하면서 부족한 걸 채우기 🗣️",
        ],
        "routine": [
            "7분 쇼츠 → 8분 표현 5개 → 10분 말하기(주제 1개) ⚡",
            "주 2회 ‘나의 하루 브이로그’처럼 60초 말하기 🎥",
        ],
        "tools": ["이모지 단어장 😄", "짧은 영상 📺", "보이스 노트 🎙️"],
        "mission": ["오늘 기분을 표현하는 형용사 5개 쓰기 😆😮‍💨😍", "‘진짜/완전/엄청’ 강조 표현을 문장에 넣기 💥"],
    },

    "ISTJ": {
        "tagline": "성실한 관리자 📚🧾",
        "core": [
            "교재/기출 기반으로 ‘정석 루트’로 가기 📘",
            "매일 같은 시간에 같은 분량(꾸준함 = 최강) 🧱",
            "문법은 표로 정리하고 예문은 최소 10개 반복 🔁",
        ],
        "routine": [
            "20분 문법+연습문제 → 10분 단어 → 10분 복습(전날 오답) 🧠",
            "주 1회 누적 테스트(단어/문법) 📑",
        ],
        "tools": ["교재(단계별) 📗", "오답노트 🧷", "기출/모의고사 📝"],
        "mission": ["조사 ‘은/는, 이/가’ 예문 10개 만들기 🧩", "오늘 배운 문법으로 5문장 작문 📌"],
    },
    "ISFJ": {
        "tagline": "배려의 수호자 🫶🏡",
        "core": [
            "실생활 상황(마트/카페/전화) 중심으로 표현 학습하기 🛒☎️",
            "대화 스크립트를 만들어 안전하게 연습하기 🛡️",
            "‘정중한 말투’/‘완곡 표현’을 세트로 익히기 💐",
        ],
        "routine": [
            "10분 상황 표현 → 15분 스크립트 읽기 → 10분 따라 말하기 🎧",
            "주 1회 실제 상황 롤플레이(길 묻기/주문하기) 🗺️",
        ],
        "tools": ["상황별 표현집 📒", "대화 스크립트 🎭", "문장 패턴 카드 🃏"],
        "mission": ["‘죄송하지만~’으로 문장 3개 만들기 🙇", "주문 상황(카페) 스크립트 1개 완성 ☕"],
    },
    "ESTJ": {
        "tagline": "현실 리더 🧑‍💼📌",
        "core": [
            "성과 중심: ‘오늘 목표 3개’ 체크하며 진행 ✅✅✅",
            "말하기는 ‘템플릿’으로 빠르게 안정화(도입-근거-결론) 🧩",
            "틀리는 포인트를 규칙으로 못 박아 수정하기 🛠️",
        ],
        "routine": [
            "10분 단어(업무/생활) → 15분 말하기 템플릿 → 10분 듣기 📞",
            "주 1회 ‘업무/공식’ 문장 교정 받기 🧑‍🏫",
        ],
        "tools": ["스피킹 템플릿 📋", "체크리스트 ✅", "공식 이메일/문장 예시 📧"],
        "mission": ["‘요청 메일’ 5문장 작성하기 📩", "‘하지만/따라서’로 논리 연결 5문장 🔗"],
    },
    "ESFJ": {
        "tagline": "사교 만렙 🥳💬",
        "core": [
            "대화에서 자주 쓰는 ‘리액션 표현’부터 마스터하기 😆",
            "관계/예절 표현(안부, 감사, 사과)을 상황별로 익히기 🌷",
            "스터디/친구와 ‘정기 대화’로 유지하기 📅",
        ],
        "routine": [
            "10분 리액션 표현 → 15분 역할극 → 10분 단어(관계/모임) 🎉",
            "주 1회 ‘모임/약속’ 대화 시나리오 2개 만들기 🗓️",
        ],
        "tools": ["리액션 표현 리스트 😮😍", "롤플레이 카드 🎴", "대화 파트너 🤝"],
        "mission": ["‘맞아/진짜?/대박’ 리액션 10개 말해보기 🤩", "안부 묻기 표현 5개 만들기 🌤️"],
    },

    "ISTP": {
        "tagline": "실전 장인 🛠️😼",
        "core": [
            "설명보다 ‘바로 써먹기’: 패턴 1개 = 문장 10개 🔥",
            "발음/억양은 짧게 녹음→비교→수정 루프 🔁",
            "불필요한 암기 줄이고 자주 쓰는 것만 압축 🎯",
        ],
        "routine": [
            "10분 패턴 → 10분 즉시 문장 생산(10개) → 10분 발음 교정 🎙️",
            "주 2회 실전 대화(주문/길/약속)만 집중 🧭",
        ],
        "tools": ["보이스 레코더 🎧", "패턴 카드 🃏", "짧은 실전 회화 📞"],
        "mission": ["‘~할게요’로 약속 문장 10개 만들기 🤝", "발음 어려운 단어 10개 녹음 비교 🎤"],
    },
    "ISFP": {
        "tagline": "감각 예술가 🌿🎧",
        "core": [
            "사진/풍경/카페 메뉴로 ‘감각 단어’ 확장하기 📸",
            "짧은 문장부터 예쁘게 말하기(자연스러운 톤) 🌸",
            "취향 콘텐츠로 꾸준히(음악/브이로그/요리) 🍳🎶",
        ],
        "routine": [
            "10분 콘텐츠 감상 → 10분 표현 5개 → 10분 내 일상 묘사 🌿",
            "주 1회 ‘내가 좋아하는 것’ 소개 글 120자 ✨",
        ],
        "tools": ["사진 기반 단어장 📷", "브이로그 🎥", "표현 스크랩북 📒"],
        "mission": ["오늘 본 풍경을 5문장으로 묘사하기 🌅", "‘~스럽다’로 성격/분위기 표현 3개 만들기 🌼"],
    },
    "ESTP": {
        "tagline": "액션 히어로 🏃‍♂️🔥",
        "core": [
            "현장형 학습: 실제 상황에서 써보고 고치기 🧯",
            "짧고 강한 반복(스피드 런)으로 감각 만들기 ⚡",
            "대화는 ‘먼저 말하기’가 답! (틀려도 GO) 😎",
        ],
        "routine": [
            "5분 표현 → 10분 즉시 말하기 → 10분 듣고 따라하기 → 5분 정리 🏎️",
            "주 2회 ‘미션 대화’(카페 주문, 약속 잡기) 수행 🧩",
        ],
        "tools": ["미션 카드 🎯", "짧은 회화 클립 📱", "실전 체크리스트 ✅"],
        "mission": ["‘지금/바로/일단’으로 문장 5개 만들기 ⚡", "카페 주문 30초 스피치 녹음하기 ☕🎙️"],
    },
    "ESFP": {
        "tagline": "무드 메이커 🎉💖",
        "core": [
            "즐기는 게 실력! 대화/노래/드라마로 자연스럽게 🕺",
            "표현은 ‘리액션+감탄’ 중심으로 빠르게 늘리기 😍",
            "친구와 ‘주제 챌린지’로 말하기 유지하기 🫶",
        ],
        "routine": [
            "7분 콘텐츠 → 8분 표현 5개 → 10분 수다(주제 1개) 🗣️",
            "주 1회 ‘내 주말’ 1분 말하기 + 이모지 요약 😆📌",
        ],
        "tools": ["대화 주제 룰렛 🎡", "가사/대사 따라부르기 🎤", "리액션 표현 😮"],
        "mission": ["감탄사 10개로 짧은 상황극 하기 🤩", "‘너무/진짜’ 강조로 문장 5개 만들기 💥"],
    },

    "INJ": {},  # (안전장치용: 잘못된 값 들어와도 크래시 방지)
}

# MBTI 16개 보장
ALL_MBTI = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP",
]

DEFAULT_DATA = {
    "tagline": "너만의 스타일 🌈",
    "core": ["꾸준함 + 재미 + 피드백 3콤보로 가면 무조건 는다 💪✨"],
    "routine": ["10분이라도 매일! 짧게 자주가 최고 🔁"],
    "tools": ["단어장 📒", "녹음 🎙️", "자막 콘텐츠 🎬"],
    "mission": ["오늘 배운 표현 3개를 바로 말해보기 🗣️"],
}

# ----------------------------
# 테마(팔레트) + CSS
# ----------------------------
THEMES = {
    "🌌 네온 나이트": {
        "bg1": "#0b1026",
        "bg2": "#220a3d",
        "card": "rgba(255,255,255,0.08)",
        "card2": "rgba(255,255,255,0.06)",
        "text": "#f5f7ff",
        "muted": "rgba(245,247,255,0.75)",
        "accent": "#7CFFCB",
        "accent2": "#A78BFA",
        "border": "rgba(255,255,255,0.14)",
        "shadow": "0 12px 30px rgba(0,0,0,0.35)",
    },
    "🍬 캔디 팝": {
        "bg1": "#ff4d9d",
        "bg2": "#6a5cff",
        "card": "rgba(255,255,255,0.18)",
        "card2": "rgba(255,255,255,0.12)",
        "text": "#ffffff",
        "muted": "rgba(255,255,255,0.82)",
        "accent": "#00f5d4",
        "accent2": "#ffd166",
        "border": "rgba(255,255,255,0.22)",
        "shadow": "0 14px 34px rgba(0,0,0,0.25)",
    },
    "🌿 파스텔 그린": {
        "bg1": "#0ea5a4",
        "bg2": "#22c55e",
        "card": "rgba(255,255,255,0.18)",
        "card2": "rgba(255,255,255,0.12)",
        "text": "#f8fffe",
        "muted": "rgba(248,255,254,0.82)",
        "accent": "#fff1a6",
        "accent2": "#ffd1dc",
        "border": "rgba(255,255,255,0.22)",
        "shadow": "0 14px 34px rgba(0,0,0,0.22)",
    },
}

def inject_css(p):
    st.markdown(
        f"""
        <style>
        /* 전체 배경 */
        .stApp {{
            background: radial-gradient(1200px 700px at 10% 10%, {p["bg2"]} 0%, transparent 60%),
                        radial-gradient(900px 600px at 90% 20%, {p["accent2"]}33 0%, transparent 65%),
                        linear-gradient(135deg, {p["bg1"]} 0%, {p["bg2"]} 100%);
            color: {p["text"]};
        }}

        /* 기본 폰트 느낌 */
        html, body, [class*="css"] {{
            font-family: ui-sans-serif, system-ui, -apple-system, "Apple SD Gothic Neo", "Noto Sans KR", "Segoe UI", Roboto, Helvetica, Arial, "Noto Color Emoji";
        }}

        /* 헤더 글로우 */
        .hero-title {{
            font-weight: 900;
            letter-spacing: -0.6px;
            line-height: 1.05;
            font-size: clamp(2rem, 2.8vw, 3.2rem);
            text-shadow: 0 0 18px {p["accent"]}33;
            margin-bottom: 0.35rem;
        }}
        .hero-sub {{
            color: {p["muted"]};
            font-size: 1.05rem;
            margin-top: 0;
        }}

        /* 카드 */
        .glass {{
            background: {p["card"]};
            border: 1px solid {p["border"]};
            box-shadow: {p["shadow"]};
            border-radius: 22px;
            padding: 18px 18px;
            backdrop-filter: blur(12px);
        }}
        .glass2 {{
            background: {p["card2"]};
            border: 1px solid {p["border"]};
            box-shadow: {p["shadow"]};
            border-radius: 18px;
            padding: 14px 14px;
            backdrop-filter: blur(10px);
        }}

        /* 배지 */
        .badge {{
            display:inline-block;
            padding: 6px 12px;
            border-radius: 999px;
            background: linear-gradient(90deg, {p["accent"]}66, {p["accent2"]}66);
            border: 1px solid {p["border"]};
            color: {p["text"]};
            font-weight: 800;
            font-size: 0.95rem;
        }}

        /* 구분선 느낌 */
        .divider {{
            height: 1px;
            background: linear-gradient(90deg, transparent, {p["border"]}, transparent);
            margin: 10px 0 14px 0;
        }}

        /* 버튼 약간 화려하게 */
        div.stButton > button {{
            border-radius: 999px !important;
            border: 1px solid {p["border"]} !important;
            padding: 0.65rem 1.0rem !important;
            font-weight: 800 !important;
            box-shadow: 0 10px 22px rgba(0,0,0,0.18) !important;
            background: linear-gradient(90deg, {p["accent"]}AA, {p["accent2"]}AA) !important;
            color: #0b1026 !important;
        }}
        div.stButton > button:hover {{
            transform: translateY(-1px);
        }}

        /* 탭 글씨 */
        .stTabs [data-baseweb="tab"] {{
            font-weight: 800;
        }}

        /* 사이드바도 살짝 글래스 */
        section[data-testid="stSidebar"] > div {{
            background: linear-gradient(180deg, {p["card"]}, transparent);
            border-right: 1px solid {p["border"]};
        }}

        /* 입력 박스 라운드 */
        .stTextInput input, .stSelectbox > div, .stRadio > div {{
            border-radius: 14px !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def get_mbti_payload(mbti: str):
    if mbti in MBTI_DATA and MBTI_DATA[mbti]:
        return MBTI_DATA[mbti]
    return DEFAULT_DATA

def bullet_list(items):
    return "\n".join([f"- {x}" for x in items])

def nice_block(title, emoji, body_md):
    st.markdown(
        f"""
        <div class="glass2">
          <div class="badge">{emoji} {title}</div>
          <div class="divider"></div>
          <div style="color: inherit; font-size: 1.02rem; line-height:1.65">
            {body_md}
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def make_example_sentences(style_hint: str):
    # 아주 간단한 예문 생성(템플릿 기반)
    starters = [
        "요즘 저는", "오늘은", "사실 저는", "저는 보통", "어제는", "다음 주에는"
    ]
    topics = [
        "한국어 공부를", "발음을", "듣기 연습을", "단어 암기를", "말하기를", "작문을"
    ]
    patterns = [
        "더 꾸준히 해보려고 해요.",
        "조금 더 재미있게 하고 싶어요.",
        "매일 10분이라도 하려고요.",
        "실수해도 괜찮으니까 계속 말해볼게요.",
        "오늘 배운 표현을 바로 써볼 거예요.",
        "제 방식으로 정리해보려 해요.",
    ]
    random.shuffle(starters)
    random.shuffle(topics)
    random.shuffle(patterns)
    sents = [f"{starters[i]} {topics[i]} {patterns[i]}" for i in range(5)]
    sents.append(f"👉 {style_hint} 그래서 오늘 미션을 꼭 달성할 거예요! 🔥")
    return sents

# ----------------------------
# 사이드바
# ----------------------------
with st.sidebar:
    st.markdown("## ⚙️ 설정 메뉴")
    theme_name = st.radio("🎨 테마 선택", list(THEMES.keys()), index=0)
    st.markdown("---")
    mbti = st.selectbox("🧩 MBTI를 선택해줘!", ALL_MBTI, index=0)
    fun_mode = st.toggle("✨ 파티클 모드(풍선/눈)", value=True)
    st.caption("💡 팁: MBTI는 참고용! 그래도 꽤 찰떡 추천 나옴 😎")

palette = THEMES[theme_name]
inject_css(palette)

# ----------------------------
# 헤더(히어로)
# ----------------------------
left, right = st.columns([1.35, 1], vertical_alignment="top")

with left:
    st.markdown(
        """
        <div class="glass">
          <div class="hero-title">✨ K-Study Spark 🇰🇷<br/>MBTI 맞춤 한국어 공부법 추천</div>
          <p class="hero-sub">
            MBTI를 고르면 <b>딱 맞는 학습 루틴</b> + <b>추천 자료</b> + <b>예문</b> + <b>미니 퀴즈</b>까지!<br/>
            이모지 듬뿍 😆🌈🔥 화려하게 가자!
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    payload = get_mbti_payload(mbti)
    st.markdown(
        f"""
        <div class="glass">
          <div class="badge">🧬 선택된 MBTI: {mbti} · {payload["tagline"]}</div>
          <div class="divider"></div>
          <div style="font-size:1.05rem; color:{palette["muted"]}; line-height:1.6">
            오늘도 한국어 레벨업 가보자! 💪📚<br/>
            아래에서 <b>맞춤 추천</b>을 확인해줘 😼✨
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")  # 약간의 여백

# ----------------------------
# 액션 버튼
# ----------------------------
c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
with c1:
    if st.button("💎 추천 뽑기! (화려하게)"):
        if fun_mode:
            random.choice([st.balloons, st.snow])()
        st.toast("✨ 추천 생성 완료! 아래로 내려가 봐 😆", icon="✅") if hasattr(st, "toast") else None
with c2:
    if st.button("🎲 오늘의 미션 랜덤"):
        payload = get_mbti_payload(mbti)
        m = random.choice(payload.get("mission", DEFAULT_DATA["mission"]))
        st.session_state["daily_mission"] = m
with c3:
    if st.button("🧠 학습 점수 +1"):
        st.session_state["score"] = st.session_state.get("score", 0) + 1
with c4:
    if st.button("🧼 점수 리셋"):
        st.session_state["score"] = 0

score = st.session_state.get("score", 0)
mission = st.session_state.get("daily_mission", "🎯 아직 미션이 없어요! ‘오늘의 미션 랜덤’을 눌러줘 😆")

m1, m2, m3 = st.columns(3)
m1.metric("🔥 오늘의 학습 점수", score, delta=None)
m2.metric("⏱️ 추천 집중 시간", f"{min(60, 10 + score*3)}분", delta=None)
m3.metric("🎯 오늘의 미션", "READY ✅" if "아직" not in mission else "WAIT ⏳", delta=None)

st.markdown(
    f"""
    <div class="glass2">
      <div class="badge">🎯 오늘의 미션</div>
      <div class="divider"></div>
      <div style="font-size:1.05rem; line-height:1.65">{mission}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ----------------------------
# 메인 추천 탭
# ----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["💡 공부법 추천", "🧰 루틴 & 자료", "📝 예문 생성", "🧪 미니 퀴즈"])

payload = get_mbti_payload(mbti)

with tab1:
    colA, colB = st.columns([1.1, 0.9], vertical_alignment="top")
    with colA:
        nice_block(
            "핵심 전략",
            "💡",
            bullet_list(payload["core"]).replace("\n", "<br/>"),
        )
        st.write("")
        nice_block(
            "하루 루틴(추천)",
            "⏰",
            bullet_list(payload["routine"]).replace("\n", "<br/>"),
        )
    with colB:
        st.markdown(
            f"""
            <div class="glass2">
              <div class="badge">✨ 너에게 특히 잘 맞는 포인트</div>
              <div class="divider"></div>
              <ul style="margin-top:0; line-height:1.75">
                <li>강점 살리기: <b>{payload["tagline"]}</b>의 스타일로 몰입 🎯</li>
                <li>약점 보완: <b>피드백</b> + <b>반복</b>으로 안정감 업 🔁</li>
                <li>성장 키: <b>‘짧게 자주’</b> + <b>‘바로 써먹기’</b> ⚡</li>
              </ul>
              <div class="divider"></div>
              <div style="color:{palette["muted"]}; font-size:0.98rem">
                📌 TIP: 오늘 추천에서 마음에 드는 것 <b>딱 1개</b>만 골라서 바로 실행하면 성공 확률이 급상승! 🚀
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )

with tab2:
    cA, cB = st.columns([1, 1], vertical_alignment="top")
    with cA:
        nice_block(
            "추천 도구/자료",
            "🧰",
            bullet_list(payload["tools"]).replace("\n", "<br/>"),
        )
        st.write("")
        st.markdown(
            """
            <div class="glass2">
              <div class="badge">📚 상황별 추천(공통)</div>
              <div class="divider"></div>
              <ul style="margin-top:0; line-height:1.75">
                <li>듣기 🎧: 자막 있는 영상 → 자막 끄기 → 쉐도잉</li>
                <li>말하기 🎙️: 30초 녹음 → 다시 듣기 → 1문장 개선</li>
                <li>문법 📘: 규칙 1개 → 예문 5개 → 변형 10개</li>
                <li>단어 🧠: ‘문장 속 단어’로 외우기(단독 암기 최소화)</li>
              </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    with cB:
        st.markdown(
            """
            <div class="glass2">
              <div class="badge">🗓️ 7일 스파클 플랜</div>
              <div class="divider"></div>
              <div style="line-height:1.75">
                <b>Day 1</b> 🔥 패턴 1개 + 예문 10개<br/>
                <b>Day 2</b> 🎧 듣기 쉐도잉 10분 + 발음 5개 교정<br/>
                <b>Day 3</b> 📝 일기 5문장(오늘 기분 포함 😆)<br/>
                <b>Day 4</b> 🗣️ 60초 스피치(주제: 내 취미) 녹음<br/>
                <b>Day 5</b> 📚 읽기 1문단 요약 + 키워드 5개<br/>
                <b>Day 6</b> 🎭 역할극(카페/면접/병원 중 택1)<br/>
                <b>Day 7</b> 🏁 미니 모의: 듣기 5문항 + 작문 100자
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        progress = min(1.0, score / 10.0)
        st.progress(progress, text=f"✨ 오늘의 성장 게이지: {int(progress*100)}%")

with tab3:
    hint = f"{payload['tagline']} 스타일로 ‘짧게 자주 + 바로 써먹기’ 💥"
    sents = make_example_sentences(hint)

    st.markdown(
        f"""
        <div class="glass2">
          <div class="badge">📝 예문 자동 생성</div>
          <div class="divider"></div>
          <div style="color:{palette["muted"]}; line-height:1.6">
            아래 예문을 소리 내어 읽고(📢) 마음에 드는 문장을 <b>내 상황</b>으로 바꿔 말해봐! 😆
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    ex_col1, ex_col2 = st.columns([1, 1], vertical_alignment="top")
    with ex_col1:
        st.markdown("### 📌 오늘의 예문 1~3")
        for i in range(3):
            st.info(f"**{i+1}.** {sents[i]}")

    with ex_col2:
        st.markdown("### 🌟 오늘의 예문 4~6")
        for i in range(3, 6):
            st.success(f"**{i+1}.** {sents[i]}")

    st.write("")
    st.markdown("### ✍️ 내 문장 만들기 (바로 연습!)")
    user_text = st.text_area("여기에 너만의 문장을 적어봐 😼✨", height=120, placeholder="예: 요즘 저는 발음을 더 꾸준히 해보려고 해요!")
    if st.button("🧁 문장 꾸미기 팁 받기"):
        tips = [
            "✨ ‘그래서/하지만/게다가’로 문장 연결하면 더 자연스러워져!",
            "✨ ‘~거든요/~잖아요’ 넣으면 말투가 더 한국어스러워져!",
            "✨ ‘조금/진짜/완전/엄청’ 같은 부사를 살짝 넣어봐!",
            "✨ 존댓말/반말 톤을 한 번 정하고 끝까지 유지하면 깔끔해!",
        ]
        st.markdown(f"**추천 팁 🎁**: {random.choice(tips)}")

    if user_text.strip():
        st.markdown(
            f"""
            <div class="glass2">
              <div class="badge">🪄 너의 문장</div>
              <div class="divider"></div>
              <div style="font-size:1.08rem; line-height:1.75">{user_text.strip()}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

with tab4:
    st.markdown(
        """
        <div class="glass2">
          <div class="badge">🧪 미니 퀴즈(가볍게 레벨업)</div>
          <div class="divider"></div>
          <div style="line-height:1.7">
            부담 ㄴㄴ 😆 틀려도 괜찮아! 바로 배우면 됨 🔥
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")

    # 간단 퀴즈(공통)
    questions = [
        {
            "q": "‘가능하면’과 가장 비슷한 뜻은? 🤔",
            "opts": ["되도록", "갑자기", "이미", "특히"],
            "a": "되도록",
            "explain": "‘가능하면’ = ‘되도록/될 수 있으면’ 👍"
        },
        {
            "q": "다음 중 가장 자연스러운 문장은? ✨",
            "opts": [
                "저는 한국어를 공부가 해요.",
                "저는 한국어를 공부해요.",
                "저는 공부 한국어해요.",
                "저는 한국어가 공부해요."
            ],
            "a": "저는 한국어를 공부해요.",
            "explain": "목적격 조사 ‘를’ + 동사 ‘공부해요’가 자연스러워요 ✅"
        },
        {
            "q": "‘~(으)려고’의 의미는? 🎯",
            "opts": ["추측", "의도/계획", "원인", "대조"],
            "a": "의도/계획",
            "explain": "‘~(으)려고’는 ‘하려고 해요’처럼 의도/계획을 나타내요 🗓️"
        }
    ]

    correct = 0
    user_answers = []
    for idx, item in enumerate(questions, start=1):
        st.markdown(f"### Q{idx}. {item['q']}")
        ans = st.radio("선택해줘 👇", item["opts"], key=f"quiz_{idx}", horizontal=True)
        user_answers.append((ans, item["a"], item["explain"]))
        st.write("")

    if st.button("✅ 채점하기"):
        for ans, a, _ in user_answers:
            if ans == a:
                correct += 1
        st.session_state["score"] = st.session_state.get("score", 0) + correct

        st.markdown(
            f"""
            <div class="glass2">
              <div class="badge">🏁 결과</div>
              <div class="divider"></div>
              <div style="font-size:1.15rem; line-height:1.7">
                정답: <b>{correct}</b> / {len(questions)} 🎉<br/>
                학습 점수에 <b>+{correct}</b> 추가됨! 🔥
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for i, (ans, a, exp) in enumerate(user_answers, start=1):
            if ans == a:
                st.success(f"Q{i} ✅ 정답! ({ans}) — {exp}")
            else:
                st.error(f"Q{i} ❌ 오답! (너의 답: {ans} / 정답: {a}) — {exp}")

# ----------------------------
# 푸터
# ----------------------------
st.write("")
st.markdown(
    """
    <div class="glass" style="text-align:center">
      <div style="font-size:1.05rem; font-weight:800">
        ✨ 오늘도 스파클하게 레벨업! 🇰🇷🔥
      </div>
      <div style="color: rgba(255,255,255,0.80); margin-top:6px">
        원하면 다음 단계도 만들어줄게: ✅ 회원가입/저장, ✅ 학습 히스토리, ✅ 레벨 테스트, ✅ TOPIK 모드, ✅ 단어장(Anki export) 😎
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
