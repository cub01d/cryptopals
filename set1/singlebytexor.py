def score(text):
    """
    Returns frequency analysis score for text.
    Frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
    """

    freqs = {
            ' ': 12,
            # lowercase
            'e': 12.70,
            't': 9.06,
            'a': 8.17,
            'o': 7.51,
            'i': 6.97,
            'n': 6.75,
            's': 6.33,
            'h': 6.09,
            'r': 5.99,
            'd': 4.25,
            'l': 4.03,
            'c': 2.78,
            'u': 2.76,
            'm': 2.41,
            'w': 2.36,
            'f': 2.23,
            'g': 2.02,
            'y': 1.97,
            'p': 1.93,
            'b': 1.29,
            'v': 0.98,
            'k': 0.77,
            'j': 0.15,
            'x': 0.15,
            'q': 0.10,
            'z': 0.07,
            # uppercase
            'E': 12.70,
            'T': 9.06,
            'A': 8.17,
            'O': 7.51,
            'I': 6.97,
            'N': 6.75,
            'S': 6.33,
            'H': 6.09,
            'R': 5.99,
            'D': 4.25,
            'L': 4.03,
            'C': 2.78,
            'U': 2.76,
            'M': 2.41,
            'W': 2.36,
            'F': 2.23,
            'G': 2.02,
            'Y': 1.97,
            'P': 1.93,
            'B': 1.29,
            'V': 0.98,
            'K': 0.77,
            'J': 0.15,
            'X': 0.15,
            'Q': 0.10,
            'Z': 0.07
    }

    s = 0
    for letter in text:
        if letter in freqs:
            s += freqs[letter]
    return s

def decrypt(c):
    # iterate over every possible key
    maxscore = 0
    result = None
    for key in range(256):
        decoded = "".join( [chr(ord(x) ^ key) for x in c.decode("hex")] )
        s = score(decoded)
        if s > maxscore:
            maxscore = s
            result = decoded
    return result

print decrypt("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
# output: "Cooking MC's like a pound of bacon"






