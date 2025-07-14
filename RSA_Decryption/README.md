# RSA Decryption with Modular Exponentiation

## Description

Use **public key** `(n, e)` and a **cipher-text** `(c)` to break RSA cryptography and recover the original **message** `(m)`.

Each test case consists of one line with:
- Two integers: `n`, `e`
- A string of encrypted ASCII values `c`, separated by commas `,`

For each encrypted value in `c`, compute the original ASCII code as:

m = c^e mod n  


Convert each result back to a character and concatenate to form the decrypted message.

**Important:**  
You must implement your own modular exponentiation function (i.e., `c^e mod n`) without using built-in `pow()`.

---

## Constraints

- `6 ≤ n ≤ 10^18`
- `1 ≤ e ≤ 10^8`

---

## Input Format

- `n`: RSA modulus
- `e`: RSA public exponent
- `c`: A comma-separated string of encrypted integers

---

## Output Format
m  

- A single line string — the decrypted original message.

---

## Example

### Sample Case 1

**Input:**
221 5 89,99  

**Output:**
HI  

---

### Sample Case 2

**Input:**
12902023 4723267 2967605,9078654,5068419,5068419,406642,1905121,10620281,406642,9727012,5068419,10073213  

**Output:**
hello world  

---

## Summary Table

| Input                                                                                                              | Output       |
|-------------------------------------------------------------------------------------------------------------------|--------------|
| `221 5 89,99`                                                                                                     | `HI`         |
| `12902023 4723267 2967605,9078654,5068419,5068419,406642,1905121,10620281,406642,9727012,5068419,10073213`        | `hello world` |

---

## Hint

To decode each number, use **modular exponentiation** (exponentiation by squaring)

