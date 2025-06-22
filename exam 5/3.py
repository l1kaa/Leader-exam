# 3️⃣ Find All Unique Substrings of a String
# Instructions:
#  Write a function that takes a string and returns a list of all unique substrings.
# Test Cases:
# "abc" → ["a","ab","abc","b","bc","c"]
# "a" → ["a"]
# "ab" → ["a","ab","b"]
# "" → []
# "aa" → ["a","aa"]

def unique(s):
    res = set()
    for i in range(len(s)):
        for n in range(i + 1, len(s) + 1):
            res.add(s[i:n])
    return sorted(res)

print(unique("abc"))
