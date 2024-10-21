# cryptizia.py

import string
from time import sleep
from termcolor import colored

class CaesarCipherExample:
    def __init__(self, shift=3, plaintext="HELLO", output_file="caesar_cipher_output.txt"):
        self.shift = shift
        self.alphabet = string.ascii_uppercase
        self.output_file = output_file
        # Clear file contents before writing new output
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write("")

        # Automatically show example on instantiation
        self.show_animation(plaintext, mode="encrypt")
        self.show_animation("KHOOR", mode="decrypt")  # Decrypting the result of encryption

    def save_to_file(self, text):
        with open(self.output_file, "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def display_intro(self):
        intro_text = f"""
        === Introduction to Caesar Cipher ===
        
        The Caesar Cipher is one of the simplest and most widely known encryption techniques. 
        It is a type of substitution cipher where each letter in the plaintext is 'shifted' 
        by a certain number of positions down the alphabet.
        
        The mathematical formula for encryption is:
        E(x) = (x + n) % 26
        
        Where:
        - E(x) is the encrypted letter.
        - x is the position of the letter in the alphabet (starting from 0 for 'A').
        - n is the shift value (the number of positions to shift).

        The decryption formula is:
        D(x) = (x - n) % 26
        
        Let's explore how this works with an example using a shift value of {self.shift}.
        """
        
        # Display the introduction
        for line in intro_text.splitlines():
            self.save_to_file(line.strip())
            print(colored(line.strip(), "cyan", attrs=["bold"]))
            sleep(0.3)

    def encrypt(self, plaintext):
        self.save_to_file("\n=== Caesar Cipher Encryption ===\n")
        print(colored("\n=== Caesar Cipher Encryption ===\n", "green", attrs=["bold"]))
        ciphertext = ''
        for char in plaintext.upper():
            if char in self.alphabet:
                idx = self.alphabet.index(char)
                new_idx = (idx + self.shift) % 26
                encrypted_char = self.alphabet[new_idx]
                
                # Display Mathematical Explanation
                self.save_to_file(f"Encrypting {char}:")
                self.save_to_file(f"  - Current Position (Index of {char}): {idx}")
                self.save_to_file(f"  - Shift by {self.shift}: ({idx} + {self.shift}) % 26 = {new_idx}")
                self.save_to_file(f"  - Encrypted Character: {char} → {encrypted_char}")
                
                print(colored(f"Encrypting {char}:", "yellow", attrs=["bold"]))
                print(f"  - Current Position (Index of {char}): {idx}")
                print(f"  - Shift by {self.shift}: ({idx} + {self.shift}) % 26 = {new_idx}")
                print(f"  - Encrypted Character: {char} → {encrypted_char}")
                sleep(0.5)  # Pause for effect
                
                ciphertext += encrypted_char
            else:
                ciphertext += char
        
        self.save_to_file(f"\nFinal Encrypted Text: {ciphertext}\n")
        print(colored(f"\nFinal Encrypted Text: {ciphertext}\n", "cyan", attrs=["bold"]))
        return ciphertext

    def decrypt(self, ciphertext):
        self.save_to_file("\n=== Caesar Cipher Decryption ===\n")
        print(colored("\n=== Caesar Cipher Decryption ===\n", "blue", attrs=["bold"]))
        plaintext = ''
        for char in ciphertext.upper():
            if char in self.alphabet:
                idx = self.alphabet.index(char)
                new_idx = (idx - self.shift) % 26
                decrypted_char = self.alphabet[new_idx]
                
                # Display Mathematical Explanation
                self.save_to_file(f"Decrypting {char}:")
                self.save_to_file(f"  - Current Position (Index of {char}): {idx}")
                self.save_to_file(f"  - Shift by {self.shift}: ({idx} - {self.shift}) % 26 = {new_idx}")
                self.save_to_file(f"  - Decrypted Character: {char} → {decrypted_char}")
                
                print(colored(f"Decrypting {char}:", "magenta", attrs=["bold"]))
                print(f"  - Current Position (Index of {char}): {idx}")
                print(f"  - Shift by {self.shift}: ({idx} - {self.shift}) % 26 = {new_idx}")
                print(f"  - Decrypted Character: {char} → {decrypted_char}")
                sleep(0.5)  # Pause for effect
                
                plaintext += decrypted_char
            else:
                plaintext += char
        
        self.save_to_file(f"\nFinal Decrypted Text: {plaintext}\n")
        print(colored(f"\nFinal Decrypted Text: {plaintext}\n", "cyan", attrs=["bold"]))
        return plaintext

    def show_animation(self, text, mode="encrypt"):
        self.save_to_file("\nProcessing...\n")
        print(colored("\nProcessing...\n", "blue", attrs=["bold"]))
        sleep(1)
        self.save_to_file(f"\nOriginal Text: {text}\n")
        print(colored(f"\nOriginal Text: {text}\n", "yellow", attrs=["bold", "underline"]))
        sleep(0.5)

        if mode == "encrypt":
            # Display introduction to the Caesar Cipher before starting
            self.display_intro()
            result = self.encrypt(text)
        else:
            result = self.decrypt(text)

        self.save_to_file(f"\nResult: {result}\n")
        print(colored(f"\nResult: {result}\n", "green", attrs=["bold", "underline"]))
        sleep(1)
        self.save_to_file("=== Process Completed ===\n")
        print(colored("=== Process Completed ===\n", "cyan", attrs=["bold"]))

# Example Usage
if __name__ == "__main__":
    # Automatically show example when creating an instance
    cipher = CaesarCipherExample()
