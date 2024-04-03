import streamlit as st

st.set_page_config(
    page_title="My App"
)


st.sidebar.success("Select a page above")

import streamlit as st


# Use local CSS
def local_css(style1):
    with open(style1) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Animation
animation_symbol = "🌸"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)
def main():
    st.title("Welcome to My Streamlit App!")

    # Text input widget
    name = st.text_input("Enter your name", "")

    # Slider widget
    age = st.slider("Select your age", min_value=1, max_value=100, value=25)

    # Checkbox widget
    agree = st.checkbox("I agree to the terms and conditions")

    # Radio button widget
    gender = st.radio("Select your gender", options=["Male", "Female", "Other"])

    # Dropdown widget
    country = st.selectbox("Select your country", options=["India","China","America","other"])

    # Button widget
    if st.button("Submit"):
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Gender: {gender}")
        st.write(f"Country: {country}")
        if agree:
            st.write("You agreed to the terms and conditions.")
        else:
            st.write("You did not agree to the terms and conditions.")

if __name__ == "__main__":
    main()
