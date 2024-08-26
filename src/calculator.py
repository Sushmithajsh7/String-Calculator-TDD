import re

def add(numbers: str) -> int:
    """
    Adds together numbers in a given string, supporting custom delimiters and handling special cases.

    This function processes a string of numbers, which can be separated by custom delimiters specified
    in the format `//[delimiter]\n`. Multiple delimiters can be defined using `//[delimiter1][delimiter2]\n`.
    Delimiters might be of any length.
    The function sums up all the numbers in the string, ignores numbers greater than or equal to 1000,
    and raises a `ValueError` if any negative numbers are encountered.

    Args:
        numbers (str): A string containing numbers separated by delimiters.

    Returns:
        int: The sum of the numbers in the string.

    Raises:
        ValueError: If any negative numbers are present in the input string.
    """

    result = 0
    delimiter = ','
    negative_list = []

    if numbers == "":
        return result

    # Regex to check and fetch the multiple delimiters
    pattern_delimiter = re.compile(r'\[(.*?)\]')
    matches = pattern_delimiter.findall(numbers)

    # For multiple delimiters
    if matches:
        for match in matches:
            delimiter = delimiter + '|' + re.escape(match)
        pattern_replace = re.compile(r'//\[(.*?)\]\n')
        numbers = pattern_replace.sub('', numbers)  # Fetch the number string after fetching the delimiters

    # For single delimiter
    else:
        if numbers.startswith("//"):
            delimiter = re.escape(numbers[2])
            numbers = numbers.replace(numbers[0:3], "")

    regex = delimiter + r'|\n'
    # Split the number string based on all the delimiters.
    # Then convert the string of lists to integer of lists
    number_list = map(int, [char for char in re.split(regex, numbers) if char])

    for number in number_list:
        if number < 0:
            negative_list.append(number)        # To get all the negative number list
        if number < 1000:
            result += number                    # Add up all the numbers to result

    # If there ae any negative value raise exception
    if negative_list:
        raise ValueError(f"negative numbers not allowed {negative_list}")

    return result
