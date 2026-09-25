def extract_even(lst):
    even_numbers = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_numbers.append(lst[i])
    return even_numbers


original_list = [1, 4, 5, -1, 10]
print("Original list:", original_list)

result = extract_even(original_list)
print("List with only even numbers:", result)