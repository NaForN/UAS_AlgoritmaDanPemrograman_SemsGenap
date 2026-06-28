import streamlit as st
from utils.transaksi import load_transaksi
from utils.laporan import laporan_harian

st.set_page_config(page_title="Riwayat")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #1565c0;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
        text-shadow: 2px 2px #90caf9;
    }

    h2, h3 {
        color: #0d47a1;
        margin-top: 25px;
        font-weight: 600;
        border-left: 6px solid #1565c0;
        padding-left: 10px;
    }

    .stTable {
        border: 2px solid #1565c0;
        border-radius: 10px;
        overflow: hidden;
        background-color: #fff;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }

    .stButton>button {
        background-color: #1565c0;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1e88e5;
        transform: scale(1.05);
    }

    hr {
        border: none;
        border-top: 3px dashed #1565c0;
        margin: 25px 0;
    }
    </style>
""", unsafe_allow_html=True)

if not st.session_state.get("is_login", False):
    st.switch_page("app.py")

st.title("Riwayat Transaksi & Laporan Harian")
st.write(f"Selamat datang, {st.session_state['username']}")

st.divider()
st.subheader("Riwayat Transaksi")
transaksi = load_transaksi()
if transaksi:
    st.table(transaksi)
else:
    st.info("Belum ada transaksi.")

st.divider()
st.subheader("Laporan Penjualan Harian")
laporan, total_harian = laporan_harian()
if laporan:
    st.table(laporan)
    st.write(f"Total Pendapatan Hari Ini: Rp {total_harian}")
else:
    st.info("Belum ada transaksi hari ini.")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
