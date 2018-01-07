from singlebytexor import score, decrypt

with open("4.txt", "r") as f:
    for line in f.read().split("\n"):
        d = decrypt(line)
        if d is not None:
            print line,  d

# 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f Now that the party is jumping

