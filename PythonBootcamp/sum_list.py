def sum_list(nums: list[int]) -> int:
    total = 0
    for i in nums:
        total = total + i
    return total

print(sum_list(nums = [-1, 10, -5, 20]))