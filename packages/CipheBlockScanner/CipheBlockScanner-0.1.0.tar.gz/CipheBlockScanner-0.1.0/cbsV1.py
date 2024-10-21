import base64
from collections import Counter
import argparse

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

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Analyze base64-encoded ciphertext")
    parser.add_argument("ciphertext", help="The base64-encoded ciphertext to analyze")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Analyze the provided ciphertext
    print(f"Analyzing ciphertext: {args.ciphertext}")
    analyze_ciphertext(args.ciphertext)
    print("\n")

if __name__ == "__main__":
    main()
