import re


def add(numbers: str) -> int:
    result = 0
    delimiter = ','

    if numbers == "":
        return result

    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers.replace(numbers[0:3], "")

    regex = re.escape(delimiter) + r'|\n'
    number_list = map(int, [char for char in re.split(regex, numbers) if char])

    for number in number_list:
        result += number

    return result
