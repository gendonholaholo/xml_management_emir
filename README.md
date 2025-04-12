# XML Processing Automation

## Deskripsi
Skrip Python ini secara otomatis membaca semua file `.xml` dalam folder sumber (default: `Data/`), memodifikasi elemen `<JVNUMBER>` dengan menambahkan akhiran (suffix) yang ditentukan (default: `000`), lalu menyimpannya ke dalam folder keluaran (default: `Data/modified/`). Proses ini juga dicatat dalam file log (default: `logs/process.log`).

---

## Struktur Folder yang Direkomendasikan
```
C:. (Project Root)
├── Data/              # Folder berisi file XML asli
│   ├── B1.xml
│   └── ...
├── apps/              # Folder skrip Python
│   ├── process_xml.py   # Skrip utama
│   └── requirements.txt # Dependensi Python
├── logs/              # Folder log (dibuat otomatis)
│   └── process.log    # File log (dibuat otomatis)
├── .gitignore
└── README.md

# Catatan: Folder Data/modified/ akan dibuat otomatis di dalam Data/ saat skrip berjalan.
```

---

## Cara Kerja Aplikasi
1.  Skrip `process_xml.py` dijalankan dari *root* direktori proyek.
2.  Membaca argumen baris perintah (`--source`, `--output`, `--suffix`). Jika tidak ada argumen, nilai default akan digunakan.
3.  Memeriksa keberadaan folder sumber (`Data/` secara default).
4.  Membaca semua file yang berakhiran `.xml` di dalam folder sumber.
5.  Melakukan parsing XML dan mencari elemen `<JVNUMBER>`.
6.  Menambahkan *suffix* yang ditentukan (default: `000`) di belakang teks dalam setiap `<JVNUMBER>` yang valid.
7.  Menyimpan hasil modifikasi ke folder keluaran (`Data/modified/` secara default) dengan nama file yang sama.
8.  Membuat log proses di `logs/process.log`.

---

## Detail Komponen
| Komponen                | Deskripsi |
|-------------------------|-----------|
| **`Data/`**             | Folder utama yang menyimpan semua file XML asli (default). Lokasi bisa diubah via `--source`. |
| **`Data/modified/`**    | Folder untuk menyimpan file XML yang telah dimodifikasi (default). Lokasi bisa diubah via `--output`. |
| **`apps/`**             | Folder tempat menyimpan skrip Python dan dependensinya. |
| **`logs/`**             | Folder untuk menyimpan file log (dibuat otomatis). |
| **`process_xml.py`**    | Skrip Python yang menangani proses parsing dan modifikasi XML menggunakan argumen baris perintah. |
| **`requirements.txt`**  | File daftar dependensi Python (`rich`). |
| **`logs/process.log`**  | File log untuk mencatat hasil pemrosesan XML (dibuat otomatis). |
| **`.gitignore`**        | Mengatur file/folder yang diabaikan oleh Git. |
| **`README.md`**         | Dokumentasi ini. |


## Cara Menjalankan

1.  **Pastikan Python terinstal** (disarankan versi 3.7+).
2.  **Buka terminal/cmd** di direktori *root* proyek (`xml_management_emir`).
3.  **(Opsional) Instal dependensi:** Jika ini pertama kali atau ada perubahan pada `requirements.txt`:
    ```sh
    pip install -r apps/requirements.txt
    ```
4.  **Jalankan skrip:**

    *   **Menggunakan pengaturan default** (sumber: `Data/`, output: `Data/modified/`, suffix: `000`):
        ```sh
        python apps/process_xml.py
        ```

    *   **Menentukan suffix kustom** (misalnya, menambahkan `XYZ`):
        ```sh
        python apps/process_xml.py --suffix XYZ
        ```

    *   **Menentukan folder sumber dan output yang berbeda:**
        ```sh
        python apps/process_xml.py --source path/ke/folder/input --output path/ke/folder/output
        ```

    *   **Menggabungkan argumen:**
        ```sh
        python apps/process_xml.py --source D:/MyXML --output D:/MyXML/Processed --suffix _DONE
        ```

5.  **Cek folder output** (default: `Data/modified/`) untuk melihat hasil modifikasi.
6.  **Cek file `logs/process.log`** jika ingin melihat detail log pemrosesan.

---
~Mas Gendon
