#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
        print(a)
    return a