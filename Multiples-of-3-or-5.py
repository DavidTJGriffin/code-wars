# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number):
    sum = 0
    if number < 0:
        return 0
    for natural_numbers in range(0, number):
        if natural_numbers != 0:
            if natural_numbers % 3 == 0 and natural_numbers % 5 == 0:
                sum += natural_numbers
                print(natural_numbers)
            elif natural_numbers % 3 == 0 or natural_numbers % 5 == 0:
                sum += natural_numbers
                print(natural_numbers)
            elif number < 0:
                print('less than zero')
    return(sum)