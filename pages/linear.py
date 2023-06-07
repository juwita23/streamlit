import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Persamaan Linear dan Grafik Garis dengan Streamlit')

# Input koefisien m dan b
m = st.number_input('Masukkan koefisien m (gradien)', value=1.0)
b = st.number_input('Masukkan koefisien b (intersep)', value=0.0)

# Generate data untuk garis
x = np.linspace(-10, 10, 100)
y = m * x + b

# Menampilkan grafik garis
fig, ax = plt.subplots()
ax.plot(x, y, label='Garis')
ax.set_xlabel('Nilai x')
ax.set_ylabel('Nilai y')
ax.set_title('Grafik Garis')
ax.legend()
st.pyplot(fig)

# Menampilkan persamaan linear
st.write(f'PERSAMAAN LINEAR: y = {m}x + {b}')
