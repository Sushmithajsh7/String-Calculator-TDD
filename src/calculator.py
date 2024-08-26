import re


def add(numbers: str) -> int:
    result = 0
    delimiter = ','
    negative_list = []

    if numbers == "":
        return result

    pattern_delimiter = re.compile(r'\[(.*?)\]')
    matches = pattern_delimiter.findall(numbers)

    # For multiple delimiters
    if matches:
        for match in  matches:
            delimiter = delimiter + '|' + re.escape(match)
        pattern_replace =  re.compile(r'//\[(.*?)\]\n')
        numbers = pattern_replace.sub('', numbers)
    #For single delimiter
    else:
        if numbers.startswith("//"):
            delimiter = re.escape(numbers[2])
            numbers = numbers.replace(numbers[0:3], "")

    regex = delimiter + r'|\n'
    xx = re.split(regex, numbers)
    number_list = map(int, [char for char in re.split(regex, numbers) if char])

    for number in number_list:
        if number < 0:
            negative_list.append(number)
        if number < 1000:
            result += number

    if negative_list:
        raise ValueError(f"negative numbers not allowed {negative_list}")

    return result
