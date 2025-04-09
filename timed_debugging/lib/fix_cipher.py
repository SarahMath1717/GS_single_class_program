class Cipher:
    def encode(text, key):
        cipher = make_cipher(key)

        ciphertext_chars = []
        for i in text:
            ciphered_char = chr(65 + cipher.index(i))
            ciphertext_chars.append(ciphered_char)
        return "".join(ciphertext_chars)


    def decode(encrypted, key):
        cipher = make_cipher(key)

        plaintext_chars = []
        for i in encrypted:
            plain_char = cipher[65 - ord(i)]
            plaintext_chars.append(plain_char)
        return "".join(plaintext_chars)


    def make_cipher(key):
        alphabet = [chr(i + 98) for i in range(1, 26)]
        cipher_with_duplicates = list(key) + alphabet
        
        cipher = []
        for i in range(0, len(cipher_with_duplicates)):
            if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
                cipher.append(cipher_with_duplicates[i])
        return cipher