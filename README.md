# Caesar Cipher (Day 8)

A simple interactive Caesar cipher script from the "100 Days of Code" exercises.

Features
- Single `caesar` function that handles both encoding and decoding.
- Preserves letter case and leaves non-letter characters unchanged.
- Normalizes shift via modulo 26 (large shifts work as expected).
- Prints the progressively-built output after each character so you can observe the transformation.
- Runs in a loop so you can process multiple messages without restarting.

Prerequisites
- Python 3.x

Run

```bash
python "Day 8 of 100 - Caesar cipher.py"
```

Usage
1. Enter the message you want to encrypt/decrypt.
2. Enter the shift number (integer).
3. Choose `encode` (or `encrypt`) to shift forward, or `decode` (or `decrypt`) to shift backward.
4. The script will print the intermediate result after each character and the final transformed text.
5. Type `yes` when asked if you want to go again to run another operation.

Notes
- Uppercase and lowercase letters are shifted preserving case.
- Punctuation, numbers, and whitespace are left unchanged.
- Large shift values are reduced using modulo 26 (e.g., shift 27 == shift 1).

File
- The main script is `Day 8 of 100 - Caesar cipher.py` in this folder.

License
- No license specified — use for learning and experimentation.

## Skills Learned

- Understanding and implementing the Caesar cipher algorithm.
- Working with character codes using `ord()` and `chr()` to map letters to numeric positions.
- Using modulo arithmetic to wrap shifts within the 26-letter alphabet.
- Preserving letter case and leaving non-letter characters unchanged.
- Validating and handling user input (integers and choices).
- Organizing code into functions and using docstrings for clarity.
- Building a simple interactive CLI loop for repeated use.
- Printing intermediate results to observe step-by-step transformations.
