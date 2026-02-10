import streamlit as st
import random

st.title("🏔️ 山泥傾瀉風險評估（雲端版 UI）")

uploaded_file = st.file_uploader("📷 上傳坡面照片", type=["jpg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="已上傳照片", use_column_width=True)

def simulate_ai_photo():
    return random.choice(["無風險", "準備發生", "正在發生"])

ai_result = simulate_ai_photo()
st.write(f"📸 AI 模擬判斷：{ai_result}")

slope = st.slider("📐 坡度角（度）", 0, 60, 30)
soil = st.selectbox("🌱 土壤類型", ["黏土", "砂土", "岩石"])
water = st.slider("💧 含水量（%）", 0, 100, 30)
veg = st.slider("🌳 植被覆蓋率（%）", 0, 100, 50)

def calculate_fs(slope, water):
    return round((1/(1 + water/100)) * (1/(1 + slope/60)), 2)

def calculate_risk_score(slope, soil, water, veg):
    score = 0
    score += 30 if slope > 40 else 20 if slope > 30 else 10
    score += 25 if soil == "黏土" else 15 if soil == "砂土" else 5
    score += 25 if water > 40 else 15 if water > 25 else 5
    score += 20 if veg < 30 else 10 if veg < 60 else 5
    return score

def determine_level(score):
    if score >= 75:
        return "極高風險"
    elif score >= 55:
        return "高風險"
    elif score >= 35:
        return "中風險"
    else:
        return "低風險"

fs = calculate_fs(slope, water)
score = calculate_risk_score(slope, soil, water, veg)
level = determine_level(score)

st.write("---")
st.write(f"📐 穩定係數 Fs ≈ {fs}")
st.write(f"🧮 綜合風險分數：{score}/100")
st.write(f"🚨 最終判定：{level}")
