def fibonacci(N):
    a = 0
    b = 1

    forward_num = ""
    even_sum = ""
    reversed_num = ""

    for i in range(N):
        if i == 0:
            forward_num = forward_num(a)
            reversed_num = reversed_num(a)
        else:
            forward_num = forward_num + ", " + str(a)
            reversed_num = str(a) +", " + reversed_num
    
        next_num = 0
        