# Kalkulator Gesture Tangan

Program kalkulator yang menggunakan gesture tangan untuk melakukan operasi matematika dasar. Program ini menggunakan MediaPipe untuk mendeteksi tangan dan OpenCV untuk menampilkan hasil.

## Fitur

- Deteksi gesture tangan menggunakan MediaPipe
- Operasi matematika dasar (tambah, kurang, kali, bagi)
- Tampilan real-time dengan OpenCV
- Visualisasi landmark tangan

## Persyaratan

- Python 3.x
- OpenCV (cv2)
- MediaPipe

## Instalasi

1. Clone repository ini
2. Install dependencies yang diperlukan:
```bash
pip install opencv-python mediapipe
```

## Cara Penggunaan

1. Jalankan program:
```bash
python calc.py
```

2. Gunakan gesture tangan untuk:
   - Menampilkan angka (0-5) dengan mengangkat jari
   - Operator matematika:
     - Angka 5 = operator tambah (+)
     - Angka 10 = operator kurang (-)
     - Angka 15 = operator kali (*)
     - Angka 20 = operator bagi (/)

3. Tekan 'q' untuk keluar dari program

## Cara Kerja

Program menggunakan MediaPipe untuk mendeteksi landmark tangan dan mengkonversi posisi jari menjadi angka. Setelah mendeteksi operator dan dua angka, program akan melakukan operasi matematika yang sesuai dan menampilkan hasilnya.
