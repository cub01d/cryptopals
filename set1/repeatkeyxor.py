s = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = "ICE"

def encrypt(message, key):
    result = ""
    index = 0
    for c in message:
        result += chr(ord(c) ^ ord(key[index]))
        index += 1
        if index == len(key):
            index = 0
    return result

print encrypt(s, key).encode("hex")
# output:
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

