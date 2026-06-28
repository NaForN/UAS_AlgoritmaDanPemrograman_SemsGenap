import streamlit as st
from utils.menu import load_menu, tambah_menu, hapus_menu, ubah_menu
from utils.transaksi import catat_transaksi

st.set_page_config(page_title="Kelola Menu & Pembelian")

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

    .stButton>button {
        background-color: #6f4e37;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #8d6e63;
        transform: scale(1.05);
    }

    .stTextInput>div>input, .stNumberInput>div>input {
        border: 2px solid #6f4e37;
        border-radius: 6px;
        padding: 6px;
        background-color: #fff;
    }

    .stTable {
        border: 2px solid #6f4e37;
        border-radius: 10px;
        overflow: hidden;
        background-color: #fff;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
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

st.title("Kelola Menu & Pembelian")

st.divider()
st.subheader("Pengelolaan Menu")

menu = load_menu()
st.table(menu)

nama = st.text_input("Nama Menu")
harga = st.number_input("Harga", min_value=0)
stok = st.number_input("Stok", min_value=0)

if st.button("Tambah Menu"):
    tambah_menu(nama, harga, stok)
    st.success("Menu berhasil ditambahkan!")

if menu:
    nama_hapus = st.selectbox("Pilih Menu untuk Dihapus", [m[0] for m in menu])
    if st.button("Hapus Menu"):
        hapus_menu(nama_hapus)
        st.success("Menu berhasil dihapus!")

if menu:
    nama_ubah = st.selectbox("Pilih Menu untuk Diubah", [m[0] for m in menu])
    nama_baru = st.text_input("Nama Baru (kosongkan jika tidak ingin ganti)")
    harga_baru = st.number_input("Harga Baru", min_value=0)
    stok_baru = st.number_input("Stok Baru", min_value=0)
    if st.button("Update Menu"):
        final_nama = nama_baru.strip() if nama_baru.strip() else nama_ubah
        berhasil = ubah_menu(nama_ubah, final_nama, harga_baru, stok_baru)
        if berhasil:
            st.success("Menu berhasil diubah!")
        else:
            st.error("Nama menu tidak ditemukan!")

st.divider()
st.subheader("Pembelian Produk")

if menu:
    pilihan = st.selectbox("Pilih Produk", [m[0] for m in menu if int(m[2]) > 0])
    jumlah = st.number_input("Jumlah", min_value=1)
    harga_produk = next((int(m[1]) for m in menu if m[0] == pilihan), 0)
    stok_produk = next((int(m[2]) for m in menu if m[0] == pilihan), 0)
    total = harga_produk * jumlah

    if jumlah >= 3:
        total = int(total * 0.9)
        st.info("Diskon 10% diterapkan!")

    st.write(f"Total: Rp {total}")

    if st.button("Catat Pembelian"):
        if jumlah > stok_produk:
            st.error("Stok tidak mencukupi!")
        else:
            catat_transaksi(pilihan, jumlah, total)
            st.success("Pembelian berhasil dicatat!")
else:
    st.info("Belum ada produk.")

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
