# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    text_list = list(text)
    ending_list = list(ending)
    ending_list_length = len(ending_list) * -1
    if text_list[ending_list_length: ] == ending_list:
        return True
    else:
        return False