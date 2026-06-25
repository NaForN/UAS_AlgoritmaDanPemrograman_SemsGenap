import streamlit as st
from utils.auth import register_user

st.set_page_config(page_title="Register")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #fff8e1, #fbe9e7);
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #6f4e37;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
        text-shadow: 2px 2px #d7ccc8;
    }

    h2, h3 {
        color: #4e342e;
        margin-top: 25px;
        font-weight: 600;
        border-left: 6px solid #6f4e37;
        padding-left: 10px;
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

st.title("Register Akun")

username = st.text_input("Username Baru")
password = st.text_input("Password Baru", type="password")

if st.button("Daftar"):
    register_user(username, password)
    st.success("Registrasi berhasil!")

st.page_link("app.py", label="Sudah punya akun? Login")
