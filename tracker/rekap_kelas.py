class RekapKelas:
    """Mengelola daftar mahasiswa dan nilai mereka."""

    def __init__(self):
        self.data = {}

    def tambah_mahasiswa(self, mhs, penilaian):
        self.data[mhs.nim] = {'mhs': mhs, 'nilai': penilaian}

    def set_hadir(self, nim, persen):
        self.data[nim]['mhs'].hadir_persen = persen

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        p = self.data[nim]['nilai']
        p.quiz, p.tugas, p.uts, p.uas = quiz, tugas, uts, uas

    def predikat(self, nilai):
        if nilai >= 85: return 'A'
        elif nilai >= 75: return 'B'
        elif nilai >= 65: return 'C'
        elif nilai >= 50: return 'D'
        else: return 'E'

    def rekap(self):
        records = []
        for nim, item in self.data.items():
            mhs = item['mhs']
            p = item['nilai']
            nilai_akhir = p.nilai_akhir()
            records.append({
                'nim': mhs.nim,
                'nama': mhs.nama,
                'hadir': mhs.hadir_persen,
                'nilai_akhir': nilai_akhir,
                'predikat': self.predikat(nilai_akhir)
            })
        return records
