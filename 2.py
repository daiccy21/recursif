def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

if __name__ == "__main__":
    text = input("Masukkan kalimat untuk dicek apakah palindrome: ")
    if is_palindrome_recursive(text):
        print(f'"{text}" adalah palindrome.')
    else:
        print(f'"{text}" bukan palindrome.')
