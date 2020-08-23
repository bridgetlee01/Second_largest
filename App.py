# code to make a function that prints out the second largest number in the list

def second_largest(given_list):
    largest = None
    second_largest = None
    for current_number in given_list:
        if largest == None:
            largest = current_number
        elif current_number > largest:
            second_largest = largest
            largest = current_number
        elif second_largest == None:
            second_largest = current_number
        elif current_number > second_largest:
            second_largest = current_number
    return second_largest

my_list = [1, 3, 4, 5, 0, 2]
a_list = [-2, -2, -1]
b_list = []
print(second_largest(my_list))
print(second_largest(a_list))
print(second_largest(b_list))