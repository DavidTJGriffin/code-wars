# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    num_list = []
    ordered_list = []
    string_ordered_list = []
    
    for digits in (str(num)):
        num_list.append(int(digits))
    
    for elements in range(len(num_list)):
        ordered_list.append(max(num_list))
        del num_list[num_list.index(max(num_list))]
    
    for numbers in ordered_list:
        string_ordered_list.append(str(numbers))
        
    
    return int("".join(string_ordered_list))