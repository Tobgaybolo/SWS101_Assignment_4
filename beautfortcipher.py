def beaufort_encrypt(plaintext, keyword):
    ciphertext = []
    keyword_repeated = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]
    for p, k in zip(plaintext.upper(), keyword_repeated.upper()):
        if p.isalpha():
            shift = (ord(k) - ord(p)) % 26
            ciphertext.append(chr(shift + ord('A')))
        else:
            ciphertext.append(p)
    return ''.join(ciphertext)

def beaufort_decrypt(ciphertext, keyword):
    plaintext = []
    keyword_repeated = (keyword * ((len(ciphertext) // len(keyword)) + 1))[:len(ciphertext)]
    for c, k in zip(ciphertext.upper(), keyword_repeated.upper()):
        if c.isalpha():
            shift = (ord(k) - ord(c)) % 26
            plaintext.append(chr(shift + ord('A')))
        else:
            plaintext.append(c)
    return ''.join(plaintext)

# Example Usage
plaintext = "CYBERGO"
keyword = "KEY"
encrypted = beaufort_encrypt(plaintext, keyword)
decrypted = beaufort_decrypt(encrypted, keyword)
print(f"Encrypted: {encrypted}")  # Output: IGXGNSW
print(f"Decrypted: {decrypted}")  # Output: CYBERGO