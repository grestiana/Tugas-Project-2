class Penilaian:
    """Kelas untuk menyimpan nilai dan menghitung nilai akhir mahasiswa."""

    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def nilai_akhir(self):
        return (0.15 * self.quiz) + (0.25 * self.tugas) + (0.25 * self.uts) + (0.35 * self.uas)

    def validasi_nilai(self):
        for nilai in [self.quiz, self.tugas, self.uts, self.uas]:
            if not 0 <= nilai <= 100:
                raise ValueError("Nilai harus antara 0–100.")
