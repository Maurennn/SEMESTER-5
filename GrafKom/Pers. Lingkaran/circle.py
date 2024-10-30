import matplotlib.pyplot as plt
import numpy as np

# Masukkan nilai a, b, dan r
a = 20  # Titik tengah x
b = 6   # Titik tengah y
r = 6   # Jari-jari lingkaran

# Menghitung titik-titik pada lingkaran
theta = np.linspace(0, 2 * np.pi, 100) # Menghitung theta
x = a + r * np.cos(theta) # Menghitung nilai x
y = b + r * np.sin(theta) # Menghitung nilai y

# Membuat plot
plt.figure(figsize=(6, 6))  # Ukuran gambar
plt.plot(x, y)  # Gambar lingkaran dengan label
plt.scatter(a, b, color='red', label=f'Titik Pusat ({a}, {b})')  # Titik pusat

# Menambahkan keterangan jari-jari
plt.plot([a, a + r], [b, b], 'k--')  # Garis jari-jari
plt.text(a + r/2, b, f'Jari-jari = {r}', color='black', ha='center', va='bottom')  # Keterangan jari-jari

# Pengaturan plot
plt.title('Gambar Persamaan Lingkaran')  # Judul grafik
plt.xlabel('Sumbu X')  # Label sumbu X
plt.ylabel('Sumbu Y')  # Label sumbu Y
plt.grid(True)  # Tampilkan grid
plt.axis('equal')  # Pastikan lingkaran tidak terlihat oval
plt.legend()  # Tampilkan legenda
plt.show()  # Tampilkan gambar