import random

# Fungsi untuk Roulette Wheel Selection (RWS)
# Digunakan berdasarkan NIM H1D024026 (digit pertama dari 2 angka terakhir = 2 → RWS)
def roulette_wheel_selection(populasi, fitness_populasi):
    """
    Seleksi menggunakan metode Roulette Wheel Selection (RWS).
    Setiap individu memiliki peluang terpilih sebanding dengan nilai fitness-nya.
    Individu dengan fitness lebih tinggi memiliki peluang lebih besar.
    """
    total_fitness = sum(fitness_populasi)
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx  # Mengembalikan individu dan indeksnya

    # Menghitung probabilitas seleksi
    probabilitas = [fitness / total_fitness for fitness in fitness_populasi]
    
    # Menghitung probabilitas kumulatif
    kumulatif_prob = []
    kumulatif = 0
    for p in probabilitas:
        kumulatif += p
        kumulatif_prob.append(kumulatif)

    # Memutar roda roulette
    r = random.random()
    for i, kum_prob in enumerate(kumulatif_prob):
        if r <= kum_prob:
            return populasi[i], i  # Mengembalikan individu dan indeksnya
    return populasi[-1], len(populasi)-1

# Contoh penggunaan
if __name__ == "__main__":
    # Definisikan populasi awal dan fitness_populasi
    populasi_awal = ['individu1', 'individu2', 'individu3', 'individu4']
    fitness_populasi = [10, 20, 30, 40]

    # Membuat salinan populasi dan fitness untuk dimodifikasi
    available_populasi = populasi_awal.copy()
    available_fitness = fitness_populasi.copy()

    # Memilih Parent 1 menggunakan Roulette Wheel Selection
    parent1, idx1 = roulette_wheel_selection(available_populasi, available_fitness)

    # Menghapus parent1 dari daftar
    del available_populasi[idx1]
    del available_fitness[idx1]

    # Memilih Parent 2 menggunakan Roulette Wheel Selection
    parent2, idx2 = roulette_wheel_selection(available_populasi, available_fitness)

    print("\nParent Terpilih (RWS):")
    print(f"Parent 1: {parent1}")
    print(f"Parent 2: {parent2}")
