# Link https://leetcode.com/problems/two-sum/

from typing import List, Mapping
Index = int
Num = int

"""
Beats 92.15% in runtime
Beats 37.13% in memory
"""
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
