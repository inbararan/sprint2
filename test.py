b = ord(b'z')
m = 1
bits = []
for i in range(0, 8):
    bits.append(int((m & b) != 0))
    m = m << 1
bits.reverse()
print(bits)