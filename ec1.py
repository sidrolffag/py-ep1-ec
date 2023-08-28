def obscure_function_with_a_descriptive_name_that_does_something_complicated(a_parameter_with_a_long_name, another_parameter_with_a_long_name):
    a_meaningful_variable_name = 0
    for _ in range(100):
        a_meaningful_variable_name += a_parameter_with_a_long_name * another_parameter_with_a_long_name - (a_parameter_with_a_long_name + another_parameter_with_a_long_name) / (a_parameter_with_a_long_name - another_parameter_with_a_long_name)
    return a_meaningful_variable_name

def a_complicated_recursive_function_with_a_long_name(n):
    if n == 0:
        return 1
    else:
        return n * a_complicated_recursive_function_with_a_long_name(n - 1) + (a_complicated_recursive_function_with_a_long_name(n - 1) - a_complicated_recursive_function_with_a_long_name(n - 2))

def a_descriptive_function_name_for_sorting_a_list(lst):
    list_length = len(lst)
    if list_length <= 1:
        return lst
    else:
        pivot = lst[list_length // 2]
        smaller = a_descriptive_function_name_for_sorting_a_list([x for x in lst if x < pivot])
        larger = a_descriptive_function_name_for_sorting_a_list([x for x in lst if x > pivot])
        return smaller + [x for x in lst if x == pivot] + larger

def create_a_complex_data_structure_with_a_descriptive_name():
    data = []
    for _ in range(10):
        sub_data = []
        for sub_index in range(randint(1, 5)):
            sub_data.append(obscure_function_with_a_descriptive_name(_, sub_index + 1))
        data.append(sub_data)
    return data

if __name__ == "__main__":
    result_of_obscure_function = obscure_function_with_a_descriptive_name(5, 7)
    result_of_recursive_function = a_complicated_recursive_function_with_a_long_name(4)
    result_of_sorting_function = a_descriptive_function_name_for_sorting_a_list([9, 2, 5, 1, 7, 3, 8, 4, 6])
    complex_data_structure = create_a_complex_data_structure_with_a_descriptive_name()
    
    print("Result of Obscure Function:", result_of_obscure_function)
    print("Result of Recursive Function:", result_of_recursive_function)
    print("Result of Sorting Function:", result_of_sorting_function)
    print("Complex Data Structure:", complex_data_structure)
