import curses
import time
import re
from pathlib import Path
import hashlib

WATCH_FILE = "../config/app_config.env"
KNOWN_KEYS = ["SECRET_KEY", "API_KEY", "JWT_SECRET", "DATABASE_PASSWORD"]
prev_hash = None

def get_env_keys():
    path = Path(WATCH_FILE)
    keys = []
    if path.exists():
        lines = path.read_text().splitlines()
        for line in lines:
            if '=' in line:
                key, _ = line.split('=', 1)
                keys.append(key)
    return keys

def hash_file():
    path = Path(WATCH_FILE)
    return hashlib.sha256(path.read_bytes()).hexdigest()

def monitor(stdscr):
    global prev_hash
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(1000)

    prev_hash = hash_file()

    while True:
        stdscr.erase()
        stdscr.addstr(0, 2, "🛡️  Real-Time Env Monitor", curses.A_BOLD)

        keys = get_env_keys()
        suspicious = [k for k in keys if k not in KNOWN_KEYS]

        stdscr.addstr(2, 2, f"Known Keys: {', '.join(k for k in keys if k in KNOWN_KEYS)}")
        stdscr.addstr(3, 2, f"Suspicious Keys: {', '.join(suspicious) or 'None'}")

        current_hash = hash_file()
        if current_hash != prev_hash:
            stdscr.addstr(5, 2, "⚠️  CONFIG TAMPERED!", curses.A_BLINK | curses.A_BOLD)
            prev_hash = current_hash
        else:
            stdscr.addstr(5, 2, "✅ Config Intact", curses.color_pair(2))

        stdscr.refresh()
        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(monitor)

