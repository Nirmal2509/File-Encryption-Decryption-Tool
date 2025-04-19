from utils import generate_key, load_key, encrypt_file, decrypt_file
import os

def main():
    print("🔐 Welcome to the File Encryption/Decryption Tool")

    while True:
        choice = input("Do you want to (e)ncrypt, (d)ecrypt a file, or (q)uit? (e/d/q): ").lower()

        if choice == 'e':
            if not os.path.exists("secret.key"):
                generate_key()
                print("✔️ Key generated and saved to secret.key")
            else:
                print("🔑 Using existing secret.key")

            file_path = input("Enter the full file path to encrypt: ")
            file_path = os.path.expanduser(file_path)

            delete_original = input("Delete original file after encryption? (y/n): ").lower() == 'y'

            encrypt_file(file_path, delete_original)

        elif choice == 'd':
            if not os.path.exists("secret.key"):
                print("❌ secret.key file not found. Cannot decrypt.")
                continue

            file_path = input("Enter the full file path to decrypt: ")
            file_path = os.path.expanduser(file_path)

            decrypt_file(file_path)

        elif choice == 'q':
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 'e', 'd', or 'q'.")

        print("\n")  # Add spacing before rerunning

if __name__ == "__main__":
    main()
