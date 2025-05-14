# Program Perhitungan BMI

print("Perhitungan BMI (BODY MASS INDEX)")
print("-------------by: ryo-------------")
bb = int(input("Masukkan berat badan Anda (kg): "))
tb = float(input("Masukkan tinggi badan Anda (m): "))

bmi = bb / tb**2

bbideal = dict()
bbideal['bawah'] = 18.5*(tb**2)
bbideal['atas'] = 25*(tb**2)


if bmi < 18.5:
    kategori = "Berat badan Anda kurang ideal, naikkan berat badan Anda!"
elif bmi >= 18.5 and bmi <= 25:
    kategori = "Berat badan Anda ideal!"
elif bmi >= 25 and bmi <= 30:
    kategori = "Berat badan Anda kurang ideal, kurangi berat badan Anda!"
else:
    kategori = "Anda sangat kelebihan berat badan (Obesitas), mohon kurangi berat badan Anda!"

print("\nHasil kalkulator BMI Anda adalah:")
print("--------------------------------")
print(kategori)

print(f"Berat badan ideal Anda adalah dalam rentang " f"{bbideal['bawah']:.2f} kg - {bbideal['atas']:.2f} kg")

print("--------------------------------")
print(f"BODY MASS INDEKS ANDA: {bmi:.2f} kg/m^2")
print("Note: BMI normal adalah dalam rentang 18.5 kg/m^2 - 25 kg/m^2")

print("--------------------------------")
print("Terima kasih sudah menggunakan program ini :)")