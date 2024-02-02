def case_counter(text):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0

    # Iterate through each character in the input string
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1

    # Return the counts of uppercase and lowercase letters
    return uppercase_count, lowercase_count