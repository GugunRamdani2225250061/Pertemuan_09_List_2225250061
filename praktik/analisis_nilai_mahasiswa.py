
# Praktik: Analisis Nilai Mahasiswa
# Mata Kuliah: Algoritma dan Pemrograman
# Materi: List dan Pengolahan Data Numerik

# Fungsi untuk menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi untuk mengambil nilai yang lulus
def nilai_lulus(data, batas=60):
    hasil = []

    for x in data:
        if x >= batas:
            hasil.append(x)

    return hasil


# Data nilai mahasiswa (10 data)
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
banyak_data = len(nilai)
total = sum(nilai)
minimum = min(nilai) if nilai else 0
maksimum = max(nilai) if nilai else 0

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# Menampilkan hasil analisis
print("=" * 45)
print("       ANALISIS NILAI MAHASISWA")
print("=" * 45)

print(f"Data nilai       : {nilai}")
print(f"Banyak data      : {banyak_data}")
print(f"Total nilai      : {total}")
print(f"Rata-rata        : {rata_rata(nilai):.2f}")
print(f"Nilai minimum    : {minimum}")
print(f"Nilai maksimum   : {maksimum}")
print(f"Nilai lulus      : {lulus}")
print(f"Jumlah lulus     : {jumlah_lulus}")
print(f"Belum lulus      : {jumlah_belum_lulus}")

print("=" * 45)