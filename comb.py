import itertools
import string

# Define the template with placeholders for replacements
template = "ruthless__n_.2002"

# Define the positions of underscores to replace (0-based index)
positions = [8, 9, 12]  # Adjust the index positions of underscores

# Generate all alphanumeric characters and specified special characters
chars = string.ascii_letters + string.digits + "!@#$%^&*()"

# Create all combinations of three characters from the extended set
combinations = itertools.product(chars, repeat=len(positions))

# Function to replace characters in specific positions of a string
def replace_positions(s, positions, replacements):
    s = list(s)
    for pos, repl in zip(positions, replacements):
        s[pos] = repl
    return ''.join(s)

# Open a text file to write the outputs
with open('name_combinations.txt', 'w') as file:
    # Generate and write all possible names to the file
    for combo in combinations:
        name = replace_positions(template, positions, combo)
        file.write(name + '\n')

print("All combinations have been written to 'name_combinations.txt'.")
