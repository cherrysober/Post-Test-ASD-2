def jumpSearch(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    for c in range(len(arr)):
        if type(arr[c]) == list:
            a = jumpSearch(arr[c], x)
            if a != -1:
                print(f"{x} ditemukan pada indeks {c} kolom {a}")
                return a
        elif arr[c] == x:
            print(f"{x} ditemukan pada indeks {c}")
            return c
    return -1


var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
x = input("Masukkan nama: ")
index = jumpSearch(var, x)

if x == "Arsel":
    if index != -1:
        print(f"Elemen {x} ditemukan pada indeks ke-{index}")
    else:
        print(f"Elemen {x} tidak ditemukan")
elif x == "Avivah":
    if index != -1:
        print(f"Elemen {x} ditemukan pada indeks ke-{index}")
    else:
        print(f"Elemen {x} tidak ditemukan")
elif x == "Daiva":
    if index != -1:
        print(f"Elemen {x} ditemukan pada indeks ke-{index}")
    else:
        print(f"Elemen {x} tidak ditemukan")
elif x == "Wahyu":
    index = jumpSearch(var, x)
    if index != -1:
        print(f"Elemen {x} ditemukan pada indeks ke-{index} pada kolom 0")
    else:
        print(f"Elemen {x} tidak ditemukan pada kolom 0")
elif x == "Wibi":
    index = jumpSearch(var, x)
    if index != -1:
        print(f"Elemen {x} ditemukan pada indeks ke-{index} pada kolom 1")
    else:
        print(f"Elemen {x} tidak ditemukan pada kolom 1")
else:
    print(f"Elemen {x} tidak ditemukan")