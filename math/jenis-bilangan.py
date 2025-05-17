import math
from fractions import Fraction

def parse_input(user_input):
    allowed_names = {
        "math": math,
        "pi": math.pi,
        "sqrt": math.sqrt,

    }
    user_input = user_input.replace("π", "math.pi").replace("√", "math.sqrt").replace("^", "**")
    return eval(user_input, {"__builtins__": {}}, allowed_names)

def adalah_prima(n):
    if not float(n).is_integer():
        return False
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def klasifikasi_bilangan(x):
    try:
        frac = Fraction(x).limit_denominator()
        if float(frac) == x:
            print(f"{x} adalah bilangan rasional (bisa ditulis sebagai pecahan)")
        else:
            print(f"{x} adalah bilangan irasional (aproksimasi)")
    except:
        print(f"{x} adalah bilangan irasional (tidak bisa direpresentasikan sebagai pecahan)")

# MAIN UI
print("PENGKATEGORIAN JENIS BILANGAN")
print("-----------by: ryo-----------")
try:
    print("(contoh: 3, 2.5, -2, sqrt(2), pi, 2^3, 1/3)")

    x = parse_input(input("Masukkan bilangan: "))

    x_float = float(x)
except Exception as e:
    print(f"Input tidak valid. \nGunakan format seperti 3, 2.5, -2, sqrt(2), pi, 2**0.5, 1/3")
    exit()
print("-----------------------------")

# Positif/Negatif/Nol
if x_float > 0:
    print(f"{x_float} adalah bilangan positif")
elif x_float < 0:
    print(f"{x_float} adalah bilangan negatif")
else:
    print(f"{x_float} adalah bilangan nol")

# Bulat / Genap / Ganjil
if x_float.is_integer():
    x_int = int(x_float)
    print(f"{x_int} adalah bilangan bulat")
    if x_int % 2 == 0:
        print(f"{x_int} adalah bilangan genap")
    else:
        print(f"{x_int} adalah bilangan ganjil")
else:
    print(f"{x_float} adalah bilangan desimal/pecahan")

# Prima / Komposit
if x_float.is_integer() and x_float > 0:
    if adalah_prima(x_float):
        print(f"{int(x_float)} adalah bilangan prima")
    elif int(x_float) > 1:
        print(f"{int(x_float)} adalah bilangan komposit/non-prima")
    else:
        print(f"{int(x_float)} bukan bilangan prima atau komposit")
else:
    print(f"{x_float} bukan bilangan prima (bukan bilangan bulat positif)")

# Rasional / Irrasional
klasifikasi_bilangan(x_float)

print("-----------------------------")
print("Terima kasih sudah menggunakan program ini :)")