def flip_bits(s):
    return "".join("1" if c == "0" else "0" for c in s)

s = input()
print(flip_bits(s))
