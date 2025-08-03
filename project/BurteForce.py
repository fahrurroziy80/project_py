import string
import itertools

def brute_force(target_password):
    characters = string.ascii_lowercase  #
    attempts = 0

    for password_length in range(1, len(target_password)+1):
        for guess in itertools.product(characters, repeat=password_length):
            attempts += 1
            guess_password = ''.join(guess)
            print(f"Mencoba: {guess_password}")
            if guess_password == target_password:
                print(f"\n✅ Password ditemukan: {guess_password}")
                print(f"Total percobaan: {attempts}")
                return

# Main Program
target = input("Masukkan password yang akan di-brute-force (huruf kecil saja): ")
brute_force(target)
