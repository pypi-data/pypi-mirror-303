class CaesarCipher:
    def __init__(self):
        pass

    # Caesar cipher encryption function
    def caesar_encrypt(self, plaintext, shift):
        encrypted = ""  # Initializes an empty string to store the resulting encrypted message.
        
        # Iterates over each character in the plaintext.
        for char in plaintext:
            # Checks if the character is a letter (either uppercase or lowercase).
            if char.isalpha():
                # Determines the base ASCII value for the letter shift.
                shift_base = 65 if char.isupper() else 97  # For uppercase (A-Z) and lowercase (a-z)
                
                # Convert letter to ASCII, apply the shift, wrap around using modulo 26, and convert back to char
                ascii_value = ord(char) - shift_base
                shifted_value = (ascii_value + shift) % 26
                new_ascii_value = shifted_value + shift_base
                new_char = chr(new_ascii_value)

                # Add the encrypted character to the result string
                encrypted += new_char
            else:
                # Non-alphabetical characters remain unchanged
                encrypted += char

        return encrypted

    # Caesar cipher decryption function
    def caesar_decrypt(self, ciphertext, shift):
        # Decrypt by using caesar_encrypt with the negative shift value.
        return self.caesar_encrypt(ciphertext, -shift)