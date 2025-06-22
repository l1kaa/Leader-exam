# 4️⃣ Implement a Simple Caesar Cipher
# Instructions:
#  Write a function that takes a message and a shift value and returns the message with each letter shifted (A→B, B→C, etc). Ignore non-alphabet characters.
# Test Cases:
# "abc", 1 → "bcd"
# "xyz", 2 → "zab"
# "Hello!", 3 → "Khoor!"
# "ABC", 1 → "BCD"
# "Test 123", 4 → "Xiwx 123"


def caesar_cipher(message, shift):
    alph = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for i in message:
        if i.isalpha():
            # try:
                index = alph.find(i)
                res += alph[index + shift]
            # except IndexError:
        else:
            None
    return res

print(caesar_cipher("abc",1))
print(caesar_cipher("xyz",2))
print(caesar_cipher("Hello!", 3))
