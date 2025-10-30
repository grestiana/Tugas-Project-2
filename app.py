import csv
from tracker.mahasiswa import Mahasiswa
from tracker.penilaian import Penilaian
from tracker.rekap_kelas import RekapKelas
from tracker.report import build_markdown_report, save_text


def load_data_from_csv(rekap):
    """Muat data mahasiswa dan nilai dari file CSV."""
    try:
        with open("data/attendance.csv", "r", encoding="utf-8") as f1, \
             open("data/grades.csv", "r", encoding="utf-8") as f2:

            attendances = csv.DictReader(f1)
            grades = csv.DictReader(f2)

            # Tambah mahasiswa dari attendance.csv
            for row in attendances:
                nim = row["nim"]
                nama = row["nama"]
                hadir = float(row["hadir"])
                mhs = Mahasiswa(nim, nama, hadir)
                rekap.tambah_mahasiswa(mhs, Penilaian())

            # Masukkan nilai dari grades.csv
            for row in grades:
                nim = row["nim"]
                if nim in rekap.data:
                    rekap.set_penilaian(
                        nim,
                        float(row["quiz"]),
                        float(row["tugas"]),
                        float(row["uts"]),
                        float(row["uas"])
                    )

        print("✅ Data berhasil dimuat dari CSV.")

    except FileNotFoundError:
        print("⚠️ File CSV belum ditemukan di folder 'data/'. Pastikan file attendance.csv dan grades.csv ada.")


def main():
    rekap = RekapKelas()

    while True:
        print(f"\n=== Student Performance Tracker === (Total data: {len(rekap.data)})")
        print("1) Muat data dari CSV")
        print("2) Tambah mahasiswa")
        print("3) Ubah presensi")
        print("4) Ubah nilai")
        print("5) Lihat rekap")
        print("6) Simpan laporan Markdown")
        print("7) Keluar")

        pilihan = input("Pilih menu: ")

        # ===== MENU 1 =====
        if pilihan == "1":
            load_data_from_csv(rekap)

        # ===== MENU 2 =====
        elif pilihan == "2":
            nim = input("NIM: ")
            nama = input("Nama: ")
            hadir = float(input("Persentase hadir (%): "))
            mhs = Mahasiswa(nim, nama, hadir)
            nilai = Penilaian()
            rekap.tambah_mahasiswa(mhs, nilai)
            print(f"✅ Mahasiswa {nama} berhasil ditambahkan dengan kehadiran {hadir:.1f}%.")

        # ===== MENU 3 =====
        elif pilihan == "3":
            nim = input("NIM: ")
            if nim not in rekap.data:
                print("⚠️ NIM tidak ditemukan.")
                continue
            persen = float(input("Persentase hadir baru (%): "))
            rekap.set_hadir(nim, persen)
            print(f"✅ Data presensi berhasil diubah menjadi {persen:.1f}%.")

        # ===== MENU 4 =====
        elif pilihan == "4":
            nim = input("NIM: ")
            if nim not in rekap.data:
                print("⚠️ NIM tidak ditemukan.")
                continue
            quiz = float(input("Nilai Quiz: "))
            tugas = float(input("Nilai Tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
            rekap.set_penilaian(nim, quiz, tugas, uts, uas)
            print("✅ Nilai berhasil diperbarui.")

        # ===== MENU 5 =====
        elif pilihan == "5":
            data = rekap.rekap()
            if not data:
                print("⚠️ Belum ada data mahasiswa.")
            else:
                print("\nNIM        | Nama            | Hadir (%) | Nilai Akhir | Predikat")
                print("-" * 70)
                for row in data:
                    print(f"{row['nim']:<10} | {row['nama']:<15} | {row['hadir']:>8.1f}% | {row['nilai_akhir']:>12.2f} | {row['predikat']:^9}")

        # ===== MENU 6 =====
        elif pilihan == "6":
            records = rekap.rekap()
            if not records:
                print("⚠️ Tidak ada data untuk disimpan.")
            else:
                content = build_markdown_report(records)
                save_text("out/report.md", content)
                print("✅ Laporan tersimpan di out/report.md")

        # ===== MENU 7 =====
        elif pilihan == "7":
            print("👋 Keluar dari program...")
            break

        # ===== MENU INVALID =====
        else:
            print("❌ Pilihan tidak valid. Silakan pilih 1–7.")


if __name__ == "__main__":
    main()
