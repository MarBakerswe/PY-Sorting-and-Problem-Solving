# Write your solution for algorithm 2 below

def create_sorted_list(input_list):
    # The sorted() function returns a new sorted list and leaves the original list unchanged
    sorted_list = sorted(input_list)
    return sorted_list

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(create_sorted_list(numbers)) 
