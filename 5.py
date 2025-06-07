def kombinasi(n, r):
    """Fungsi untuk menghitung kombinasi C(n, r) secara rekursif."""
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

n = 5
r = 2
print(f"Kombinasi C({n}, {r}) = {kombinasi(n, r)}")
