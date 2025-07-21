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

# Result logic
if submitted:
    st.markdown("---")
    if sunlight == "Shade" or watering == "Rarely":
        plant = "🌵 Snake Plant"
        desc = "Thrives in low light and needs very little water. Perfect for beginners!"
        image_url = "https://i.pinimg.com/564x/b7/bc/6e/b7bc6ebcbd6b03d7e5f733c3ffb7dbcd.jpg"
    elif sunlight == "Partial Sun" and watering == "Weekly":
        plant = "🪴 Pothos"
        desc = "Beautiful trailing plant, grows well indoors, easy to care for."
        image_url = "feey-IZz3sboy1g8-unsplash Medium"
    else:
        plant = "🌼 Peace Lily"
        desc = "Loves bright, indirect light. Purifies air and looks elegant."
        image_url = "https://i.pinimg.com/564x/11/14/16/111416dc1c4d872f23f6f6b8b1117c6c.jpg"

    # Display result
    st.success(f"Your Perfect Plant: **{plant}**")
    st.image(image_url, caption=plant, use_column_width=True)
    st.info(desc)

    if st.button("🔁 Try Again"):
        st.experimental_rerun()
