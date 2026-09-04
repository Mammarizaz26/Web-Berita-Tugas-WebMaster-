from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = "berita.db"


#KONEKSI DATABASE
def get_db_connection():
    # row_factory bikin hasil query bisa diakses pakai nama kolom, bukan cuma index angka
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    # Bikin tabel berita kalau belum ada. Dipanggil sekali saat app pertama dijalankan.
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS berita (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            isi TEXT NOT NULL,
            penulis TEXT NOT NULL,
            tanggal TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


#READ: tampilkan semua berita
@app.route("/")
def index():
    conn = get_db_connection()
    # ORDER BY id DESC biar berita terbaru muncul paling atas
    daftar_berita = conn.execute("SELECT * FROM berita ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", daftar_berita=daftar_berita)


#READ: tampilkan satu berita detail
@app.route("/berita/<int:id>")
def detail(id):
    conn = get_db_connection()
    berita = conn.execute("SELECT * FROM berita WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template("detail.html", berita=berita)


# CREATE: tambah berita baru
@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        judul = request.form["judul"]
        isi = request.form["isi"]
        penulis = request.form["penulis"]
        tanggal = datetime.now().strftime("%Y-%m-%d %H:%M")

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO berita (judul, isi, penulis, tanggal) VALUES (?, ?, ?, ?)",
            (judul, isi, penulis, tanggal),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    # kalau method GET, tampilkan form kosong
    return render_template("tambah.html")


#UPDATE: edit berita yang sudah ada
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db_connection()

    if request.method == "POST":
        judul = request.form["judul"]
        isi = request.form["isi"]
        penulis = request.form["penulis"]

        conn.execute(
            "UPDATE berita SET judul = ?, isi = ?, penulis = ? WHERE id = ?",
            (judul, isi, penulis, id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    # kalau method GET, ambil data lama untuk ditampilkan di form
    berita = conn.execute("SELECT * FROM berita WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", berita=berita)


# DELETE: hapus berita
@app.route("/hapus/<int:id>")
def hapus(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM berita WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()  # pastikan tabel sudah dibuat sebelum app jalan
    app.run(debug=True)
