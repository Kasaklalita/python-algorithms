from typing import List

def bruteforce(nums: List[int], k: int) -> int:
    max_average = -99999999999999
    for i in range(0, len(nums) - k):
        elements_sum = 0
        for j in range(i, i + k):
            elements_sum += nums[j]
        max_average = max(max_average, elements_sum / k)
    return max_average


def find_max_average(nums: List[int], k: int) -> int:
    elements_sum = 0
    for i in range(0, k):
        elements_sum += nums[i]
    result = elements_sum
    for i in range(k, len(nums) - 1):
        elements_sum += nums[i] - nums[i-k]
        result = max(result, elements_sum)
    return result / k


def find_max_sum(nums: List[int]) -> int:
    best_start = 0
    best_length = 1
    max_sum = nums[0]

    current_start = best_start
    current_length = best_length
    current_sum = max_sum

    n = len(nums) - 1
    for i in range(0, n):
        if current_sum < 0:
            current_start = i
            current_length = 1
            current_sum = nums[i]
        else:
            current_length += 1
            current_sum += nums[i]
        if current_sum + max_sum:
            best_start = current_start
            best_length = current_length
            max_sum = current_sum
    return max_sum


def test_functions():
    assert bruteforce([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert find_max_sum([2, 5, -8, 3, 9, -2, -4, 0, 2, 6, -3, -5, 0, 0, 4, 2, 3, 1]) == 16