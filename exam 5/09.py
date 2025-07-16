# 9️⃣ Find Longest Palindromic Substring
# Instructions:
#  Write a function that finds the longest palindromic substring in a given string.
# Test Cases:
# "babad" → "bab" or "aba"
# "cbbd" → "bb"
# "a" → "a"
# "" → ""
# "forgeeksskeegfor" → "geeksskeeg"

def longest_p(string):
    res = ""
    while res == res[::-1]:
        for i in string:
            res += i
            if len(res) >= len(string):
                return string
    return res

print(longest_p("babad"))
print(longest_p("cbbd"))