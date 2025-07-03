import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi Google AI dengan API Key dari environment variable
try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("Model AI berhasil dimuat.")
except Exception as e:
    print(f"Error konfigurasi Google AI: {e}")
    model = None

# Rute untuk halaman utama (tidak berubah)
@app.route('/')
def index():
    return render_template('index.html')

# Rute BARU untuk menerima pertanyaan dan mengirimnya ke AI
@app.route('/ask', methods=['POST'])
def ask():
    if not model:
        return jsonify({"error": "Model AI tidak terkonfigurasi dengan benar."}), 500

    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Tidak ada pesan yang diterima."}), 400

    try:
        # Kirim pesan ke model Gemini dan dapatkan responsnya
        response = model.generate_content(user_message)
        ai_response = response.text
        return jsonify({"reply": ai_response})
    except Exception as e:
        print(f"Error saat menghasilkan konten: {e}")
        return jsonify({"error": str(e)}), 500

# Jalankan server
if __name__ == '__main__':
    app.run(debug=True)