# Praktikum Kecerdasan Buatan - Pertemuan 10
## Algoritma Genetika 2 - Knapsack Problem

### Identitas
| | |
|---|---|
| **Nama** | Muhammad Fathan Ramdani |
| **NIM** | H1D024026 |
| **Mata Kuliah** | Praktikum Kecerdasan Buatan (A) |
| **Pertemuan** | 10 |

---

### Deskripsi
Program ini mengimplementasikan **Algoritma Genetika** untuk menyelesaikan **Knapsack Problem**. Sebuah toko memiliki gudang dengan ukuran maksimal tertentu, dan tujuannya adalah memilih barang-barang yang memberikan keuntungan maksimal tanpa melebihi kapasitas gudang.

### Penentuan Metode Berdasarkan NIM
NIM: **H1D024026** → Dua angka terakhir: **2** dan **6**

| Langkah | Digit | Metode |
|---------|-------|--------|
| **Seleksi** | Digit pertama = 2 | **Roulette Wheel Selection (RWS)** |
| **Crossover** | Digit kedua = 6 | **One-Point Crossover** |
| **Mutasi** | 2 + 6 = 8 (digit terakhir = 8) | **Uniform Mutation** |

### Data Barang

| Barang | Keuntungan | Ukuran |
|--------|-----------|--------|
| Barang1 | 60 | 10 |
| Barang2 | 100 | 20 |
| Barang3 | 120 | 30 |
| Barang4 | 90 | 25 |
| Barang5 | 70 | 15 |

**Kapasitas Gudang**: 50

### Struktur File
```
Pertemuan10/
├── main.py               # Program utama Algoritma Genetika
├── inisiasipopulasi.py   # Fungsi inisialisasi populasi
├── EvaluasiFitness.py    # Fungsi evaluasi fitness
├── selection.py          # Fungsi seleksi (RWS)
├── crossover.py          # Fungsi crossover (One-Point)
├── mutation.py           # Fungsi mutasi (Uniform)
└── README.md             # Dokumentasi
```

### Cara Menjalankan
1. Pastikan Python sudah terinstal
2. Install library yang diperlukan:
   ```bash
   pip install matplotlib
   ```
3. Jalankan program utama:
   ```bash
   python main.py
   ```

### Parameter Algoritma Genetika
| Parameter | Nilai |
|-----------|-------|
| Jumlah Generasi | 50 |
| Jumlah Populasi | 20 |
| Probabilitas Crossover | 0.8 |
| Probabilitas Mutasi | 0.1 |

### Output
Program akan menampilkan:
1. Populasi awal beserta nilai fitness
2. Hasil akhir berupa barang yang terpilih dengan keuntungan maksimal
3. Grafik perkembangan fitness per generasi (fitness tertinggi, terendah, dan rata-rata)
