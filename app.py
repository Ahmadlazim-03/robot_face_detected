from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Definisikan rute untuk halaman utama
@app.route('/')
def index():
    # Perintah ini akan mencari dan menampilkan file 'index.html' dari folder 'templates'
    return render_template('index.html')

# Jalankan server saat script dieksekusi
if __name__ == '__main__':
    app.run(debug=True)