import random
import matplotlib.pyplot as plt

# Mengimpor fungsi-fungsi dari file lain
from inisiasipopulasi import inisialisasi_populasi
from EvaluasiFitness import hitung_fitness
from selection import roulette_wheel_selection
from crossover import one_point_crossover
from mutation import uniform_mutation

"""
=============================================================
Algoritma Genetika untuk Knapsack Problem
=============================================================
NIM      : H1D024026
Nama     : Muhammad Fathan Ramdani
Pertemuan: 10

Penentuan Metode berdasarkan NIM H1D024026:
- Dua angka terakhir NIM: 2 dan 6
- Seleksi   : Digit pertama (2) → RWS (Roulette Wheel Selection)
- Crossover : Digit kedua (6)   → One Point Crossover
- Mutasi    : 2 + 6 = 8, digit terakhir (8) → Uniform Mutation
=============================================================
"""

# Data barang: (nama, keuntungan, ukuran)
barang = [
    ("Barang1", 60, 10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90, 25),
    ("Barang5", 70, 15),
]

# Ukuran Maksimal gudang
KAPASITAS_GUDANG = 50


def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, kapasitas):
    """
    Menjalankan Algoritma Genetika untuk menyelesaikan Knapsack Problem.
    
    Parameter:
    - jumlah_generasi : jumlah iterasi evolusi
    - jumlah_populasi : jumlah individu dalam populasi
    - prob_crossover  : probabilitas crossover (0-1)
    - prob_mutasi     : probabilitas mutasi (0-1)
    - kapasitas       : ukuran maksimal gudang
    """
    # Menentukan jumlah gen berdasarkan jumlah barang
    jumlah_gen = len(barang)

    # Inisialisasi populasi awal
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)

    # Menampilkan populasi awal
    print("=" * 60)
    print("POPULASI AWAL")
    print("=" * 60)
    for idx, individu in enumerate(populasi):
        fitness = hitung_fitness(individu, barang, kapasitas)
        print(f"Individu {idx+1:2d}: {individu} | Fitness: {fitness}")

    # List untuk menyimpan nilai fitness terbaik, terburuk, dan rata-rata setiap generasi
    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []

    # Variabel untuk menyimpan individu terbaik secara keseluruhan
    best_individu = None
    best_fitness_overall = 0

    # Proses evolusi selama jumlah generasi yang ditentukan
    for generasi in range(jumlah_generasi):
        # Evaluasi fitness populasi saat ini
        fitness_populasi = [hitung_fitness(individu, barang, kapasitas) for individu in populasi]

        # Menyimpan nilai fitness untuk plotting
        best_fitness = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness = sum(fitness_populasi) / len(fitness_populasi)
        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())

        # Menyimpan individu terbaik secara keseluruhan
        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            index_best = fitness_populasi.index(best_fitness)
            best_individu = populasi[index_best][:]

        new_populasi = []
        used_indices = []

        # Membentuk populasi baru melalui seleksi, crossover, dan mutasi
        while len(new_populasi) < jumlah_populasi:
            # ==============================
            # SELEKSI: Roulette Wheel Selection (RWS)
            # ==============================
            parent1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)
            used_indices.append(idx1)

            # Memastikan orang tua kedua berbeda
            available_indices = [i for i in range(len(populasi)) if i not in used_indices]
            if not available_indices:
                used_indices = [idx1]
                available_indices = [i for i in range(len(populasi)) if i != idx1]

            parent2, idx2 = roulette_wheel_selection(
                [populasi[i] for i in available_indices],
                [fitness_populasi[i] for i in available_indices]
            )
            used_indices.append(available_indices[idx2])

            # ==============================
            # CROSSOVER: One-Point Crossover
            # ==============================
            if random.random() < prob_crossover:
                anak1, anak2 = one_point_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]

            # ==============================
            # MUTASI: Uniform Mutation
            # ==============================
            if random.random() < prob_mutasi:
                anak1 = uniform_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = uniform_mutation(anak2)

            # Menambahkan anak ke populasi baru
            new_populasi.extend([anak1, anak2])

        # Memastikan populasi baru sesuai dengan jumlah populasi
        populasi = new_populasi[:jumlah_populasi]

    # ==============================
    # MENAMPILKAN HASIL AKHIR
    # ==============================
    print("\n" + "=" * 60)
    print("HASIL ALGORITMA GENETIKA")
    print("=" * 60)

    # Menampilkan barang yang terpilih dalam knapsack terbaik
    selected_items = [barang[i] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_value = hitung_fitness(best_individu, barang, kapasitas)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])

    print(f"\nKromosom Terbaik  : {best_individu}")
    print(f"Nilai Fitness     : {selected_value}")
    print(f"Total Ukuran      : {selected_weight} / {kapasitas}")
    print(f"\nBarang yang Dipilih:")
    print("-" * 40)
    print(f"{'Nama':<12} {'Keuntungan':>12} {'Ukuran':>10}")
    print("-" * 40)
    for item in selected_items:
        print(f"{item[0]:<12} {item[1]:>12} {item[2]:>10}")
    print("-" * 40)
    print(f"{'TOTAL':<12} {selected_value:>12} {selected_weight:>10}")
    print("=" * 60)

    # ==============================
    # PLOTTING GRAFIK FITNESS
    # ==============================
    plt.figure(figsize=(12, 7))

    # Plot semua nilai fitness dengan transparansi rendah
    for i in range(jumlah_generasi):
        x = [i+1] * len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1, s=10)

    # Plot nilai fitness terbaik, terburuk, dan rata-rata
    generasi_range = range(1, jumlah_generasi + 1)
    plt.plot(generasi_range, best_fitness_list, color='blue', label='Fitness Tertinggi', linewidth=2)
    plt.plot(generasi_range, worst_fitness_list, color='orange', label='Fitness Terendah', linewidth=2)
    plt.plot(generasi_range, avg_fitness_list, color='red', label='Fitness Rata-rata', linewidth=2, linestyle='--')

    plt.title('Perkembangan Nilai Fitness per Generasi\n'
              '(Seleksi: RWS | Crossover: One-Point | Mutasi: Uniform)',
              fontsize=13, fontweight='bold')
    plt.xlabel('Generasi', fontsize=12)
    plt.ylabel('Nilai Fitness', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ==============================
# MENJALANKAN ALGORITMA GENETIKA
# ==============================
if __name__ == "__main__":
    print("=" * 60)
    print("ALGORITMA GENETIKA - KNAPSACK PROBLEM")
    print("NIM: H1D024026 - Muhammad Fathan Ramdani")
    print("=" * 60)
    print(f"\nMetode yang digunakan:")
    print(f"  Seleksi   : Roulette Wheel Selection (RWS)")
    print(f"  Crossover : One-Point Crossover")
    print(f"  Mutasi    : Uniform Mutation")
    print(f"\nData Barang:")
    print(f"{'Nama':<12} {'Keuntungan':>12} {'Ukuran':>10}")
    print("-" * 40)
    for b in barang:
        print(f"{b[0]:<12} {b[1]:>12} {b[2]:>10}")
    print(f"\nKapasitas Gudang: {KAPASITAS_GUDANG}")
    print()

    run_ga(
        jumlah_generasi=50,
        jumlah_populasi=20,
        prob_crossover=0.8,
        prob_mutasi=0.1,
        kapasitas=KAPASITAS_GUDANG
    )
