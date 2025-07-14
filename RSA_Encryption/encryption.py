x = input()
#x = input(" please input nem:")
n_str, e_str, text = x.split()
n = int(n_str)
e = int(e_str)


ascii_values = [ord(char) for char in text]

# 輸出結果
#print("n:", n)
#print("e:", e)
#print("ASCII values for text:", ascii_values)


# 將整數轉換為二進位 去掉 '0b' 前綴
binary_string = bin(e)[2:]

# 將二進位字串轉換為一個包含每個位元的整數列表
binary_array = [int(bit) for bit in binary_string]

# 輸出結果
#print("Binary array:", binary_array)

binary_size = len(binary_array)
#print ("binary array", binary_size)
text_size = len(ascii_values)
c = []
for i in range(text_size):
    y = 1
    power = ascii_values[i] % n
    for j in range (binary_size-1,-1,-1):
        #print (binary_array[j], " this is binary ", j )
        if (binary_array[j] == 1):
            y = (y*power)%n 
        power = (power*power)%n
    c.append(y)  # 使用 append 方法
print(",".join(map(str, c)))
