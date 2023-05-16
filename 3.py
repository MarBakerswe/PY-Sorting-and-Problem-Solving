# Write your solution for algorithm 3 below

def create_sorted_list_descending(input_list):
    # To sort in descending order, we pass the argument reverse=True to the sorted() function
    sorted_list_descending = sorted(input_list, reverse=True)
    return sorted_list_descending

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(create_sorted_list_descending(numbers)) 
