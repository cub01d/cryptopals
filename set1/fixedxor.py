def fixedxor(a, b):
    return "".join( [hex(ord(x) ^ ord(y))[2:] for x,y in zip(a.decode("hex"), b.decode("hex"))] )


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
print fixedxor(a, b) # expected: 746865206b696420646f6e277420706c6179
