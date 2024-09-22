def calculate_structure_sum(*args):
    total_sum = 0
    stack = list(args)
    while stack:
        element = stack.pop()
        if isinstance(element, (list, tuple)):
            stack.extend(element)
        elif isinstance(element, dict):
            stack.extend(element.values())
            total_sum += sum(len(k) for k in element.keys())
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, set):
            stack.extend(element)
        else:
            total_sum += element
    return total_sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)