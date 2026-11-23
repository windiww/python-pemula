def sapa(nama, platform="Santrikoding"):
    return f"Halo {nama}, selamat belajar di {platform}!"

def hitung_luas_persegi(sisi):
    return sisi * sisi

pesan = sapa("Budi")
luas = hitung_luas_persegi(6)

print(pesan)
print("Luas persegi (sisi 6):", luas)