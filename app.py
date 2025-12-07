#import Library streamlit
import streamlit as st
#mengolah simbol matematika (User)
import sympy as sp
#hitng numerik
import numpy as np
#tabel iterasi
import pandas as pd
#grafik fungsi
import matplotlib.pyplot as plt

#Judul tab web
st.set_page_config(
  page_title="SPNL - Metode Regula Falsi",
  layout="centered"
)

st.title("Aplikasi ini digunakan untuk mencari akar persamaan non-linear tunggal menggunakan metode Regula Falsi "
)

st.sidebar.header("Input Parameter")

input_fungsi = st.sidebar.text_input(
    "Masukkan f(x)",
    value="x**3 - x - 2",
    help="Contoh: x**3 - x - 2"
)

a = st.sidebar.number_input("Batas bawah (a)", value=1.0)
b = st.sidebar.number_input("Batas atas (b)", value=2.0)
toleransi = st.sidebar.number_input("Toleransi |f(c)|", value=1e-6, format="%.10f")
max_iterasi = st.sidebar.number_input("Maksimum iterasi", value=50, min_value=1, step=1)

#fungsi untuk mengubah f(x)
def buat_fungsi(teks_fungsi):
  x = sp.symbols("x")
  try:
    ekspresi = sp.sympify(teks_fungsi)
    fungsi_numerik = sp.lambdify(x, ekspresi,"numpy")
    return ekspresi, fungsi_numerik
  except:
    raise ValueError("fungsi tidak valid, periksa kembali penulisan f(x)")

def metode_regula_falsi(f, a, b, toleransi, max_iterasi):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("f(a) dan f(b) harus memiliki tanda yang berbeda")

    data = []

    for i in range(1, max_iterasi + 1):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        data.append({
            "Iterasi": i,
            "a": a,
            "b": b,
            "c": c,
            "f(a)": fa,
            "f(b)": fb,
            "f(c)": fc
        })

        if abs(fc) < toleransi:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return pd.DataFrame(data)

# Tombol eksekusi
if st.button("Hitung Regula Falsi"):
    try:
        ekspresi, fungsi = buat_fungsi(input_fungsi)
        hasil = metode_regula_falsi(
            fungsi, a, b, toleransi, int(max_iterasi)
        )

        akar = hasil.iloc[-1]["c"]

        st.success(f"Akar hampiran: x ≈ {akar:.8f}")

        st.subheader("Tabel Iterasi")
        st.dataframe(hasil)

        # =========================
        # Grafik fungsi
        # =========================
        x_vals = np.linspace(a - 1, b + 1, 500)
        y_vals = fungsi(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label="f(x)")
        ax.axhline(0)
        ax.scatter(hasil["c"], hasil["f(c)"], color="red", label="Nilai c")
        ax.legend()
        ax.grid()

        st.pyplot(fig)

        st.info("Aplikasi ini dibuat untuk tugas SPNL menggunakan metode Regula Falsi")

    except Exception as e:
        st.error(str(e))
  
          
          
