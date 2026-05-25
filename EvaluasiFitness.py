# Data barang (nama, keuntungan, ukuran)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 70, 15),
]

kapasitas_gudang = 50  # Ukuran Maksimal gudang

# Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, kapasitas):
    """
    Menghitung fitness dari sebuah kromosom (individu).
    Fitness = total keuntungan jika total ukuran <= kapasitas gudang.
    Jika melebihi kapasitas, fitness = 0 (penalti).
    """
    total_keuntungan = 0
    total_ukuran = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_keuntungan += barang[i][1]
            total_ukuran += barang[i][2]
    if total_ukuran > kapasitas:
        return 0  # Penalti jika melebihi kapasitas gudang
    else:
        return total_keuntungan

# Contoh penggunaan
if __name__ == "__main__":
    # Definisi contoh populasi awal
    populasi_awal = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
    ]

    # Menghitung fitness untuk setiap individu
    fitness_populasi = [hitung_fitness(individu, barang, kapasitas_gudang) for individu in populasi_awal]

    # Menampilkan nilai fitness
    print("\nNilai Fitness:")
    for idx, fitness in enumerate(fitness_populasi):
        print(f"Individu {idx+1}: Fitness = {fitness}")
