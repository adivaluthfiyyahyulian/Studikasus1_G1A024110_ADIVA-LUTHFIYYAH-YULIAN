# Studi Kasus Materi 1: Make Sense of Data with Analysis and AI

## Judul
**Analisis Data Penjualan untuk Mendukung Pengambilan Keputusan Menggunakan Python**

## Latar Belakang
Data transaksi dapat membantu toko memahami kondisi penjualan. Namun, data perlu diperiksa dan dibersihkan sebelum dianalisis. Proyek ini mengubah data transaksi menjadi informasi, insight, dan rekomendasi awal untuk mendukung keputusan bisnis.

## Tujuan
1. Mempraktikkan tahapan pengolahan data sebelum analisis.
2. Menerapkan descriptive analytics untuk melihat omzet, produk, dan tren bulanan.
3. Menunjukkan alur Data → Information → Insight → Decision.
4. Menghasilkan ringkasan yang dapat digunakan sebagai dasar diskusi pengambilan keputusan.

## Keterkaitan dengan Materi Pemateri
- **CRISP-DM:** Business Understanding, Data Understanding, Data Preparation, Modeling/Analysis, Evaluation, dan Deployment dapat digunakan sebagai kerangka kerja proyek.
- **Data quality / Garbage In, Garbage Out:** program memeriksa nilai kosong, duplikasi, tanggal tidak valid, jumlah yang tidak valid, dan harga yang kosong sebelum analisis.
- **Descriptive Analytics:** program merangkum omzet dan penjualan per produk serta per bulan.
- **Insight dan Decision:** hasil analisis diikuti rekomendasi awal, tetapi keputusan tetap perlu ditinjau manusia.
- **Human-in-the-Loop:** rekomendasi program bukan keputusan otomatis dan perlu diperiksa berdasarkan konteks bisnis.

> Catatan: Proyek ini menerapkan beberapa tahapan dan konsep dari materi. Bagian modeling CRISP-DM tidak menggunakan model prediktif; analisis utama bersifat deskriptif.

## Dataset
File `data_penjualan.csv` merupakan **data contoh/sintetis untuk latihan**, bukan data transaksi toko sungguhan. File sengaja berisi beberapa masalah kualitas data seperti baris duplikat, nilai kosong, tanggal tidak valid, dan jumlah negatif agar proses data preparation dapat diperlihatkan.

Kolom:
- `tanggal`: tanggal transaksi
- `produk`: nama produk
- `jumlah`: unit terjual
- `harga_satuan`: harga satuan dalam rupiah

## Analitik yang Digunakan
Analisis ini termasuk **Descriptive Analytics**, yaitu menjelaskan apa yang terjadi berdasarkan data yang tersedia. Program menghitung omzet, total unit, ringkasan omzet per produk, dan omzet bulanan. Rekomendasi yang ditampilkan merupakan interpretasi awal, bukan pembuktian sebab-akibat.

## Struktur Proyek
```text
studi-kasus-analisis-penjualan/
├── main.py
├── data_penjualan.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Cara Menjalankan
Pastikan Python telah terpasang. Buka terminal pada folder proyek lalu jalankan:

```bash
pip install -r requirements.txt
python main.py
```

Jika perintah `python` tidak dikenali pada Windows, coba:

```bash
py main.py
```

## Output
Program menampilkan:
- Pemeriksaan data awal
- Jumlah baris sebelum dan sesudah dibersihkan
- Total omzet dan unit terjual
- Ringkasan penjualan per produk
- Ringkasan omzet per bulan
- Insight dan rekomendasi awal

Program juga membuat folder `hasil` berisi data bersih dan ringkasan hasil analisis.
