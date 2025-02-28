
"""

Finding Keys with a Specific Value in a Dictionary
Explanation:
The goal of this problem is to find all keys in a given dictionary that are associated with a specific value (the target). 
The dictionary’s keys and values are both integers. You need to return a sorted list of keys whose values match the target.

For example, given the dictionary:
aDict = {5: 1, 3: 90, 4: 90, 12: 90, 22: 90, 21: 100}
If the target value is 90, the keys with this value are [3, 4, 12, 22].
Your function should return this list in sorted order. If no keys match the target, return an empty list.

Instructions:
1. Define the function keysWithValue(aDict, target), which takes a dictionary and an integer target as inputs.
2. Initialize an empty list result_list to store keys that match the target value.
3. Iterate through each key in the dictionary (aDict):
  - Check if the value associated with the key matches the target.
  - If it matches, append the key to result_list.
4. Sort result_list in increasing order.
5. Return result_list. If no keys match the target, it will remain an empty list.

Example Runs:

aDict = {5: 1, 3: 90, 4: 90, 12: 90, 22: 90, 21: 100}
print(keysWithValue(aDict, 90))
# Output: [3, 4, 12, 22]

print(keysWithValue(aDict, 100))
# Output: [21]

print(keysWithValue(aDict, 50))
# Output: []

"""