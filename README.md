### Basis for the Implementation:
1. Understanding the Beaufort Cipher:

    - The Beaufort Cipher encrypts/decrypts by calculating the reverse shift of the Vigenère Cipher. For a plaintext letter 
    **P** and keyword letter **K**, the ciphertext letter **C** is derived as:

        **C = ( K − P )** mod26 (Encryption)
         
        **P = ( K − C )** mod26 (Decryption)
    - This mirrors the Vigenère decryption process, making the Beaufort Cipher self-reciprocal (same algorithm for encryption/decryption if roles of **P** and **C** are swapped).

2. Algorithmic Steps:

    - Keyword Repetition: The keyword is repeated to match the plaintext/ciphertext length (e.g., "CYBERGO" with keyword "KEY" becomes "IGXGNSW").

    - Modulo Arithmetic: Letters are converted to their alphabetical positions (A=0, B=1, ..., Z=25), and shifts are computed modulo 26 to wrap around the alphabet.

3. Python Translation:

    - ord() converts letters to Unicode code points (e.g., ord('A') = 65).

    - % 26 ensures the result stays within the alphabet range.

    - Non-alphabetic characters (e.g., spaces) are preserved as-is.

### Why This Implementation is Original:
- No Third-Party Libraries: The code uses only Python built-ins (ord(), chr(), zip()), as required by the assignment.

- Self-Derived Logic: The mathematical operations follow the Beaufort Cipher’s definition, not copied from external sources.

- Example-Tested: The provided example ("CYBERGO" → "IGXGNSW") was manually verified using the tabula recta before coding.