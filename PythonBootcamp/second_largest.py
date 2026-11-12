def second_largest(num):
    largest = num[0]
    second_largest = None

    for i in num:
        if i > largest:
            second_largest = largest
            largest = i

        elif i != largest:
            if second_largest is None or i > second_largest:
                second_largest = i

    return second_largest

num = [10, 5, 8, 20, 15]
result = second_largest(num)

print(result)
