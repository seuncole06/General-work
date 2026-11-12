def find_min_max(nums: list[int]) -> tuple[int, int]:
    if len(nums) == 0:
        return (None, None)
    maximum = nums[0]
    minimum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return (maximum, minimum)

print(find_min_max(nums = [3, 1, 9, 4, 2, 7]))
print(find_min_max(nums = [-10, 0, 50, -3]))