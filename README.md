# Python Functions

This repository contains various utility functions implemented in Python. The functions demonstrate basic operations and manipulations on strings, numbers, and lists.

## Functions

- `count_vowels(text: str) -> int`: Counts the number of vowels in the given string.
- `most_frequent(data: list[str]) -> str`: Returns the most frequent string in the given list.
- `sum_numbers(text: str) -> int`: Sums all the integers found in the given string.
- `beginning_zeros(a: str) -> int`: Counts the number of leading zeros in the given string representation of a number.
- `end_zeros(a: int) -> int`: Counts the number of trailing zeros in the given integer.
- `count_digits(text: str) -> int`: Counts the number of digits in the given string.
- `is_all_upper(text: str) -> bool`: Checks if all characters in the given string are uppercase.
- `remove_all_before(items: list, border: int) -> list`: Removes all elements before the first occurrence of 'border' in the list.
- `replace_first(items: list) -> list`: Moves the first element of the list to the end.
- `max_digit(value: int) -> int`: Finds the maximum digit in the given integer.
- `between_markers(text: str, start: str, end: str) -> str`: Extracts the substring between the first occurrence of 'start' and 'end' markers.
- `split_pairs(text: str) -> list[str]`: Splits the given string into pairs of characters.
- `correct_sentence(text: str) -> str`: Capitalizes the first letter of the given string and ensures it ends with a period.
- `nearest_value(values: set[int], one: int) -> int`: Finds the value in the set that is closest to 'one'. In case of a tie, chooses the smaller value.
- `backward_string_by_word(text: str) -> str`: Reverses each word in the given string while preserving the spaces between them.

## Usage

To use these functions, import them into your Python script. For example:

```python
from functions import count_vowels, most_frequent

text = "Hello World"
print(count_vowels(text))  # Output: 3

data = ["apple", "banana", "apple"]
print(most_frequent(data))  # Output: apple
