# H I J A C K

Hijax adalah framework red team modular yang dibangun untuk mendemonstrasikan dan mensimulasikan **session hijacking** dari browser dan host yang terinfeksi. Framework ini mengekstrak token dan mengambil alih sesi yang terautentikasi di berbagai platform:

* Discord
* Instagram
* Google
* Facebook
* iCloud
* Dan platform lain yang menyimpan session cookies atau OAuth tokens

> **Hanya untuk tujuan pendidikan dan pengujian etis. Jangan gunakan pada target yang tidak Anda miliki atau tanpa izin eksplisit untuk melakukan penilaian.**

---

## Fitur

* Ekstrak session cookies live dari Chrome/Firefox
* Ambil alih sesi melalui injeksi cookie browser
* Replay sesi melalui akses API (tidak perlu GUI)
* Memantau clipboard untuk token Discord atau JWT
* Menjatuhkan implant browser atau remote untuk eksfiltrasi pasif
* Auto-generate **implant script** mandiri untuk di-deploy ke sistem remote

## Instalasi

### Clone Repositori

```bash
git clone https://github.com/username/hijack.git
cd hijack
```

### Instalasi Dependensi

```bash
sudo apt update && sudo apt install -y python3 python3-pip chromium-driver curl jq unzip
pip3 install selenium requests browser-cookie3 beautifulsoup4 pycryptodome pyperclip --break-system-packages
```

---

## Cara Penggunaan

### Menjalankan CLI

```bash
python3 hijack_cli.py
```

Ini akan memberikan Anda:

![hijack]()

---

### Cookie Harvester

```bash
python3 token_harvester.py
```

* Mengekstrak session cookies dari Chrome/Firefox
* Menyimpan semua ke `loot/stolen_tokens.txt`
* Mencatat IP, hostname, timestamp, dan platform

---

### Clipboard Token Monitor

```bash
python3 utils/clipboard_monitor.py
```

* Memantau 24/7 untuk token Discord, JWT, MFA yang disalin ke clipboard
* Menulis hasil langsung ke `loot/stolen_tokens.txt`

---

### Token Injection (Browser Hijack)

```bash
python3 token_injector.py
```

* Meluncurkan Chromium dengan Selenium
* Menyuntikkan cookie yang dicuri ke dalam sesi live
* Melewati login/2FA dan menyamar sebagai korban

---

### Headless API Replay (Tanpa GUI)

```bash
python3 token_replayer.py
```

* Memungkinkan recon, dumping DM, daftar file, dll. melalui API
* Bekerja dengan Discord, Instagram, Facebook, Google, dan lainnya
* Tidak perlu GUI — semua impersonation berbasis token

---

## Implant Builder (BARU!)

```bash
[4] Generate Implant via CLI
```

* Auto-generate implant Python yang berfungsi penuh:

  * `hijack_remote_implant.py`
* Dapat di-deploy pada sistem remote untuk mengekstrak dan mengirim token kembali
* Mencatat cookies Chrome + fingerprint perangkat
* Mengirim data ke webhook Anda atau menyimpan secara lokal
* Tidak ada dependensi malware, sederhana dan stealthy

Gunakan ini ketika:

* Anda ingin stealer kredensial
* Anda ingin membundelnya ke dalam payload lain
* Anda ingin menyajikan implant melalui QR/link

---

## Integrasi payload

Hijack sudah dirancang untuk bekerja secara native dengan untuk pengiriman payload berbasis browser.

### Payload: `hijax_browser_implant.html`

* Mengambil:

  * `document.cookie`
  * `window.localStorage`
  * Isi clipboard (jika tersedia)
* Mengirimkannya ke:

  ```
  POST /api/hijax
  ```
* Output disimpan di: `loot/hijack_loot.txt`
* Opsional redirect ke situs legit (contoh: Google account)

---

## Sumber Token & Metode

| Platform  | Metode                    | Sumber                 |
| --------- | ------------------------- | ---------------------- |
| Discord   | `token`, `__dcfduid`      | Cookie atau clipboard  |
| Instagram | `sessionid`, `ds_user_id` | Cookie                 |
| Google    | `SID`, `SAPISID`          | Cookie                 |
| Facebook  | `c_user`, `xs`            | Cookie                 |
| iCloud    | `MEAuthToken`             | Cookie atau localStorage |

---

## Workflow Red Team

1. Harvest atau generate implant dari Hijack CLI
2. Sajikan implant deploy langsung
3. Token diekstrak ke mesin penyerang
4. Replay sesi atau inject ke browser Selenium
5. Dump data pengguna, pesan, sesi, dll.

---

## Penafian

Hijack hanya untuk tujuan **pendidikan**, **penelitian**, dan **simulasi red team**.

**Jangan** gunakan terhadap sistem, individu, atau jaringan nyata tanpa **izin tertulis eksplisit**.
Penggunaan tanpa izin dapat melanggar CFAA, GDPR, atau hukum lainnya.
