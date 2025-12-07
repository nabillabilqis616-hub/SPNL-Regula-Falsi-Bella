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
  page_title="SPNL - Metode Regula Falsi".
  layout="centeredd"
)

st.tittle("Aplikasi ini digunakan untuk mencari akar persamaan non-linear tunggal menggunakan metode Regula Falsi, "
          "Masukkan fungsi f(x) (contoh: `x**3 - x - 2`) dan interval [a, b]"
          
