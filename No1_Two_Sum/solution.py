# Link https://leetcode.com/problems/two-sum/

from typing import List, Mapping
Index = int
Num = int

"""
Frst method

0(n) time
O(n) space

Beats 60.64% in runtime
Beats 36.45% in memory
"""
def twoSum(nums: List[int], target: int) -> List[int]:
  memory: Mapping[Num, Index] = {}

  for i, n in enumerate(nums):
    found = memory.get(target - n)

    if found is not None:
      return [i, found]
    else:
      memory[n] = i


"""
After comparing the speed difference between `enumerate` and a `i-0; for _ in []: ...`
I decided that the second method was faster

Using timeit module
enumerate method : 10000 loops, best of 5: 27.1 usec per loop
i method         : 10000 loops, best of 5: 25.9 usec per loop
"""

# Second solution
def twoSum2(nums: List[int], target: int) -> List[int]:
  memory: Mapping[Num, Index] = {}

  i = 0
  for n in nums:
    found = memory.get(target - n)

    if found is not None:
      return [i, found]
    else:
      memory[n] = i
      i += 1

def twoSum(nums: List[int], target: int) -> List[int]:
  memory: Mapping[Num, Index] = {}

  for i, n in enumerate(nums):
    found = memory.get(target - n)

    if found is not None:
      return [i, found]
    else:
      memory[n] = i


# [1, 4, 10, 15, 16, 30, 34, 71, 98, 100] 64
# ans: []
# print(twoSum2([1,4,10,15,16,30,34,71,98,100], 64))
