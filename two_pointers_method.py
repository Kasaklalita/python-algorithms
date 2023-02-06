from typing import List

def bruteforce(nums: List[int], target: int) -> List[int]:
    for i, _ in enumerate(nums):
        for j, _ in enumerate(nums):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
        raise Exception('The pair must be found')
    
def two_pointers(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left != right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
    raise Exception('The pair must be found')


def two_pointers_with_dict(nums: List[int], target: int) -> List[int]:
    m = {}
    for i, x in enumerate(nums):
        m[x] = i
    for i, x in enumerate(nums):
        complement = target - x
        if complement in m and m[target - x] != i:
            return [i, m[target - x]]
    raise Exception('The pair must be found')
    
def test_functions():
    assert bruteforce([2, 7, 11, 15], 9) == [0, 1]
    assert two_pointers([2, 7, 11, 15], 9) == [0, 1]
    assert two_pointers_with_dict([2, 7, 11, 15], 9) == [0, 1]