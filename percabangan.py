nilai = 82

if nilai >= 90:
    predikat = "A"
elif nilai >= 80:
    predikat = "B"
elif nilai >= 70:
    predikat = "C"
else:
    predikat = "D"

print("Nilai:", nilai)
print("Predikat:", predikat)
print("Status kelulusan:", "Lulus" if nilai >= 75 else "Perlu remedial")