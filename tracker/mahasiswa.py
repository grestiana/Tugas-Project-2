class Mahasiswa:
    """Kelas untuk menyimpan data mahasiswa."""

    def __init__(self, nim, nama, hadir_persen=0):
        self.nim = nim
        self.nama = nama
        self._hadir_persen = hadir_persen

    @property
    def hadir_persen(self):
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        if 0 <= value <= 100:
            self._hadir_persen = value
        else:
            raise ValueError("Persentase kehadiran harus antara 0–100.")

    def info(self):
        return f"{self.nim} - {self.nama} ({self.hadir_persen}%)"
