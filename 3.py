def jumlah_deret_ganjil(n):
    if n < 1:
        return 0
    
    if n % 2 == 0:
        return "Input harus berupa bilangan ganjil."
    
    if n == 1:
        return 1
    
    return n + jumlah_deret_ganjil(n - 2)

n = int(input("Masukkan bilangan ganjil terakhir dalam deret: "))
if n % 2 != 0:
    print(f"Jumlah deret ganjil 1 + 3 + 5 + ... + {n} adalah {jumlah_deret_ganjil(n)}.")
else:
    print("Input harus berupa bilangan ganjil.")

