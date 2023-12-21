import re

file_path = 'input.txt'

with open(file_path, 'r') as file:
    data = file.readlines()
    data = [line.strip() for line in data]


# Part 1
# Determine which games would have been possible if the bag had been loaded with
# only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

# Parse the string to get the total amount of each color cubes
possible_games = []

for index, line in enumerate(data):
    sliced_line = re.split(r'[;,:]', line)
    # clean by removing the game nr from the first list item
    sliced_line.pop(0)
    possible_game = True
    for set in sliced_line:
        # Get the amount of cubes
        amount = int(re.search(r'\d+', set).group())
        if 'red' in set and amount > 12:
            possible_game = False
        elif 'green' in set and amount > 13:
            possible_game = False
        elif 'blue' in set and amount > 14:
            possible_game = False

    if possible_game:
        possible_games.append(index+1)


print(sum(possible_games))

# Part two
# Find the minimum set of cubes for each game. The power of the game is the min multiplied

mimimum_power = []

for line in data:
    sliced_line = re.split(r'[;,:]', line)
    # clean by removing the game nr from the first list item
    sliced_line.pop(0)
    red = []
    green = []
    blue = []
    for set in sliced_line:
        # Get the amount of cubes
        amount = int(re.search(r'\d+', set).group())
        if 'red' in set:
            red.append(amount)
        elif 'green' in set:
            green.append(amount)
        elif 'blue' in set:
            blue.append(amount)
    print(f"The values are: red={red}, green={green}, blue={blue}")

    mimimum_power.append(max(red) * max(green) * max(blue))

print(sum(mimimum_power))
