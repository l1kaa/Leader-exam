# 8️⃣ Rotate List by K Positions
# Instructions:
#  Write a function that rotates a list to the right by k positions.
# Test Cases:
# [1,2,3,4,5], 2 → [4,5,1,2,3]
# [1,2,3], 1 → [3,1,2]
# [1], 0 → [1]
# [], 3 → []
# [1,2,3,4], 4 → [1,2,3,4]

def rotate(listn, position):
    if len(listn) == position:
        return listn
    res = listn[-position:][::-1] + listn[:-position]
    return res

print(rotate([1,2,3,4,5], 2))
print(rotate([1,2,3], 1))
print(rotate([1],0))