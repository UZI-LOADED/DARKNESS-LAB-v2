#!/bin/bash
echo "[+] Deploying Extended Darkness Lab..."

mkdir -p ../config
echo "SECRET_KEY=$(openssl rand -hex 32)" > ../config/app_config.env

echo "[+] Starting File Guardian..."
python3 ../defender/file_hash_guardian.py &

echo "[+] Launching Real-Time Monitor..."
python3 ../monitor/realtime_audit_tui.py
