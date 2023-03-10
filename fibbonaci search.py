def fibonacci_search(arr, x):
    # Inisialisasi bilangan Fibonacci
    fib2 = 0  # Fib(n-2)
    fib1 = 1  # Fib(n-1)
    fib = fib1 + fib2  # Fib(n)

    # Cari bilangan Fibonacci terbesar yang <= len(arr)
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    # Indeks awal, tengah, dan akhir array
    i = 0
    mid = 0
    n = len(arr)

    # Lakukan pencarian biner
    while fib > 1:
        # Hitung indeks dari mid dan cek apakah valid
        mid = min(i+fib2, n-1)

        # Jika x lebih besar dari elemen mid, cari di sebelah kanan
        if isinstance(arr[mid], list):
            if arr[mid][0] < x:
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                i = mid
            elif arr[mid][0] > x:
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
            else:
                return mid, 0
        else:
            if arr[mid] < x:
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                i = mid
            elif arr[mid] > x:
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
            else:
                return mid, 0

    # Jika x tidak ditemukan pada kolom 0, cek pada kolom 1
    if isinstance(arr[i], list):
        if arr[i][1] == x:
            return i, 1
        else:
            return -1, -1
    else:
        if arr[i] == x:
            return i, 0
        else:
            return -1, -1


var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
x = input("Masukkan nama: ")
index, col = fibonacci_search(var, x)

if col == 0:
    if index != -1:
        print(f"Elemen {x} ditemukan pada indeks ke-{index}")
    else:
        print(f"Elemen {x} tidak ditemukan")
elif col == 1:
    if index != -1:
        print(f"Elemen {x} ditemukan pada indeks ke-{index} pada kolom {col}")
    else:
        print(f"Elemen {x} tidak ditemukan pada kolom 1")
else:
    print(f"Elemen {x} tidak ditemukan")