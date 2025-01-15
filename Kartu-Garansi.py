import os
import time
import re
from datetime import datetime

# Clear screen function
def clear_screen():
    os.system("clear")

# Print the logo with advanced design
def print_logo():
    logo = """
██████╗ ███████╗ █████╗ ██████╗ ████████╗ █████╗ ██╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║   ██║
██████╔╝█████╗  ███████║██║  ██║   ██║   ███████║██║   ██║
██╔═══╝ ██╔══╝  ██╔══██║██║  ██║   ██║   ██╔══██║██║   ██║
██║     ███████╗██║  ██║██████╔╝   ██║   ██║  ██║╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
---------------------------------------------------------
           ██████╗  █████╗ ██████╗ ██╗████████╗
          ██╔═══██╗██╔══██╗██╔══██╗██║╚══██╔══╝
          ██║   ██║███████║██████╔╝██║   ██║
          ██║   ██║██╔══██║██╔══██╗██║   ██║
          ╚██████╔╝██║  ██║██████╔╝██║   ██║
           ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝
           KARTU GARANSI SEUMUR HIDUP
---------------------------------------------------------
AUTHOR  : ANDHIKA ANGGA KURNIAWAN
KELAS   : RPL 2
TOOLS   : ONLINE
---------------------------------------------------------
"""
    print("\033[1;36m" + logo + "\033[0m")

# Greet user based on the time of day with emojis
def greet_user():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        print("\033[1;32m🌞 Selamat Pagi! 🌞\033[0m")
    elif 12 <= current_hour < 18:
        print("\033[1;33m🌞 Selamat Siang! 🌞\033[0m")
    elif 18 <= current_hour < 22:
        print("\033[1;34m🌆 Selamat Sore! 🌆\033[0m")
    else:
        print("\033[1;31m🌙 Selamat Malam! 🌙\033[0m")

# Typing animation effect
def typing_effect(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zAZ0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Validate phone number format (12 digits)
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 12

# Main function
def main():
    clear_screen()
    print_logo()
    greet_user()

    # Start interactive process
    typing_effect("\033[5;41;37m🛠️ KARTU GARANSI 🛠️\033[0m\n", 0.2)
    print("\033[1;32m📝 Silakan masukkan informasi untuk melanjutkan...\033[0m")

    # Gathering User Information
    nama_depan = input("💡 Masukkan nama depan Anda: ")
    nama_belakang = input("💡 Masukkan nama belakang Anda: ")
    jenis_kelamin = input("💡 Masukkan jenis kelamin Anda (girl/boy): ").lower()

    while jenis_kelamin not in ['girl', 'boy']:
        jenis_kelamin = input("❌ Input tidak valid, masukkan jenis kelamin yang benar (girl/boy): ").lower()

    tanggal_lahir = input("💡 Masukkan tanggal lahir Anda (YYYY-MM-DD): ")

    # Validate KTP status
    no_ktp = input("🔑 Apakah Anda memiliki KTP? (Ya/Tidak): ").lower()
    while no_ktp not in ['ya', 'tidak']:
        no_ktp = input("❌ Input tidak valid, masukkan 'Ya' atau 'Tidak': ").lower()

    if no_ktp == "Ya":
        typing_effect("📜 Silakan masukkan paspor Anda.", 0.1)
    elif no_ktp == "Tidak":
        typing_effect("🔒 Mungkin Anda sangat privasi.", 0.1)

    alamat = input("🏠 Masukkan alamat Anda: ")

    # Validate email
    email = input("📧 Masukkan email Anda: ")
    while not is_valid_email(email):
        email = input("❌ Email tidak valid, silakan masukkan email yang benar: ")

    # Validate phone number
    telepon = input("📱 Masukkan nomor telepon (12 digit): ")
    while not is_valid_phone(telepon):
        telepon = input("❌ Nomor telepon tidak valid, masukkan nomor telepon 12 digit yang benar: ")

    merek_hp = input("📱 Masukkan nama merek HP Anda: ")

    # Confirmation and displaying collected data
    typing_effect("\n🟢 Terima kasih telah mengisi data garansi! 🟢", 0.2)
    typing_effect("🔍 Informasi yang telah dimasukkan:", 0.2)
    typing_effect(f"🔑 Nama: {nama_depan} {nama_belakang}", 0.1)
    typing_effect(f"🧑‍🤝‍🧑 Jenis Kelamin: {jenis_kelamin}", 0.1)
    typing_effect(f"🎂 Tanggal Lahir: {tanggal_lahir}", 0.1)
    typing_effect(f"🆔 KTP: {'Ada' if no_ktp == 'ya' else 'Tidak ada'}", 0.1)
    typing_effect(f"🏠 Alamat: {alamat}", 0.1)
    typing_effect(f"📧 Email: {email}", 0.1)
    typing_effect(f"📱 Telepon: {telepon}", 0.1)
    typing_effect(f"📱 Merek HP: {merek_hp}", 0.1)

    # Final message with animation
    time.sleep(1)
    clear_screen()
    print_logo()
    typing_effect("\033[1;32m✅ Data telah berhasil disimpan! Terima kasih! ✅\033[0m", 0.1)

if __name__ == "__main__":
    main()
