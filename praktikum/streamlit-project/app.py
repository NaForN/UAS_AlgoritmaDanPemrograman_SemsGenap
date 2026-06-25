import streamlit as st
from utils.auth import login_user

st.set_page_config(page_title="Login Kafe")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #fdf6f0, #fbe9e7);
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #6f4e37;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
        text-shadow: 2px 2px #d7ccc8;
    }

    h2 {
        color: #4e342e;
        text-align: center;
        margin-bottom: 25px;
    }

    .stTextInput>div>input {
        border: 2px solid #6f4e37;
        border-radius: 6px;
        padding: 8px;
        background-color: #fff;
    }

    .stButton>button {
        background-color: #6f4e37;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #8d6e63;
        transform: scale(1.05);
    }

    a {
        color: #6f4e37;
        font-weight: bold;
        text-decoration: none;
    }
    a:hover {
        color: #8d6e63;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Kafe 4U")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/logo.png")

st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if login_user(username, password):
        st.session_state["is_login"] = True
        st.session_state["username"] = username
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Username atau Password salah")

st.page_link("pages/register.py", label="Belum punya akun? Register")
