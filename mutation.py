import random

# Uniform Mutation
# Digunakan berdasarkan NIM H1D024026 (2+6=8, digit terakhir=8 → Uniform)
def uniform_mutation(kromosom, mutation_rate=0.1):
    """
    Mutasi menggunakan metode Uniform Mutation.
    Setiap gen pada kromosom memiliki peluang sebesar mutation_rate
    untuk di-flip (0 → 1 atau 1 → 0).
    """
    kromosom = list(kromosom)  # Konversi ke list jika perlu
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]  # Membalik nilai gen (flip bit)
    return kromosom

# Contoh penggunaan
if __name__ == "__main__":
    # Definisikan anak sebelum digunakan
    anak1 = [0, 1, 1, 0, 1]

    # Contoh penggunaan Uniform Mutation
    mutasi_anak1 = uniform_mutation(anak1.copy(), mutation_rate=0.3)

    # Menampilkan hasil setelah mutasi
    print("\nAnak Setelah Uniform Mutation:")
    print(f"Sebelum Mutasi : {anak1}")
    print(f"Setelah Mutasi : {mutasi_anak1}")
