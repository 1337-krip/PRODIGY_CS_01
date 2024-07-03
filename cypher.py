def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        result = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
