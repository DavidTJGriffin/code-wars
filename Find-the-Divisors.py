# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

def divisors(integer):
    divisor_list = []
    for index in range(1, integer+1):
         if integer % index == 0:
                divisor_list.append(index)
    if len(divisor_list) == 2:
        return f'{integer} is prime'
    else:
        divisor_list.remove(1)
        divisor_list.remove(integer)
        return divisor_list    