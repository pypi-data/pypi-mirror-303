# cryptizia.py

import string
from time import sleep
from termcolor import colored

class PlayfairCipherExample:
    def __init__(self, key="PLAYFAIR", plaintext="HELLO", output_file="playfair_cipher_output.txt"):
        self.key = self.prepare_key(key)
        self.output_file = output_file
        # Clear file contents before writing new output
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write("")

        # Automatically show example on instantiation
        self.show_animation(plaintext, mode="encrypt")
        ciphertext = self.encrypt(plaintext)  # Encrypt the plaintext
        self.show_animation(ciphertext, mode="decrypt")  # Decrypt the result of encryption

    def save_to_file(self, text):
        with open(self.output_file, "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def prepare_key(self, key):
        # Remove duplicates and create a 5x5 matrix for the Playfair cipher
        key = key.upper().replace("J", "I")
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Keep order and remove duplicates
        key += ''.join([char for char in string.ascii_uppercase if char not in key])
        return [key[i:i + 5] for i in range(0, 25, 5)]  # 5x5 matrix

    def display_key_matrix(self):
        self.save_to_file("\n=== Playfair Cipher Key Matrix ===\n")
        print(colored("\n=== Playfair Cipher Key Matrix ===\n", "cyan", attrs=["bold"]))
        for row in self.key:
            row_str = ' '.join(row)
            self.save_to_file(row_str)
            print(colored(row_str, "yellow"))
            sleep(0.3)

    def display_intro(self):
        intro_text = f"""
        === Introduction to Playfair Cipher ===

        The Playfair Cipher is a manual symmetric encryption technique and is one of the 
        first digraph substitution ciphers. The encryption process uses a 5x5 matrix 
        of letters constructed using a keyword. The letters are combined in pairs, and 
        different rules apply based on their position in the matrix.
        
        === Rules for Playfair Cipher ===

        1. **Creating the Key Matrix**:
            - Choose a keyword (e.g., "PLAYFAIR") and remove any duplicate letters.
            - Replace the letter 'J' with 'I' (e.g., "JACK" becomes "IACK").
            - Fill a 5x5 matrix with the letters of the keyword first, followed by the remaining letters of the alphabet (excluding 'J').

        2. **Preparing the Plaintext**:
            - Convert all letters to uppercase and remove non-alphabet characters.
            - If a pair of letters in plaintext is identical (e.g., "LL"), insert an 'X' between them (e.g., "LL" becomes "LX").
            - If the plaintext has an odd number of characters, append an 'X' at the end (e.g., "HELLO" becomes "HELX LO").

        3. **Encrypting the Plaintext**:
            - Divide the formatted plaintext into pairs of letters.
            - For each pair, apply the following rules:
                a. **Same Row**: If both letters are in the same row of the matrix, replace them with the letters immediately to their right (wrap around to the beginning of the row if needed).
                b. **Same Column**: If both letters are in the same column, replace them with the letters immediately below (wrap around to the top if needed).
                c. **Rectangle**: If the letters form a rectangle in the matrix, replace them with the letters on the same row but at the opposite corners of the rectangle.

        4. **Decrypting the Ciphertext**:
            - Follow the same process as encryption but reverse the rules:
                a. For letters in the same row, replace them with the letters immediately to their left.
                b. For letters in the same column, replace them with the letters immediately above.
                c. For letters forming a rectangle, swap them as before.

        Let's explore how this works with the key '{self.key[0]}':
        """
        
        # Display the introduction
        for line in intro_text.splitlines():
            self.save_to_file(line.strip())
            print(colored(line.strip(), "cyan", attrs=["bold"]))
            sleep(0.3)

    def format_plaintext(self, plaintext):
        # Remove non-alpha characters and format plaintext
        plaintext = plaintext.upper().replace("J", "I")
        formatted = []
        i = 0
        while i < len(plaintext):
            a = plaintext[i]
            if i + 1 < len(plaintext):
                b = plaintext[i + 1]
                if a == b:
                    formatted.append(a + "X")  # Insert 'X' between identical letters
                    i += 1
                else:
                    formatted.append(a + b)
                    i += 2
            else:
                formatted.append(a + "X")  # Pad with 'X' if the last letter is alone
                i += 1
        return formatted

    def clean_decrypted_text(self, decrypted_text):
        # If the last character is 'X', check the previous character to decide if it should be removed
        if len(decrypted_text) > 0 and decrypted_text[-1] == 'X':
            # Check if 'X' is at the end after a valid pair
            if len(decrypted_text) > 1 and decrypted_text[-2] == decrypted_text[-3]:
                # Do not remove 'X' if it follows the rules (e.g., "LLX")
                return decrypted_text  # Return as is
            decrypted_text = decrypted_text[:-1]  # Remove the trailing 'X'
        return decrypted_text


    def find_position(self, letter):
        for r in range(5):
            for c in range(5):
                if self.key[r][c] == letter:
                    return r, c
        return None

    def encrypt(self, plaintext):
        self.save_to_file("\n=== Playfair Cipher Encryption ===\n")
        print(colored("\n=== Playfair Cipher Encryption ===\n", "green", attrs=["bold"]))
        self.display_key_matrix()  # Show the key matrix during encryption
        formatted_text = self.format_plaintext(plaintext)
        ciphertext = ""

        for pair in formatted_text:
            row1, col1 = self.find_position(pair[0])
            row2, col2 = self.find_position(pair[1])

            # Display Mathematical Explanation
            self.save_to_file(f"Encrypting Pair: {pair}")
            if row1 == row2:  # Same row
                ciphertext += self.key[row1][(col1 + 1) % 5] + self.key[row2][(col2 + 1) % 5]
                self.save_to_file(f"  - Same Row: {pair[0]}({row1},{col1}) and {pair[1]}({row2},{col2})")
                self.save_to_file(f"  - Encrypted as: {self.key[row1][(col1 + 1) % 5]}{self.key[row2][(col2 + 1) % 5]}")
            elif col1 == col2:  # Same column
                ciphertext += self.key[(row1 + 1) % 5][col1] + self.key[(row2 + 1) % 5][col2]
                self.save_to_file(f"  - Same Column: {pair[0]}({row1},{col1}) and {pair[1]}({row2},{col2})")
                self.save_to_file(f"  - Encrypted as: {self.key[(row1 + 1) % 5][col1]}{self.key[(row2 + 1) % 5][col2]}")
            else:  # Rectangle
                ciphertext += self.key[row1][col2] + self.key[row2][col1]
                self.save_to_file(f"  - Rectangle: {pair[0]}({row1},{col1}) and {pair[1]}({row2},{col2})")
                self.save_to_file(f"  - Encrypted as: {self.key[row1][col2]}{self.key[row2][col1]}")

        self.save_to_file(f"\nFinal Encrypted Text: {ciphertext}\n")
        print(colored(f"\nFinal Encrypted Text: {ciphertext}\n", "cyan", attrs=["bold"]))
        return ciphertext

    def decrypt(self, ciphertext):
        self.save_to_file("\n=== Playfair Cipher Decryption ===\n")
        print(colored("\n=== Playfair Cipher Decryption ===\n", "blue", attrs=["bold"]))
        self.display_key_matrix()  # Show the key matrix during decryption
        formatted_text = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]  # Pair the ciphertext
        plaintext = ""

        for pair in formatted_text:
            row1, col1 = self.find_position(pair[0])
            row2, col2 = self.find_position(pair[1])

            # Display Mathematical Explanation
            self.save_to_file(f"Decrypting Pair: {pair}")
            if row1 == row2:  # Same row
                plaintext += self.key[row1][(col1 - 1) % 5] + self.key[row2][(col2 - 1) % 5]
                self.save_to_file(f"  - Same Row: {pair[0]}({row1},{col1}) and {pair[1]}({row2},{col2})")
                self.save_to_file(f"  - Decrypted as: {self.key[row1][(col1 - 1) % 5]}{self.key[row2][(col2 - 1) % 5]}")
            elif col1 == col2:  # Same column
                plaintext += self.key[(row1 - 1) % 5][col1] + self.key[(row2 - 1) % 5][col2]
                self.save_to_file(f"  - Same Column: {pair[0]}({row1},{col1}) and {pair[1]}({row2},{col2})")
                self.save_to_file(f"  - Decrypted as: {self.key[(row1 - 1) % 5][col1]}{self.key[(row2 - 1) % 5][col2]}")
            else:  # Rectangle
                plaintext += self.key[row1][col2] + self.key[row2][col1]
                self.save_to_file(f"  - Rectangle: {pair[0]}({row1},{col1}) and {pair[1]}({row2},{col2})")
                self.save_to_file(f"  - Decrypted as: {self.key[row1][col2]}{self.key[row2][col1]}")

        plaintext = self.clean_decrypted_text(plaintext)  # Clean up the decrypted text
        self.save_to_file(f"\nFinal Decrypted Text: {plaintext}\n")
        print(colored(f"\nFinal Decrypted Text: {plaintext}\n", "cyan", attrs=["bold"]))
        return plaintext

    def show_animation(self, text, mode):
         # Show introduction at the start
        if mode == "encrypt":
            self.display_intro() 
            self.encrypt(text)
        elif mode == "decrypt":
            self.decrypt(text)

# Usage
if __name__ == "__main__":
    cipher = PlayfairCipherExample(key="PLAYFAIR", plaintext="HELLO")
