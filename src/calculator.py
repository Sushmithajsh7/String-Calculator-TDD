import re


def add(numbers: str) -> int:
    sum = 0

    if numbers == "":
        return sum

    number_list = map(int, re.split(r',|\n', numbers))

    for number in number_list:
        sum += number

    return sum
