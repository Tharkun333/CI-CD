def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a# arithmetic.py

