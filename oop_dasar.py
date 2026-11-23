class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Halo, saya {self.nama} dari kelas {self.kelas}."

siswa_1 = Siswa("Windi", "XI RPL")
print(siswa_1.perkenalan())