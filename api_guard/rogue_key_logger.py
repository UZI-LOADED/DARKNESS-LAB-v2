from pathlib import Path
import re

env = Path("../config/app_config.env")
known_prefixes = ["SECRET_KEY", "API_KEY", "JWT_SECRET"]

lines = env.read_text().splitlines()
for line in lines:
    if re.match(r"\w+_KEY=.*", line) and not any(p in line for p in known_prefixes):
        print(f"[FLAG] Suspicious key found: {line}")
