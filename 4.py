def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
try:
    number = int(input("Masukkan bilangan bulat: "))
    total = sum_of_digits(abs(number))  
    print(f"Jumlah digit dari {number} adalah: {total}")
except ValueError:
    print("Silakan masukkan bilangan bulat yang valid.")