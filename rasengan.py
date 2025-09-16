from colorama import Fore, Style, init
from time import sleep
from os import system
from sms import SendSms
import threading
import itertools

init(autoreset=True)

def loading_animation(text, duration=2):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = sleep_time = duration
    start = 0
    while start < end_time:
        print(f"\r{text} {next(spinner)}", end="", flush=True)
        sleep(0.1)
        start += 0.1
    print("\r" + " " * (len(text)+2), end="\r")

def ascii_intro():
    frames = [
        f"""{Fore.CYAN}
     ____                       _       
    |  _ \ ___ _ __   ___  _ __| |_ ___ 
    | |_) / _ \ '_ \ / _ \| '__| __/ __|
    |  _ <  __/ | | | (_) | |  | |_\__ \\
    |_| \_\___|_| |_|\___/|_|   \__|___/
                                        
        {Style.BRIGHT}by ras3ng4n@tingirifistik
        """,
        f"""{Fore.LIGHTMAGENTA_EX}
     ____                       _       
    |  _ \ ___ _ __   ___  _ __| |_ ___ 
    | |_) / _ \ '_ \ / _ \| '__| __/ __|
    |  _ <  __/ | | | (_) | |  | |_\__ \\
    |_| \_\___|_| |_|\___/|_|   \__|___/
                                        
        {Style.BRIGHT}by ras3ng4n@tingirifistik
        """
    ]
    for _ in range(3):
        for frame in frames:
            system("cls||clear")
            print(frame)
            sleep(0.5)

# SMS servislerini listele
servisler_sms = [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith('__')]

ascii_intro()

while True:
    system("cls||clear")
    print(f"""{Fore.CYAN}
     ____                       _       
    |  _ \ ___ _ __   ___  _ __| |_ ___ 
    | |_) / _ \ '_ \ / _ \| '__| __/ __|
    |  _ <  __/ | | | (_) | |  | |_\__ \\
    |_| \_\___|_| |_|\___/|_|   \__|___/
                                        
    SMS Servisleri: {len(servisler_sms)}       {Style.BRIGHT}by ras3ng4n@tingirifistik
    """)

    try:
        menu = input(f"{Fore.MAGENTA} 1- SMS Gönder (Normal)\n 2- SMS Gönder (Turbo)\n 3- Çıkış\n\n{Fore.YELLOW} Seçim: ")
        if not menu:
            continue
        menu = int(menu)
    except ValueError:
        print(Fore.RED + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(2)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.YELLOW + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.GREEN, end="")
        tel_no = input()
        tel_liste = [tel_no]

        system("cls||clear")
        print(Fore.YELLOW + "Kaç adet SMS göndermek istiyorsunuz?: " + Fore.GREEN, end="")
        try:
            kere = int(input())
        except ValueError:
            print(Fore.RED + "Hatalı giriş.")
            sleep(2)
            continue

        system("cls||clear")
        print(Fore.YELLOW + "SMSler arası saniye: " + Fore.GREEN, end="")
        try:
            aralik = float(input())
        except ValueError:
            print(Fore.RED + "Hatalı giriş.")
            sleep(2)
            continue

        system("cls||clear")
        # Normal SMS gönderimi
        for i in tel_liste:
            sms = SendSms(i, "")
            while sms.adet < kere:
                for fonk in servisler_sms:
                    if sms.adet >= kere:
                        break
                    getattr(sms, fonk)()
                    print(Fore.LIGHTGREEN_EX + f"{sms.adet}/{kere} SMS gönderildi.", end="\r")
                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 2:
        # Turbo modu
        system("cls||clear")
        print(Fore.YELLOW + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.GREEN, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            print(Fore.RED + "Hatalı telefon numarası.")
            sleep(2)
            continue

        send_sms = SendSms(tel_no, "")
        dur = threading.Event()

        def Turbo():
            while not dur.is_set():
                threads = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    threads.append(t)
                    t.start()
                for t in threads:
                    t.join()
                print(Fore.LIGHTGREEN_EX + f"{send_sms.adet} SMS gönderildi (Turbo mod).", end="\r")

        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)

    elif menu == 3:
        system("cls||clear")
        print(Fore.RED + "Çıkış yapılıyor...")
        break
