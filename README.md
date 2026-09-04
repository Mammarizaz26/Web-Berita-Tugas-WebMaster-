# Portal Berita (CRUD)

## Deskripsi Project
Aplikasi web sederhana untuk mengelola berita, dibuat menggunakan **Python (Flask)** dan **SQLite**.
Aplikasi ini menerapkan operasi **CRUD** (Create, Read, Update, Delete) penuh:

- **Create** — menambahkan berita baru lewat form.
- **Read** — menampilkan daftar semua berita di halaman utama, dan halaman detail per berita.
- **Update** — mengedit judul, penulis, dan isi berita yang sudah ada.
- **Delete** — menghapus berita dari database.

Setiap berita menyimpan: judul, isi, nama penulis, dan tanggal dibuat (otomatis).

## Struktur Project
```
portal-berita/
├── app.py              # Semua route & logika database
├── templates/
│   ├── base.html        # Layout dasar (navbar)
│   ├── index.html       # Daftar berita
│   ├── detail.html       # Detail satu berita
│   ├── tambah.html      # Form tambah berita
│   └── edit.html         # Form edit berita
└── README.md
```

## Tahapan Instalasi
1. Clone repository ini:
   ```
   git clone <URL_REPO_INI>
   cd portal-berita
   ```
2. (Opsional tapi disarankan) Buat virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```
3. Install Flask:
   ```
   pip install flask
   ```

## Tahapan Menjalankan
1. Jalankan aplikasi:
   ```
   python app.py
   ```
2. Database `berita.db` akan otomatis terbuat saat pertama kali dijalankan (tidak perlu setup manual).
3. Buka browser dan akses:
   ```
   http://127.0.0.1:5000
   ```
4. Dari halaman utama, kamu bisa:
   - Klik **"+ Tambah Berita"** untuk membuat berita baru.
   - Klik **judul berita** untuk melihat detail.
   - Klik **Edit** untuk mengubah berita.
   - Klik **Hapus** untuk menghapus berita.

## Teknologi yang Digunakan
- Python 3 + Flask (web framework)
- SQLite (database)
- Jinja2 (template engine bawaan Flask)
- Bootstrap 5 (styling, via CDN)
