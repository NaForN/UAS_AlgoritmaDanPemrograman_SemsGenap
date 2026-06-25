import streamlit as st
import pandas as pd
from utils.menu import load_menu
from utils.transaksi import load_transaksi

st.set_page_config(page_title="Dashboard Kafe")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #fdf6f0, #f5e1da);
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #4e342e;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
        text-shadow: 2px 2px #d7ccc8;
    }

    h2, h3 {
        color: #6f4e37;
        margin-top: 25px;
        font-weight: 600;
        border-left: 6px solid #6f4e37;
        padding-left: 10px;
    }

    .stImage>img {
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stImage>img:hover {
        transform: scale(1.08);
        box-shadow: 0 10px 18px rgba(0,0,0,0.35);
    }

    .stTable {
        border: 2px solid #6f4e37;
        border-radius: 10px;
        overflow: hidden;
        background-color: #fff;
    }

    [data-testid="stMetric"] {
        background: #fff3e0;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        text-align: center;
        font-weight: bold;
    }

    hr {
        border: none;
        border-top: 3px dashed #6f4e37;
        margin: 25px 0;
    }
    </style>
""", unsafe_allow_html=True)

if not st.session_state.get("is_login", False):
    st.switch_page("app.py")

st.title("Dashboard Kafe")
st.write(f"Selamat datang, {st.session_state['username']}")

st.divider()
st.subheader("Produk Kami")

menu = load_menu()
if menu:
    cols = st.columns(4)
    file_map = {
        "affogato": "Affogato.jpg",
        "americano": "Americano.webp",
        "cappuccino": "Cappuccino.webp",
        "cheesecake": "CheeseCake.webp",
        "espresso": "Espresso.webp",
        "latte": "Latte.jpg",
        "macchiato": "Macchiato.webp",
        "rollcake": "Rollcake.webp"
    }
    for i, m in enumerate(menu):
        nama_produk = m[0].lower()
        file_name = file_map.get(nama_produk, None)
        with cols[i % 4]:
            if file_name:
                st.image(f"images/{file_name}", caption=m[0])
            else:
                st.write(m[0])
else:
    st.info("Belum ada produk.")

st.divider()
st.subheader("Daftar Menu")
if menu:
    st.table(menu)
else:
    st.info("Belum ada menu.")

st.divider()
st.subheader("Statistik")

transaksi = load_transaksi()
if transaksi:
    df = pd.DataFrame(transaksi, columns=["Waktu","Menu","Jumlah","Total"])
    df["Jumlah"] = df["Jumlah"].astype(int)
    df["Total"] = df["Total"].astype(int)

    total_transaksi = len(df)
    total_item = df["Jumlah"].sum()
    total_pendapatan = df["Total"].sum()
    rata_transaksi = df["Total"].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Transaksi", total_transaksi)
    col2.metric("Total Item Terjual", total_item)
    col3.metric("Total Pendapatan", f"Rp {total_pendapatan}")
    col4.metric("Rata-rata per Transaksi", f"Rp {int(rata_transaksi)}")

    st.line_chart(df.groupby("Waktu")["Total"].sum())
    st.bar_chart(df.groupby("Menu")["Jumlah"].sum())
else:
    st.info("Belum ada transaksi.")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
