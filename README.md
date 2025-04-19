# 🔐 File Encryption & Decryption Tool (Python + Cryptography)

This is a real-world Python tool to **securely encrypt and decrypt files** using a secret key and the `cryptography` library.

Built for practical use — encrypt sensitive files, choose to delete originals, and decrypt them only when needed. Files are managed into separate folders for safety.

---

## 📦 Project Structure

```
project-root/
├── main.py
├── utils.py
├── secret.key                # Secret key used for encryption/decryption
├── encrypted_files/          # Encrypted output files
└── decrypted_files/          # Decrypted output files
```

---

## ✅ Features

- AES-based strong encryption using `cryptography.Fernet`
- Encrypt/decrypt **any text-based file**
- Auto-handles output naming and folders
- Option to delete the **original file** after encryption
- Loops until you choose to quit

---

## 💻 Requirements

- Python 3.7+
- `cryptography` library

### 📥 Install dependencies

```bash
pip install cryptography
```

---

## 🚀 How to Run

```bash
python main.py
```

---

### 🧪 Example Usage

To **encrypt** a file:

```bash
Do you want to (e)ncrypt, (d)ecrypt a file, or (q)uit? (e/d/q): e
🔑 Using existing secret.key
Enter the full file path to encrypt: /Users/nirmalrajgor/Desktop/sample.txt
Delete original file after encryption? (y/n): y
✅ File encrypted and saved as: encrypted_files/sample_encrypted.txt
🗑️ Original file deleted after encryption.
```

To **decrypt** a file:

```bash
Do you want to (e)ncrypt, (d)ecrypt a file, or (q)uit? (e/d/q): d
Enter the full file path to decrypt: encrypted_files/sample_encrypted.txt
✅ File decrypted and saved as: decrypted_files/sample_decrypted.txt
```

To **quit**:

```bash
Do you want to (e)ncrypt, (d)ecrypt a file, or (q)uit? (e/d/q): q
👋 Goodbye!
```

---

## 🔐 Security Note

- The secret key is stored in `secret.key`. Keep it safe!  
- Anyone with this key can decrypt your files.

---

## 📌 Tip

To encrypt a file on your Desktop:

```bash
/Users/your-username/Desktop/yourfile.txt
```

Or use `~` for shorthand in terminal inputs:
```bash
~/Desktop/yourfile.txt
```

---

## 🛠 Future Enhancements (Ideas)

- Password protection for the key
- Encrypt whole folders
- Drag & drop GUI (Tkinter)
- Support for non-text files (images, PDFs)

---

## 👨‍💻 Author

Made with ❤️ by Nirmal Rajgor  
[GitHub Profile](https://github.com/Nirmal2509)