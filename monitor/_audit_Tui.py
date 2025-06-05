from pathlib import Path
import time
from rich.console import Console

log_file = Path("monitor/logs/system.log")
console = Console()

def tail_log():
    with log_file.open("r") as f:
        f.seek(0, 2)  # Go to the end of the file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            console.print(f"[green]LOG[/green]: {line.strip()}")

if __name__ == "__main__":
    console.print("[bold cyan]🛡️ DARKNESS Monitor Started[/bold cyan]")
    tail_log()
