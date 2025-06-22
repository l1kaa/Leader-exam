# 5️⃣ Check for Armstrong Number
# Instructions:
#  An Armstrong number is one whose sum of the nth power of its digits equals the number itself.
#  Write a function to check for this.
# Test Cases:
# 153 → True (1³ + 5³ + 3³ = 153)
# 370 → True (3³ + 7³ + 0³ = 370)
# 9474 → True (9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474)
# 10 → False (1² + 0² = 1 ≠ 10)
# 1 → True (1¹ = 1)

def armstrong(num):
    res = 0
    lenn = len(str(num))
    for i in str(num):
        res += int(i) ** lenn
    return res == num

print(armstrong(153))
print(armstrong(370))
print(armstrong(10))