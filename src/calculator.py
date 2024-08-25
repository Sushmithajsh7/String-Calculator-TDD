import re


def add(numbers: str) -> int:
    result = 0
    delimiter = ','
    negative_list = []

    if numbers == "":
        return result

    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers.replace(numbers[0:3], "")

    regex = re.escape(delimiter) + r'|\n'
    number_list = map(int, [char for char in re.split(regex, numbers) if char])

    for number in number_list:
        if number < 0:
            negative_list.append(number)
        if number < 1000:
            result += number

    if negative_list:
        raise ValueError(f"negative numbers not allowed {negative_list}")

    return result
