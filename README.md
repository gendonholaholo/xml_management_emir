# XML Processing Automation

## 📖 Deskripsi
Skrip ini secara otomatis membaca semua file `.xml` dalam folder `Data/`, memodifikasi elemen `<JVNUMBER>` dengan menambahkan `000` di belakang angka, lalu menyimpannya ke dalam folder `Data/modified/`.

---

## 📁 Struktur Folder
```
C:.
\---Data
│   │   B1.xml
│   │   B10.xml
│   │   B11.xml
│   │   B12.xml
│   │   B13.xml
│   │   B2.xml
│   │   B3.xml
│   │   B4.xml
│   │   B5.xml
│   │   B6.xml
│   │   B7.xml
│   │   B8.xml
│   │   B9.xml
│   │
│   ├── modified  # Folder hasil modifikasi
│   │   │   B1.xml
│   │   │   B10.xml
│   │   │   B11.xml
│   │   │   B12.xml
│   │   │   B13.xml
│   │   │   B2.xml
│   │   │   B3.xml
│   │   │   B4.xml
│   │   │   B5.xml
│   │   │   B6.xml
│   │   │   B7.xml
│   │   │   B8.xml
│   │   │   B9.xml
│   │
│   ├── apps  # Folder tempat skrip Python
│   │   │   process_xml.py  # Skrip utama untuk memproses file XML
│   │   │   README.md  # Dokumentasi proyek
│   │   │   requirements.txt  # Daftar dependensi (jika ada)
│   │
│   ├── logs  # Folder untuk menyimpan log proses
│   │   │   process.log  # File log hasil pemrosesan XML
```

---

## 🖥️ Cara Kerja Aplikasi
1. **Skrip `process_xml.py` akan membaca semua file XML** yang ada di folder `Data/`.
2. **Melakukan parsing XML** & mencari elemen `<JVNUMBER>`.
3. **Menambahkan "000" di belakang angka** dalam setiap `<JVNUMBER>`.
4. **Menyimpan hasil ke dalam `Data/modified/`** dengan nama yang sama.
5. **Membuat log proses di `logs/process.log`** untuk pencatatan hasil.

---

## 📜 Detail Setiap Komponen
| Komponen         | Deskripsi |
|-----------------|-----------|
| **`Data/`** | Folder utama yang menyimpan semua file XML asli. |
| **`Data/modified/`** | Folder untuk menyimpan file XML yang telah dimodifikasi. |
| **`Data/apps/`** | Folder tempat menyimpan skrip Python untuk pemrosesan. |
| **`Data/logs/`** | Folder untuk menyimpan file log dari proses pemrosesan XML. |
| **`process_xml.py`** | Skrip Python yang menangani proses parsing dan modifikasi XML. |
| **`README.md`** | Dokumentasi tentang cara menjalankan aplikasi. |
| **`requirements.txt`** | File daftar dependensi Python (jika ada). |
| **`logs/process.log`** | File log untuk mencatat hasil pemrosesan XML. |


## 🚀 Cara Menjalankan
1. **Pastikan Python terinstal** (disarankan versi 3.7+).
2. **Jalankan skrip dengan perintah berikut** di dalam terminal/cmd:
   ```sh
   python apps/process_xml.py
   ```
3. **Cek folder `Data/modified/`** untuk melihat hasil modifikasi.
4. **Cek file `logs/process.log`** jika ingin melihat hasil log pemrosesan.

---
~Mas Gendon
