# WiFi Spedee 🚀

**wifi spedee** adalah alat CLI ringan berbasis Python untuk menguji dan memantau kecepatan *download* & *upload* jaringan secara *real-time* di Terminal Linux dan Termux (Android).

## 📌 Fitur
- Monitoring kecepatan *download* & *upload* real-time.
- Visualisasi grafik bar sederhana di terminal.
- Sangat ringan dan mudah dijalankan di Termux/Linux.

## 📥 Cara Install & Jalankan

### Di Termux (Android):
```bash
pkg update && pkg install python git -y
git clone [https://github.com/MRPEGASUS-ctrl/wifi-spedee.git](https://github.com/MRPEGASUS-ctrl/wifi-spedee.git)
cd wifi-spedee
pip install -r requirements.txt
python wifi_spedee.py

### Di Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3 python3-pip git -y
git clone [https://github.com/MRPEGASUS-ctrl/wifi-spedee.git](https://github.com/MRPEGASUS-ctrl/wifi-spedee.git)
cd wifi-spedee
pip install -r requirements.txt
python3 wifi_spedee.py
