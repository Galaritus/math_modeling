name = ['I', 'v', 'a', 'n', 'K', 'a', 'z', 'a', 'k', 'o', 'v']
name_str = "_".join(name)
print(name_str)
n = name_str.upper() 
for symbol in n:
    print(ord(symbol), end="; ")
symbol_codes1 = [ord(symbol) for symbol in n]
print(symbol_codes1)
c = name_str.lower()
for symbol in c:
    print(ord(symbol), end="; ")
symbol_codes2 = [ord(symbol) for symbol in c]
print(symbol_codes2)
a1 = max(symbol_codes1)
b1 = min(symbol_codes1)
a2 = max(symbol_codes2)
b2 = min(symbol_codes2)
print(a1, b1)
print(a2, b2)