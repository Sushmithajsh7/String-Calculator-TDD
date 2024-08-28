# String-Calculator-TDD (Incubyte TDD Assessment)

This project implements a feature for summing numbers from a formatted string input using a Test-Driven Development (TDD) approach. The feature  supports custom delimiters, handling large numbers, and detecting errors related to negative values.

## Features
#### Custom Delimiters: 
Supports custom delimiters specified in the format //[delimiter]\n.
Multiple delimiters can be defined using //[delimiter1][delimiter2]\n. 
Delimiters can be of any length.
#### Ignores Large Numbers:
Numbers greater than or equal to 1000 are ignored during the sum calculation.
#### Error Handling: 
Raises a ValueError if any negative numbers are present in the input string.

## Usage
#### Function Signature

```python
def add(numbers: str) -> int:
    """
    Adds together numbers in a given string, supporting custom delimiters and handling special cases.
    """
```

## Arguments
numbers (str): A string containing numbers separated by delimiters.

## Returns
int: The sum of the numbers in the string.

## Raises
ValueError: If any negative numbers are present in the input string.


## Example Usage
```python
#### Example 1: Using default delimiters (comma and newline)
result = add("1,2,3")
print(result)  # Output: 6

#### Example 2: Using a custom single-character delimiter
result = add("//;\n1;2;3")
print(result)  # Output: 6

#### Example 3: Using multiple custom delimiters
result = add("//[*][%]\n1*2%3")
print(result)  # Output: 6

#### Example 4: Handling numbers >= 1000
result = add("2,1000,1001,3")
print(result)  # Output: 5

#### Example 5: Handling negative numbers
try:
    result = add("1,-2,3")
except ValueError as e:
    print(e)  # Output: Negative numbers are not allowed: -2
```

## Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/Sushmithajsh7/String-Calculator-TDD.git
```

Navigate to the project directory:
```bash
cd custom-string-calculator
```

## Contributing
Feel free to open issues or submit pull requests if you find bugs or want to contribute to this project.

## References 
1. https://blog.incubyte.co/blog/tdd-assessment/
2. https://www.youtube.com/watch?v=qkblc5WRn-U
3. https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/
















