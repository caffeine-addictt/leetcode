[Question Link](https://leetcode.com/problems/two-sum/)

# First thoughts

I initially thought of solving this question with nested loops, but decided against a O(n^2) time solution.

Here is a basic example of a O(n^2) solution
```py
def twoSum(nums: List[int], target: int) -> List[int]:
  for i, n in enumerate(nums):
    for i2, n2 in enumerate(nums):
      if n2 + n == target:
        return [i, i2]

>>> timeit -s 'twoSum([1,4,10,15,16,30,34,71,98,100], 64)'
100000 loops, best of 5: 3.24 usec per loop
```

And the same O(n^2) solution optimized (~5.56% faster)
```py
def twoSum(nums: List[int], target: int) -> List[int]:
  for i, n in enumerate(nums):
    for i2, n2 in enumerate(nums[i+1:]):
      if n2 + n == target:
        return [i, i2]

>>> timeit -s 'twoSum([1,4,10,15,16,30,34,71,98,100], 64)'
100000 loops, best of 5: 3.06 usec per loop
```

<br />


# My Solution

My solution is caching.<br />
By storing the number as the key and the index as it's value in a dictionary (baiscally a hash map), I can make use of the O(1) lookup time which turns it into a O(n) algorithm.

Comparison
* ~71.30% faster than the unoptimized O(n^2) solution
* ~69.61% faster than the optimized O(n^2) solution

Here is the initial solution
```py
def twoSum(nums: List[int], target: int) -> List[int]:
  memory: Mapping[Num, Index] = {}

  for i, n in enumerate(nums):
    found = memory.get(target - n)

    if found is not None:
      return [i, found]
    else:
      memory[n] = i

>>> timeit -s 'twoSum([1,4,10,15,16,30,34,71,98,100], 64)'
100000 loops, best of 5: 930 nsec per loop
```

<br />

### However, let's optimize it further!

There are 2 main ways to loop with indexes
```py
# The first
for i, v in enumerate([]):
  ...

# The second
i = 0
for v in []:
  i += 1
  ...
```

On profiling them, I discovered that the second method is a whopping ~90.50% faster than the first.
```py
>>> timeit 'for i, _ in enumerate(range(10)): print(i)'
100000 loops, best of 5: 466 usec per loop

>>> timeit -s 'i = 0' 'for _ in range(10): print(i); i += 1'
100000 loops, best of 5: 44.3 usec per loop
```

<br />


### Optimized solution

Which brings me to the final solution:
* Best case: O(1) time, O(1) space
* Worst case: O(n) time, O(n) space

<br />

* ~71.76% faster than the unoptimized O(n^2) solution
* ~70.10% faster than the optimized O(n^2) solution
* ~1.61% faster than the unoptimized O(n) solution

```py
def twoSum(nums: List[int], target: int) -> List[int]:
  memory: Mapping[Num, Index] = {}

  i = 0
  for n in nums:
    found = memory.get(target - n)

    if found is not None:
      return [i, found]
    else:
      memory[n] = i
      i += 1

>>> timeit -s 'twoSum([1,4,10,15,16,30,34,71,98,100], 64)'
100000 loops, best of 5: 915 nsec per loop
```