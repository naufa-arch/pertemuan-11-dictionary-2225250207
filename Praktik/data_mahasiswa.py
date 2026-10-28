
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data mahasiswa tidak ditemukan")


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "2225250207": {"nama": "Hashifah Naufa Setiawan", "kelas": "3E", "nilai": 95},
    "0052530102": {"nama": "Affan", "kelas": "3E", "nilai": 78},
    "0052530103": {"nama": "Citra", "kelas": "3E", "nilai": 92},
    "0052530104": {"nama": "Deni", "kelas": "3E", "nilai": 74},
    "0052530105": {"nama": "Eka", "kelas": "3E", "nilai": 88}
}

# 1. Operasi pencarian
print("=== PENCARIAN MAHASISWA ===")
print(cari_mahasiswa(data_mahasiswa, "2225250207"))
print(cari_mahasiswa(data_mahasiswa, "0052530106"))

# 2. Operasi penambahan
print("\n=== PENAMBAHAN MAHASISWA ===")
data_mahasiswa["0052530106"] = {
    "nama": "Fani",
    "kelas": "B",
    "nilai": 80
}
print("Data Fani berhasil ditambahkan.")

# 3. Operasi pembaruan
print("\n=== PEMBARUAN NILAI ===")
data_mahasiswa["0052530102"]["nilai"] = 90
print("Nilai Affan diperbarui menjadi 90.")

# 4. Rekap seluruh mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")
for nim, mahasiswa in data_mahasiswa.items():
    print(
        f"NIM: {nim}, "
        f"Nama: {mahasiswa['nama']}, "
        f"Kelas: {mahasiswa['kelas']}, "
        f"Nilai: {mahasiswa['nilai']}"
    )

# 5. Rata-rata nilai
print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai mahasiswa: {rata_rata_nilai(data_mahasiswa):.2f}")
