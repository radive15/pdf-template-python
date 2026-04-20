# pdf-template-python

Program ini secara otomatis membuat file PDF berisi halaman-halaman kosong berdasarkan daftar topik yang kamu siapkan.

## Kegunaan

Cocok digunakan untuk membuat **template buku catatan**, **modul belajar**, atau **lembar kerja** — di mana setiap topik sudah punya jumlah halaman yang ditentukan sejak awal.

## Cara Pakai

### 1. Siapkan daftar topik

Edit file `topics.csv` sesuai kebutuhan. Formatnya seperti ini:

```
Topic,Pages
Matematika,5
Bahasa Indonesia,3
IPA,4
```

- **Topic** — nama topik yang akan muncul sebagai judul dan footer
- **Pages** — jumlah halaman untuk topik tersebut

### 2. Jalankan program

Pastikan sudah menginstall Python, lalu jalankan perintah berikut di terminal:

```bash
pip install fpdf pandas
python main.py
```

### 3. Ambil hasilnya

File PDF akan tersimpan otomatis dengan nama **`lembar.pdf`** di folder yang sama.

## Contoh Hasil

Setiap topik akan menghasilkan:
- Halaman pertama dengan **judul topik** di atas dan nama topik kecil di bawah
- Halaman-halaman berikutnya yang **kosong** (hanya ada nama topik kecil di bawah)
