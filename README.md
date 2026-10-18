
# Pertemuan 09 - List dan Pengolahan Data Numerik

- Nama: Gugun Ramdani  
- NIM: 2225250061  
- Kelas: 3A
- Mata Kuliah: Algoritma dan Pemrograman (Pertemuan 09)

## Tujuan
Mengolah kumpulan data numerik menggunakan list Python,
melakukan manipulasi elemen, menghitung statistik sederhana,
dan mengelompokkan nilai mahasiswa berdasarkan batas kelulusan.

## Struktur Program

### Folder latihan
- `01_buat_list.py`: Membuat list dan menghitung jumlah data.
- `02_indeks_slicing.py`: Mengakses elemen dengan indeks dan slicing.
- `03_manipulasi_list.py`: Mengubah, menambah, menyisipkan, dan menghapus elemen.
- `04_agregasi_nilai.py`: Menghitung total, rata-rata, minimum, dan maksimum.
- `05_filter_kelulusan.py`: Menyeleksi nilai yang memenuhi batas kelulusan.
- `06_fungsi_statistik.py`: Menghitung rata-rata menggunakan fungsi.

### Folder praktik
- `analisis_nilai_mahasiswa.py`: Menganalisis statistik dan kelulusan mahasiswa.

## Cara Menjalankan

Pastikan Python 3 telah terpasang.
Jalankan latihan melalui terminal VS Code, misalnya:
```bash
python latihan/01_buat_list.py
```
Jalankan program utama:
```bash
python praktik/analisis_nilai_mahasiswa.py
```
Jika perintah `python` tidak tersedia, coba gunakan `python3`.

## Test Case
| Pengujian | Hasil yang Diharapkan |
|---|---|
| List berisi lima nilai | Banyak data = 5 |
| Rata-rata [60, 70, 80] | 70.00 |
| Minimum dan maksimum | 60 dan 80 |
| Nilai [59, 60, 61] | 2 nilai lulus |
| Rata-rata list kosong | 0, tanpa error |

## Refleksi
Saya memahami bahwa list dapat digunakan untuk menyimpan
banyak nilai dalam satu variabel. Indeks Python dimulai dari
0, sedangkan indeks negatif dapat digunakan untuk mengakses
elemen dari belakang.

Kesalahan yang perlu diperhatikan adalah mengakses indeks
di luar rentang, menggunakan batas slicing secara keliru,
dan membagi dengan nol ketika list kosong. Kesalahan tersebut
dapat dihindari dengan memeriksa indeks dan jumlah data.
