def binary_search(nums, target) -> tuple[int, int]:
    low = 0 
    high = len(nums) -1
    index_found = -1
    comparison_count = 0
   

    while low <= high:
        mid = low + (high - low) // 2
        comparison_count += 1

        if nums[mid] == target:
            index_found = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return (index_found, comparison_count)

print(binary_search(nums = [1, 3, 3, 3, 5, 8], target = 3))
print(binary_search(nums = [1, 3, 5, 8],       target = 4)) 
print(binary_search(nums = [],                 target = 7))
