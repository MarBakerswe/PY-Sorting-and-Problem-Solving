# Write your solution for algorithm 3 below

def create_sorted_list_descending(input_list):
    # To sort in descending order, we pass the argument reverse=True to the sorted() function
    sorted_list_descending = sorted(input_list, reverse=True)
    return sorted_list_descending
