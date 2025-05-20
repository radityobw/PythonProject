import time
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def count_primes_for_one_minute():
    count = 0
    number = 2
    start_time = time.time()
    while time.time() - start_time < 60:
        if is_prime(number):
            count += 1
        number += 1
    return count

if __name__ == "__main__":
    print("Menghitung jumlah bilangan prima dalam 1 menit...")
    total_primes = count_primes_for_one_minute()
    print(f"Total bilangan prima yang ditemukan dalam 1 menit: {total_primes}")