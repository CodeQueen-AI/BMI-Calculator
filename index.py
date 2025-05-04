import streamlit as st

# Page Configuration
st.set_page_config(page_title="💪 BMI Calculator", page_icon="📏", layout="centered")

# Custom CSS for rounded input boxes and a card-style look
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .main {
        background-color: #f5f7fa;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar info
st.sidebar.title("💡 How to Use")
st.sidebar.info("👉 Enter your height and weight to calculate your BMI.\n\n"
                "🎯 The result will show your health category.")

# App title
st.title("💪 BMI Calculator")
st.markdown("### _Calculate your Body Mass Index (BMI) and understand your health better!_ 🚀")

# Main container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Input fields
    height = st.number_input("📏 Enter your height (in meters):", min_value=0.1, format="%.2f")
    weight = st.number_input("⚖️ Enter your weight (in kilograms):", min_value=1.0, format="%.2f")

    # Button to calculate BMI
    if st.button("✨ Calculate BMI"):
        if height > 0 and weight > 0:
            bmi = weight / (height ** 2)
            st.markdown(f"### 📊 Your BMI: **{bmi:.2f}**")

            # Health feedback based on BMI
            if bmi < 18.5:
                st.warning("🔍 You're **underweight**. Try to include more nutrition in your diet! 🥦🍞")
            elif 18.5 <= bmi < 24.9:
                st.success("✅ You have a **normal weight**. Keep it up! 🏆💪")
                st.balloons()
            elif 25 <= bmi < 29.9:
                st.info("⚠️ You're **overweight**. Time to include some regular exercise! 🏃‍♂️💨")
            else:
                st.error("🚨 You're in the **obese** category. Consider consulting a health expert. ❤️‍🩹")
        else:
            st.error("❗ Please enter valid height and weight values.")
    
    st.markdown('</div>', unsafe_allow_html=True)
