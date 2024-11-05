first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(a, b) for a in first_strings for b in second_strings if len(a) == len(b)]
third_result = {n: len(n) for n in (first_strings + second_strings) if len(n) % 2 != 1}



print(first_result)
print(second_result)
print(third_result)