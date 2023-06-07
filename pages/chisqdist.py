import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Distribusi Chi-Square dan Uji Hipotesis dengan Streamlit')

# Input nilai derajat kebebasan (degrees of freedom)
df = st.number_input('Masukkan nilai derajat kebebasan (degrees of freedom)', value=10, step=1)

# Input nilai pengamatan
observed_value = st.number_input('Masukkan nilai pengamatan', value=10, step=1)

# Menghasilkan sampel dari distribusi chi-square
np.random.seed(0)
sample = np.random.chisquare(df, size=1000)

# Menampilkan histogram dari sampel
fig, ax = plt.subplots()
ax.hist(sample, bins=30, density=True, alpha=0.5)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title('Histogram Distribusi Chi-Square')
st.pyplot(fig)

# Menghitung p-value
p_value = 1 - stats.chi2.cdf(observed_value, df)

# Menampilkan hasil uji hipotesis
st.write('Hasil Uji Hipotesis:')
st.write(f'Nilai pengamatan: {observed_value}')
st.write(f'Nilai p-value: {p_value:.4f}')

# Menentukan apakah H0 ditolak atau diterima
alpha = 0.05
if p_value < alpha:
    st.write('Hipotesis nol (H0) ditolak')
else:
    st.write('Hipotesis nol (H0) diterima')
