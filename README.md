# Pertemuan 11 - Dictionary/Map

**Nama:** Hashifah Naufa Setiawan 
**NIM:** 2225250207 
**Kelas:** 3E

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value, serta menerapkan operasi pencarian, penambahan, pembaruan, dan rekap data mahasiswa menggunakan Python.

## Struktur Data

Program menggunakan dictionary bernama `data_mahasiswa` untuk menyimpan data mahasiswa berdasarkan NIM.

- **Key utama:** NIM mahasiswa, seperti `"A001"`, `"A002"`, dan seterusnya.
- **Value:** Dictionary yang berisi informasi mahasiswa, yaitu nama, kelas, dan nilai.
- **Key di dalam:** `"nama"`, `"kelas"`, dan `"nilai"`.
- **Value di dalam:** Informasi sesuai dengan setiap key, misalnya nama `"Ayu"`, kelas `"A"`, dan nilai `85`.

Struktur ini disebut *nested dictionary*, yaitu dictionary yang memiliki dictionary lain sebagai value.

Program juga menggunakan fungsi `cari_mahasiswa(data, nim)` untuk mencari data berdasarkan NIM dan fungsi `rata_rata_nilai(data)` untuk menghitung rata-rata nilai mahasiswa.

## Cara Menjalankan

Jalankan program melalui terminal VS Code dengan perintah:

```bash
python3 praktik/data_mahasiswa.py
```

Jika menggunakan Windows dan perintah tersebut tidak bisa dijalankan, gunakan:

```bash
python praktik/data_mahasiswa.py
```

## Test Case

| No. | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Mencari NIM `A002` | Data Budi ditemukan dengan nilai 78 sebelum pembaruan | Data Budi ditemukan | Berhasil |
| 2 | Mencari NIM `A006` sebelum penambahan | Menampilkan pesan data tidak ditemukan | Data tidak ditemukan | Berhasil |
| 3 | Menambahkan mahasiswa NIM `A006` | Data Fani, kelas B, nilai 80 berhasil ditambahkan | Data berhasil ditambahkan | Berhasil |
| 4 | Mengubah nilai Budi menjadi 90 | Nilai Budi berubah dari 78 menjadi 90 | Nilai berubah menjadi 90 | Berhasil |
| 5 | Menampilkan seluruh data mahasiswa | Semua data mahasiswa ditampilkan | Data mahasiswa ditampilkan | Berhasil |
| 6 | Menghitung rata-rata nilai setelah penambahan dan pembaruan | Rata-rata nilai sebesar 84,83 | Rata-rata nilai 84,83 | Berhasil |

*Catatan: Hasil aktual dan status di atas merupakan hasil yang diharapkan berdasarkan kode program. Sesuaikan dengan hasil yang benar-benar muncul ketika program dijalankan.*

## Refleksi

Salah satu kesalahan akses key yang dapat terjadi adalah menggunakan key yang tidak tersedia dalam dictionary, misalnya `data_mahasiswa["A006"]` sebelum data mahasiswa dengan NIM tersebut ditambahkan. Kesalahan ini dapat menyebabkan `KeyError`.

Cara memperbaikinya adalah menggunakan method `.get()`, misalnya `data_mahasiswa.get("A006", "Data mahasiswa tidak ditemukan")`. Dengan cara tersebut, program dapat menampilkan pesan apabila key tidak ditemukan tanpa menyebabkan `KeyError`.

Melalui latihan ini, saya memahami bahwa dictionary dapat digunakan untuk menyimpan dan mengelola data mahasiswa berdasarkan NIM. Saya juga mempelajari cara mencari, menambahkan, memperbarui, dan menampilkan data serta menghitung rata-rata nilai menggunakan fungsi dan perulangan Python.