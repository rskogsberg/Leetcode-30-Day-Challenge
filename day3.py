#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Kadane's algorithm

def maxSubArray(nums):
    maxEndingHere = currentAbsoluteMaximum = nums [0]
    for i in range(1, len(nums)):
        maxEndingHere = max(maxEndingHere + nums[i], nums[i])
        currentAbsoluteMaximum = max(maxEndingHere, currentAbsoluteMaximum)
    return currentAbsoluteMaximum