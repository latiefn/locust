# WireMock Load Testing with Locust 🚀

Repositori ini berisi skrip pengujian beban (*load testing*) untuk layanan API **NahSehat** yang berjalan di atas WireMock. Proyek ini bertujuan untuk memantau performa layanan selama pengujian beban berlangsung.

## 🛠️ Tech Stack
- **Python**: Bahasa pemrograman utama.
- **Locust**: Framework load testing berbasis Python.
- **python-dotenv**: Manajemen konfigurasi lingkungan.
- **WireMock**: Service virtualization/mocking.

## 📋 Prasyarat
- Python 3.10+
- Akses ke server (IP: `127.0.0.1`)

## 🚀 Cara Menjalankan
1. **Clone Repositori**:
    ```bash
    git clone <url-repo-anda>
    cd <nama-folder>

2. **Setup Environtment**:
    python3 -m venv venv
    source venv/bin/activate

3. **Instal Dependensi**:
    ```bash
    pip install -r requirements.txt

4.  **Konfigurasi .env**:
    ```bash
    Salin .env.example menjadi .env dan sesuaikan TARGET_HOST

5. **Jalankan Locust**:
    ```bash
    locust -f locustfile.py
