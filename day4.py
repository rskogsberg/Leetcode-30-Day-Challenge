# Move all zeroes to the end of the array while preserving the order of the non-zero elements

def moveZeroes(nums):
    counter = 0
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(0)
    return nums