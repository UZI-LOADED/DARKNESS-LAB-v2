import hashlib, time, shutil
from pathlib import Path

watched = Path("../config/app_config.env")
backup = Path("backup.env")

def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def restore_backup():
    shutil.copy2(backup, watched)
    print("[RECOVERY] Secret restored from backup.")

initial_hash = hash_file(watched)
shutil.copy2(watched, backup)

while True:
    time.sleep(3)
    if hash_file(watched) != initial_hash:
        print("[ALERT] Tampering detected!")
        restore_backup()
        break
