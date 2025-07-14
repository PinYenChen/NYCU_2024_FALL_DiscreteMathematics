def prime_factors(n,factors):

    # First, handle the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # n must be odd. Start from 3 and check each odd number
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is still greater than 2, then n itself is a prime number
    if n > 2:
        factors.append(n)
    
    return factors

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1 #終止條件當其中一方為零
    gcd, x1, y1 = extended_gcd(b % a, a) #遞迴帶入 b % a 
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(e, m):
    gcd, x, _ = extended_gcd(e, m)
    if x < 0 :
        return x % m
    else:
        return x 

# 輸入範例格式：「221 5 89,99」
#x = input("請輸入 n, e 以及加密的 c 值（例如：221 5 89,99）：")
x = input()
# 先將整行數據分割為 n, e 和 c
n_str, e_str, c_str = x.split()

# 將 n 和 e 轉換為整數
n = int(n_str)
e = int(e_str)

# 將 c 部分的每個數字（用逗號分隔）轉換為整數列表
c = list(map(int, c_str.split(',')))

# 檢查輸入結果
#print("n:", n)
#print("e:", e)
#print("c:", c)

factors = []
prime_factors ( n, factors)
phi = (factors[0]-1)*(factors[1]-1)
#print ("phi", phi)
c_size = len(c)

d = modular_inverse(e, phi)
# 將整數轉換為二進位 去掉 '0b'
binary_string = bin(d)[2:]
# 將二進位字串轉換為一個包含每個位元的整數列表
binary_array = [int(bit) for bit in binary_string]

# 輸出結果
#print("Binary array:", binary_array)

binary_size = len(binary_array)
text = []
for i in range(c_size):
    y = 1
    power = c[i] % n
    for j in range (binary_size-1,-1,-1):
        #print (binary_array[j], " this is binary ", j )
        if (binary_array[j] == 1):
            y = (y*power)%n 
        power = (power*power)%n
    text.append(y)  # 使用 append 方法
characters = [chr(code) for code in text]
result = ''.join(characters)  # Join characters to form a 
print(result)
