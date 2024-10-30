import matplotlib.pyplot as plt

# Fungsi untuk menggambar garis menggunakan algoritma DDA
def dda(x1, y1, x2, y2):
    # Hitung perubahan pada sumbu x dan y
    dx = x2 - x1
    dy = y2 - y1
    
    # Tentukan jumlah langkah berdasarkan perubahan terbesar (di x atau y)
    steps = max(abs(dx), abs(dy))
    
    # Hitung kenaikan (increment) pada setiap langkah
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Simpan titik awal dalam daftar
    x_values = [x1]
    y_values = [y1]
    
    # Mulai dari titik awal
    x = x1
    y = y1
    
    # Ulangi proses untuk setiap langkah
    for _ in range(int(steps)):
        # Tambahkan increment untuk menghasilkan titik-titik baru
        x += x_increment
        y += y_increment
        # Simpan titik yang dihasilkan, dibulatkan agar sesuai dengan grid
        x_values.append(round(x))
        y_values.append(round(y))
    
    # Kembalikan daftar titik-titik x dan y
    return x_values, y_values

# Titik awal dan titik akhir garis
x1, y1 = 10, 5
x2, y2 = 20, 15

# Dapatkan titik-titik garis menggunakan algoritma DDA
x_vals, y_vals = dda(x1, y1, x2, y2)

# Gambar garis menggunakan matplotlib
plt.plot(x_vals, y_vals, marker='o')
plt.title(f"Garis antara ({x1}, {y1}) dan ({x2}, {y2}) menggunakan DDA")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()