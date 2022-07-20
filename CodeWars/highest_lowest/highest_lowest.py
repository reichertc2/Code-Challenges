def high_and_low(numbers):
    list_of_nums = numbers.split(' ')
    lowest = min(list_of_nums)
    highest = max(list_of_nums)       
    numbers = f'{lowest} {highest}'
        #     highest = number
    return numbers

high_and_low("1 2 3 -4 5")