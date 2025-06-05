#!/bin/bash
echo "[+] Creating .env"
echo "SECRET_KEY=InitSecretKey123456" > ../config/app_config.env

echo "[+] Launching Defender"
python3 ../defender/file_hash_guardian.py &

echo "[+] Launching Monitor"
python3 ../monitor/realtime_audit_tui.py &

echo "[+] Ready. Begin testing injectors and encryptors manually."
