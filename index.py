import streamlit as st

# Page settings
st.set_page_config(
    page_title="plant_bloom 🌸",
    page_icon="🌱",
    layout="centered"
)

# App title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌸 plant_bloom</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Find the perfect plant for your space 🌿</p>", unsafe_allow_html=True)
st.markdown("---")

# Form starts
with st.form("plant_quiz"):
    st.subheader("☀️ 1. How much sunlight does your space get?")
    sunlight = st.radio("", ["Full Sun", "Partial Sun", "Shade"])

    st.subheader("💧 2. How often can you water your plant?")
    watering = st.radio("", ["Daily", "Weekly", "Rarely"])

    st.subheader("🏡 3. Where will you place the plant?")
    location = st.radio("", ["Desk", "Corner", "Balcony"])

    submitted = st.form_submit_button("🌱 Get My Plant")

# Recommendation logic
if submitted:
    st.markdown("---")
    
    if sunlight == "Shade" or watering == "Rarely":
        plant = "🌵 Snake Plant"
        desc = "Thrives in low light and needs very little water. Perfect for beginners!"
        image_url = "https://images.unsplash.com/photo-1616627985881-20baae0d6b8f?auto=format&fit=crop&w=600&q=80"
    
    elif sunlight == "Partial Sun" and watering == "Weekly":
        plant = "🪴 Pothos"
        desc = "Beautiful trailing plant, grows well indoors, easy to care for."
        image_url = "https://images.unsplash.com/photo-1587307367420-0f1c0a3f46c1?auto=format&fit=crop&w=600&q=80"
    
    else:
        plant = "🌼 Peace Lily"
        desc = "Loves bright, indirect light. Purifies air and looks elegant."
        image_url = "https://images.unsplash.com/photo-1609673816742-199dd9e90899?auto=format&fit=crop&w=600&q=80"

    st.success(f"Your Perfect Plant: **{plant}**")
    st.image(image_url, caption=plant, use_column_width=True)
    st.info(desc)

    if st.button("🔁 Try Again"):
        st.experimental_rerun()
