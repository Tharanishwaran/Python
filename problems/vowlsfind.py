def extract_vowels(input_string):
    vowels = "aeiou"
    result = ""
    for char in input_string:
        if char.lower() in vowels:
            result += char
    return result

# Test the function
input_string = "hello"
print(extract_vowels(input_string))  # Output: "eo"
