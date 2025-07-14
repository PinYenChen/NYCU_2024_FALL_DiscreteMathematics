# RSA Cipher Encoding with Modular Exponentiation

## Description

Use **public key** `(n, e)` and a **message** `(m)` to compute the **ciphertext** `(c)`.

Each test case consists of one line containing two integers `n`, `e`, and a string `m`. For each character in the message:

1. Convert the character to its ASCII code `m`
2. Compute `c = m^e mod n` using modular exponentiation
3. Output the encrypted values joined by commas `,`

**Important:**  
You must implement your own modular exponentiation function  
(e.g., `m^e % n` without using built-in `pow(m, e, n)`).

---

## Constraints

- `6 ≤ n ≤ 10^18`
- `1 ≤ e ≤ 10^8`

---

## Input Format

- `n`: RSA modulus
- `e`: RSA exponent
- `m`: message string

---

## Output Format
c₁,c₂,c₃,...  


A single line of comma-separated integers — each is the encrypted result of applying `m^e mod n` on the ASCII value of each character in the message.

---

## Example

### Sample Case 1

**Input:**
3165580559 200003 RSA  


**Output:**

1228066620,812049935,265910748  


---

### Sample Case 2

**Input:**
2449500764025883 9800003 201812  


**Output:**

1041410691569662,1091330202595797,585214278497037,10728887627281599,585214278497037,1041410691569662  



---

## Summary Table

| Input                                      | Output                                                                                      |
|-------------------------------------------|---------------------------------------------------------------------------------------------|
| `3165580559 200003 RSA`                   | `1228066620,812049935,265910748`                                                           |
| `2449500764025883 9800003 201812`         | `1041410691569662,1091330202595797,585214278497037,10728887627281599,585214278497037,1041410691569662` |

---

## Hint

You can use the **Exponentiation by Squaring** technique for fast modular exponentiation.

```python
def mod_exp(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

