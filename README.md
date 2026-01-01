## Aplikasi Berita Sederhana

Aplikasi berita sederhana berbasis Flask dan SQLite untuk demonstrasi CRUD (Create, Read, Update, Delete).

## Setup (Linux)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

Atau jalankan langsung:

```bash
python app.py
```

Buka http://127.0.0.1:5000 untuk melihat aplikasi.

## Struktur singkat

- `app.py` - aplikasi Flask utama, model `Article` dan route CRUD.
- `templates/` - template Jinja2 untuk list, form, dan detail.
- `requirements.txt` - dependensi minimal.

## Catatan

Database SQLite akan dibuat secara otomatis sebagai `articles.db` di folder proyek saat aplikasi dijalankan pertama kali.
