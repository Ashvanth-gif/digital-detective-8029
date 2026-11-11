# Mission 5 - Numbers and Data

## 1. Task / objective
I practised converting numbers between decimal, binary, and hexadecimal, checked the answers with Python, and ran a small number converter.

## 2. Work completed

### Manual conversions

| Question | Working | Answer |
|---|---|---|
| Decimal 13 to binary | 13 = 8 + 4 + 1 | `1101` |
| Decimal 25 to binary | 25 = 16 + 8 + 1 | `11001` |
| Binary `1010` to decimal | 1×8 + 0×4 + 1×2 + 0×1 | `10` |
| Binary `1101` to decimal | 1×8 + 1×4 + 0×2 + 1×1 | `13` |
| Hexadecimal `A` to decimal | A represents 10 | `10` |
| Hexadecimal `1F` to decimal | 1×16 + 15 | `31` |
| Binary `1111` to hexadecimal | `1111` is 15 in decimal; 15 is F in hexadecimal | `F` |

### Python checks
I entered these expressions in Python and compared each result with my working.

| Expression | Result | Match? |
|---|---|---|
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(10)` | `'0xa'` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))[2:].upper()` | `'F'` | Yes |

### Number converter
I ran `number_converter.py` with three positive values.

| Input | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | `1101` | `D` |
| 25 | `11001` | `19` |
| 42 | `101010` | `2A` |

The program uses `input()` to read what I type and `int()` to turn it into a whole number. `bin()` converts it to binary, and `hex()` converts it to hexadecimal. The program removes the `0b` or `0x` prefix from the display; it also makes the hexadecimal letters uppercase.

### Text encoding
- Uppercase `A` has ASCII decimal code `65`.
- Lowercase `a` has ASCII decimal code `97`.
- A computer needs an encoding standard to store characters as numbers and read them consistently. The rupee sign (`₹`) is an example of a character that is not part of basic ASCII; UTF-8 can represent it.

## 3. Commands / tools used
- `python3` - opened the Python interactive environment for the conversion checks.
- `python3 number_converter.py` - ran the converter from this folder.
- `printf '13\n' | python3 number_converter.py` (and the same command with `25` and `42`) - supplied the three test values from Terminal.

## 4. My understanding
Decimal uses ten digits, binary uses two, and hexadecimal uses sixteen. Each position has a different place value. Python's conversion functions helped me check the answers, and the converter uses those functions to display the binary and hexadecimal forms of a decimal number.

## 5. Difficulties faced
I found it tricky at first to keep track of the place values when converting a number by hand.

## 6. How I resolved them
I wrote the value of each place above the digits, added the places marked with `1`, and checked the result in Python. I then used three different inputs to check the converter's output.

## 7. Evidence / files
- [`number_converter.py`](number_converter.py) - the working converter.
- [`../evidence/mission-05-python-checks.txt`](../evidence/mission-05-python-checks.txt) - privacy-safe Python check and converter results.

## 8. Commit details
Commit message: `Complete Mission 5 conversions and converter examples`
Status: Committed and pushed.
