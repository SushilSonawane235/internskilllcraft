def caesar_cipher(message, shift, action):
    result = ''
    
    if action == 'decrypt':
        shift = -shift  # Reverse the shift for decryption

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Keep spaces, punctuation, numbers unchanged
    return result


def main():
    print("🔐 Welcome to the Caesar Cipher Tool!")
    print("You can encrypt or decrypt any message by shifting letters.\n")

    while True:
        action = input("What would you like to do? (encrypt / decrypt / exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye! 👋")
            break
        elif action not in ['encrypt', 'decrypt']:
            print("Oops! Please type 'encrypt', 'decrypt', or 'exit'.\n")
            continue

        message = input("Enter your message: ").strip()
        try:
            shift = int(input("How many letters should we shift by? (e.g., 3): "))
        except ValueError:
            print("That doesn’t seem like a valid number. Try again!\n")
            continue

        result = caesar_cipher(message, shift, action)
        print(f"\n✅ Here's your {action}ed message:\n{result}\n")

if __name__ == "__main__":
    main()
