import string
import random

def generate_password(length):
    if length < 6:
        print("⚠️ Panjang password terlalu pendek. Minimal 6 karakter.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def simpan_ke_file(password):
    with open("generated_passwords.txt", "a") as file:
        file.write(password + "\n")
    print("✅ Password berhasil disimpan ke 'generated_passwords.txt'.")


try:
    panjang = int(input("Masukkan panjang password yang diinginkan: "))
    password = generate_password(panjang)
    if password:
        print(f"🔐 Password kamu: {password}")
        simpan = input("Ingin simpan ke file? (y/n): ").lower()
        if simpan == 'y':
            simpan_ke_file(password)
except ValueError:
    print("❌ Masukkan angka untuk panjang password!")
