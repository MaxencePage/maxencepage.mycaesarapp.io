import string   # Import modul string untuk mengakses huruf alfabet

def caesar_encrypt(data,key):
    
    """Mengenkripsi teks menggunakan metode Caesar Cipher.

  Args:
    data: Teks yang akan dienkripsi.
    key: Kunci enkripsi (jumlah pergeseran huruf).

  Returns:
    Teks yang telah dienkripsi.
  """
    
    res = ""                                                    # Membuat string kosong untuk menyimpan teks terenkripsi
    for x in range(len(data)):                                  # Mengulangi proses untuk setiap huruf dalam teks
        if data[x].isupper():                                   # Jika huruf adalah huruf besar
            pos = string.ascii_uppercase.index(data[x]) + key   # Cari posisi huruf dalam alfabet dan tambahkan kunci
            pos = pos % 26                                      # Pastikan posisi tetap dalam rentang alfabet (0-25)
            res += string.ascii_uppercase[pos]                  # Tambahkan huruf terenkripsi ke string hasil
        elif data[x].islower():                                 # Jika huruf adalah huruf kecil
            pos = string.ascii_lowercase.index(data[x]) + key   # Lakukan hal yang sama untuk huruf kecil
            pos = pos % 26
            res += string.ascii_lowercase[pos]
        else:                                                   # Jika bukan huruf, biarkan tanpa perubahan
            res += data[x]
    return res                                                  # Kembalikan teks terenkripsi

def caesar_decrypt(data,key):
    res = ""
    for x in range(len(data)):
        if data[x].isupper():
            pos = string.ascii_uppercase.index(data[x]) - key
            pos = pos % 26
            res += string.ascii_uppercase[pos]
        elif data[x].islower():
            pos = string.ascii_lowercase.index(data[x]) - key
            pos = pos % 26
            res += string.ascii_lowercase[pos]
        else:
            res += data[x]
    return res  

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")

    if choice.lower() == 'e':
        text = input("Enter the text to encrypt: ")
        key = int(input("Enter the encryption key: "))
        enc = caesar_encrypt(text, key)
        print("Encrypted text: ", enc)
    elif choice.lower() == 'd':
        text = input("Enter the text to decrypt: ")
        key = int(input("Enter the decryption key: "))
        dec = caesar_decrypt(text, key)
        print("Decrypted text: ", dec)
    else:
        print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
