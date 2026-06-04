def encrypt(text, shift=3):
    result = ""

    for char in text:
        result += chr(ord(char) + shift)

    return result


def decrypt(text, shift=3):
    result = ""

    for char in text:
        result += chr(ord(char) - shift)

    return result


with open("secret.txt", "r", encoding="utf-8") as file:
    text = file.read()

encrypted_text = encrypt(text)

with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(encrypted_text)

with open("encrypted.txt", "r", encoding="utf-8") as file:
    encrypted_text = file.read()

decrypted_text = decrypt(encrypted_text)

with open("decrypted.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_text)

print("Шифрование и расшифровка завершены.")
