# 7️⃣ Find Pairs with Given Sum
# Instructions:
#  Write a function that returns all pairs of numbers from a list that add up to a given target sum.
# Test Cases:
# [1,2,3,4], 5 → [(1,4),(2,3)]
# [0,0,1,1], 1 → [(0,1),(0,1)]
# [5,5,5], 10 → [(5,5),(5,5),(5,5)]
# [1], 2 → []
# [], 0 → []

def pair(list1, num):
    res = []
    for i in range(len(list1)):
        for n in range(i + 1, len(list1)):
            n1 = list1[i]
            n2 = list1[n]
            if n1 + n2 == num:
                res.append((n1, n2))
    return res

print(pair([1,2,3,4], 5))
print(pair([0,0,1,1], 1)) # 4 პასუხი
