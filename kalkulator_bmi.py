# Input data dari user
print("\n========== PROGRAM MENGHITUNG BMI ==========")
berat_badan = float(input("Masukkan berat badan (kg) : "))
tinggi_badan = float(input("Masukkan tinggi badan (meter) : "))
print("============================================")

# Proses perhitungan BMI
total_bmi = berat_badan / (tinggi_badan * tinggi_badan)
if total_bmi < 18.5:
    hasil_bmi = "Kurus"
elif total_bmi < 24.9:
    hasil_bmi = "Normal"
elif total_bmi < 29.9:
    hasil_bmi = "Gemuk"
else:
    hasil_bmi = "Obesitas"

# Tampilkan hasil perhitungan BMI
print("\n========== HASIL PERHITUNGAN BMI ===========")
print(f"Berat badan : {berat_badan}")
print(f"Tinggi badan : {tinggi_badan}")
print("============================================")
print(f"Total BMI : {total_bmi:.2f}")
print(f"Status BMI : {hasil_bmi}")
print("============================================")