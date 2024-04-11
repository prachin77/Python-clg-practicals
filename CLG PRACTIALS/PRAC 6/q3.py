def count_occurrences(input_string):
    # Convert the input string to lowercase to consider both cases same
    input_string = input_string.lower()

    # Initialize an empty dictionary to store occurrences of each character
    occurrences = {}

    # Loop through each character in the input string
    for char in input_string:
        # Increment the count of the character in the dictionary
        occurrences[char] = occurrences.get(char, 0) + 1

    return occurrences

# Example input string
input_string = "E Y L S R I B K J V J H A B Z N W B T V s c c k r d w a m p w v u n q a m p l o A Z G D E G F I N D x m z o u l o z j v h w i w N T G X W c d o t x h y v z y z q e a m f w p g u q T R E N N W F c r f"

# Count occurrences of each character
occurrences = count_occurrences(input_string)

# Print the occurrences of each character
for char, count in occurrences.items():
    print(f"{count} {char}", end=" ")
    print("\n")
