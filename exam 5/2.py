# 2️⃣ Convert a List to a Dictionary
# Instructions:
#  Write a function that converts a list of key-value pair tuples into a dictionary.
# Test Cases:
# [('a', 1), ('b', 2)] → {'a': 1, 'b': 2}
# [] → {}
# [('x', 10)] → {'x': 10}
# [('a', 1), ('a', 2)] → {'a': 2}
# [('one', 1), ('two', 2)] → {'one': 1, 'two': 2}

def list_to_dict(listn):
    res = {}
    for i in listn:
        key = i[0]
        value = i[1]
        res[key] = value
    return res

print(list_to_dict([('a', 1), ('b', 2)]))