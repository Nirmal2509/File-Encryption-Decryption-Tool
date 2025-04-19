from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, delete_original=False):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        filename = os.path.basename(file_path)
        new_filename = f"{filename.split('.')[0]}_encrypted.txt"
        output_path = os.path.join("encrypted_files", new_filename)

        os.makedirs("encrypted_files", exist_ok=True)
        with open(output_path, "wb") as enc_file:
            enc_file.write(encrypted)

        if delete_original:
            os.remove(file_path)
            print("🗑️ Original file deleted after encryption.")

        print(f"✅ File encrypted and saved as: {output_path}")
    except FileNotFoundError:
        print(f"❌ Error: {file_path} not found.")
    except Exception as e:
        print(f"⚠️ Encryption error: {e}")

def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_path, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        filename = os.path.basename(file_path)
        new_filename = f"{filename.split('_encrypted')[0]}_decrypted.txt"
        output_path = os.path.join("decrypted_files", new_filename)

        os.makedirs("decrypted_files", exist_ok=True)
        with open(output_path, "wb") as dec_file:
            dec_file.write(decrypted)

        print(f"✅ File decrypted and saved as: {output_path}")
    except FileNotFoundError:
        print(f"❌ Error: {file_path} not found.")
    except Exception as e:
        print(f"⚠️ Decryption error: {e}")