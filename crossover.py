import random

# One-Point Crossover
# Digunakan berdasarkan NIM H1D024026 (digit kedua dari 2 angka terakhir = 6 → One Point)
def one_point_crossover(parent1, parent2):
    """
    Crossover menggunakan metode One-Point Crossover.
    Memilih satu titik potong secara acak, kemudian menukar bagian
    kromosom setelah titik potong antara dua parent.
    """
    titik_potong = random.randint(1, len(parent1)-1)
    anak1 = parent1[:titik_potong] + parent2[titik_potong:]
    anak2 = parent2[:titik_potong] + parent1[titik_potong:]
    return anak1, anak2

# Contoh penggunaan
if __name__ == "__main__":
    parent1 = [1, 0, 1, 1, 0]
    parent2 = [0, 1, 0, 0, 1]

    anak1, anak2 = one_point_crossover(parent1, parent2)
    print("\nHasil One-Point Crossover:")
    print(f"Parent 1: {parent1}")
    print(f"Parent 2: {parent2}")
    print(f"Anak 1  : {anak1}")
    print(f"Anak 2  : {anak2}")
