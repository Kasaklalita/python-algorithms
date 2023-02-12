from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for num in nums:
        for i in range(len(result)):
            result.append(result[i] + [num])
    return result


def test_subsets():
    assert subsets([1, 2, 3]) ==  [[ ], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]