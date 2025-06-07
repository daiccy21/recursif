def is_prime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

try:
    number = int(input("Masukkan bilangan bulat positif: "))
    if is_prime(number):
        print(f"{number} adalah bilangan prima.")
    else:
        print(f"{number} bukan bilangan prima.")
except ValueError:
    print("Silakan masukkan bilangan bulat positif yang valid.")



