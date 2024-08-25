import re


def add(numbers: str) -> int:
    result = 0
    delimiter = ','
    negative_list = []

    if numbers == "":
        return result

    pattern_delimiter = r"^//(?:\[(.*?)\]|(.*))\n(.*)"
    match = re.match(pattern_delimiter, numbers)
    if match:
        lengthy_delimiter = match.group(1)
        single_delimiter = match.group(2)

        if lengthy_delimiter:
            delimiter = lengthy_delimiter
        elif single_delimiter:
            delimiter = single_delimiter

        numbers = match.group(3)

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
