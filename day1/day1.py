file_path = 'input.txt'

with open(file_path, 'r') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

# Part one - What is the sum of all of the calibration values?

# results = []
#
# for line in data:
#     digits = []
#     for char in line:
#         # Get the digits from this line of string
#         if char.isdigit():
#             digits.append(char)
#
#     if digits:
#         first_num = digits[0]
#         second_num = digits[-1]
#         result_line = int(first_num+second_num)
#         results.append(result_line)
#
# final_result = sum(results)
# print(final_result)


# Part two  -What is the sum of all the calibration values?
# some digits are written as digits - 1, some are written as words, like - one

number_names = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

results = []

for line in data:
    digits = []
    for key in number_names:
        indices = []
        start_index = 0
        while start_index < len(line):
            index = line.find(key, start_index)
            if index == -1:
                break  # No more occurrences found
            indices.append(index)
            start_index = index + 1

        if len(indices) == 1:
            value_pair = {'digit': number_names[key], 'index': indices[0]}
            digits.append(value_pair)
        elif len(indices) > 1:
            for index in indices:
                value_pair = {'digit': number_names[key], 'index': index}
                digits.append(value_pair)

    for index, char in enumerate(line):
        if char.isdigit():
            value_pair = {'digit': char, 'index': index}
            digits.append(value_pair)
    # print(digits)
    if digits:
        sorted_digits = sorted(digits, key=lambda x: x['index'])
        first_num = str(sorted_digits[0]['digit'])
        second_num = str(sorted_digits[-1]['digit'])
        result_line = int(first_num+second_num)
        results.append(result_line)


print(sum(results))


