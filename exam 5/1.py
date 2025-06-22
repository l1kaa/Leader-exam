# 1️⃣ Sum Digits Until Single Digit
# Instructions:
#  Write a function that takes a non-negative integer and returns the sum of its digits. If the result has more than one digit, repeat the process until the result is a single digit.
# Test Cases:
# 123 → 6
# 0 → 0
# 9999 → 9
# 45 → 9
# 1 → 1

def sumDigits(num):
    num = str(num)
    
    while len(num) > 1:
        sum_n = 0
        for i in num:
            sum_n += int(i)
        num = str(sum_n)
    return int(num)

print(sumDigits(123))
print(sumDigits(0))