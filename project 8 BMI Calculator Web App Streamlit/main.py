import streamlit as st

# Page config
st.set_page_config(page_title="BMI Calculator 💪", page_icon="🏋️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 3rem;
            text-align: center;
            color: #ff4b4b;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.2rem;
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }
        .bmi-box {
            background-color: #f0f2f6;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">BMI Calculator 💪</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Calculate your Body Mass Index using weight and height</div>', unsafe_allow_html=True)

# Input box
with st.container():
    st.markdown('<div class="bmi-box">', unsafe_allow_html=True)

    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height (in feet)", min_value=0.1, step=0.1)

    def calculate_bmi(weight, height_ft):
        height_m = height_ft * 0.3048
        bmi = weight / (height_m ** 2)
        return bmi

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                st.info("Category: Underweight")
            elif 18.5 <= bmi < 24.9:
                st.success("Category: Normal weight")
            elif 25 <= bmi < 29.9:
                st.warning("Category: Overweight")
            else:
                st.error("Category: Obese")
        else:
            st.error("Please enter valid weight and height.")

    st.markdown('</div>', unsafe_allow_html=True)
