from typing import Iterable, List, Any

def count_vowels(text: str) -> int:
    """
    Count the number of vowels (both uppercase and lowercase) in the given string.
    """
    return sum(1 for char in text if char in "aeiouAEIOU")

def most_frequent(data: list[str]) -> str:
    """
    Return the most frequent string in the given list.
    """
    return max(data, key=data.count)

def sum_numbers(text: str) -> int:
    """
    Sum all the integers found in the given string. 
    Only digits are considered; non-digit items are ignored.
    """
    return sum([int(item) for item in text.split() if item.isdigit()])

def beginning_zeros(a: str) -> int:
    """
    Count the number of leading zeros in the given string representation of a number.
    """
    return len(str(a)) - len(str(a).lstrip('0'))

def end_zeros(a: int) -> int:
    """
    Count the number of trailing zeros in the given integer.
    """
    return len(str(a)) - len(str(a).rstrip('0'))

def count_digits(text: str) -> int:
    """
    Count the number of digits in the given string.
    """
    return sum(1 for char in text if char.isdigit())

def is_all_upper(text: str) -> bool:
    """
    Check if all characters in the given string are uppercase.
    """
    return text == text.upper()

def remove_all_before(items: list, border: int) -> Iterable:
    """
    Remove all elements before the first occurrence of 'border' in the list.
    If 'border' is not in the list, return the original list.
    """
    return items if border == 0 else items[items.index(border):] if border in items else items

def replace_first(items: list) -> Iterable:
    """
    Move the first element of the list to the end.
    If the list is empty, return it unchanged.
    """
    return items[1:] + items[:1] if items else items

def max_digit(value: int) -> int:
    """
    Find the maximum digit in the given integer.
    """
    return max([int(digit) for digit in str(value)])

def between_markers(text: str, start: str, end: str) -> str:
    """
    Extract the substring between the first occurrence of 'start' and 'end' markers.
    """
    return text[text.find(start)+1:text.find(end)]

def split_pairs(text: str) -> Iterable[str]:
    """
    Split the given string into pairs of characters. 
    If the string length is odd, append an underscore to make it even.
    """
    text += '_' * (len(text) % 2)
    return [text[i:i+2] for i in range(0, len(text)-1, 2)]

def correct_sentence(text: str) -> str:
    """
    Capitalize the first letter of the given string and ensure it ends with a period.
    """
    return text[0].upper() + text[1:] + ('.' if not text.endswith('.') else '')

def nearest_value(values: set[int], one: int) -> int:
    """
    Find the value in the set that is closest to 'one'. 
    In case of a tie, choose the smaller value.
    """
    return min(values, key=lambda x: (abs(x - one), x))

def backward_string_by_word(text: str) -> str:
    """
    Reverse each word in the given string while preserving the spaces between them.
    """
    # Handle the case where the input is only spaces
    if text.strip() == "":
        return text
    
    # Split the text into words
    words = text.split()
    
    # Initialize a list to hold spaces
    spaces = []
    
    i = 0
    
    # Loop to identify and record sequences of spaces
    while i < len(text):
        start = i
        
        # Find the start of a word
        while i < len(text) and text[i] == ' ':
            i += 1
        
        # Append the space sequence to the list
        if start < i:
            spaces.append(text[start:i])
        
        # Skip the word
        while i < len(text) and text[i] != ' ':
            i += 1

    # Create a list of inverted words
    inverted_words = [word[::-1] for word in words]

    # Initialize the resulting inverted text
    inverted_text = ""
    
    # Combine inverted words and spaces
    for j in range(max(len(inverted_words), len(spaces))):
        if j < len(inverted_words):
            inverted_text += inverted_words[j]
        if j < len(spaces):
            inverted_text += spaces[j]

    # Handle case where the last spaces are missing from `spaces`
    if len(spaces) > len(inverted_words):
        inverted_text += spaces[-1]

    return inverted_text
