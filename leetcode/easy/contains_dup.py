from typing import List


s1 = [1, 2, 3, 4]
s2 = [1, 1, 2, 3, 4]


def containsDuplicate(nums: List[int]) -> bool:

    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(containsDuplicate(s1))  # Confirms false
print(containsDuplicate(s2))  # Confirms true
