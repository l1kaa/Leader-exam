# 6️⃣ Sum Numbers in a String
# Instructions:
#  Write a function that finds all numbers in a string and returns their sum.
# Test Cases:
# "abc123xyz" → 123
# "7 apples and 3 oranges" → 10
# "no numbers" → 0
# "1a2b3c" → 6
# "100 200" → 300

# def sumNums(string):
#     res = 0
#     for i in string:
#         if i.isdigit():
#             res += int(i)
#     return res

# print(sumNums("7 apples and 3 oranges"))



def sumNums(string):
    res = 0
    str2 = string

    for i in string:
        index = str2.find(i)
        if i.isdigit() and str2[index+1].isdigit() == False:
            res += int(i)
        else:
            for s in string:
                index = str2.find(i)
                if s.isdigit():
                    res2 = ""
                    res2 += s
                    if str2[index+1].isdigit():
                        res2 += str2[index+1]
    return res

print(sumNums("100 200"))
