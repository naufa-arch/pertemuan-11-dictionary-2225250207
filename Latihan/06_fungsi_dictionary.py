def cari(data, nim):
    return data.get(nim, "Data tidak ditemukan")

mahasiswa = {
    "2225250207": {"nama": "Hashifah Naufa Setiawan", "nilai": 95},
    "0052530102": {"nama": "Affan", "nilai": 80}
}

print(cari(mahasiswa, "2225250207"))
print(cari(mahasiswa, "0052530102"))