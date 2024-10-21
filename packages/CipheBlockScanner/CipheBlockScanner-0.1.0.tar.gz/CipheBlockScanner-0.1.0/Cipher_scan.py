import base64
from collections import Counter

def analyze_ciphertext(ciphertext):
    # Decode the base64-encoded ciphertext
    decoded_ciphertext = base64.b64decode(ciphertext)

    # Convert to hexadecimal
    hex_representation = decoded_ciphertext.hex()

    # Count the frequency of each hex character
    hex_frequency = Counter(hex_representation)

    # Display the frequency analysis
    for char, freq in hex_frequency.items():
        print(f"Character: {char}, Frequency: {freq}")

# Example ciphertexts
ciphertexts = [
    'your_base64_encoded_ciphertext_here1',
    'your_base64_encoded_ciphertext_here2'
]

for ciphertext in ciphertexts:
    print(f"Analyzing ciphertext: {ciphertext}")
    analyze_ciphertext(ciphertext)
    print("\n")
