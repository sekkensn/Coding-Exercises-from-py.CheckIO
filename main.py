# main.py

from functions import *

def prompt_for_text(prompt: str) -> str:
    return input(prompt)

def prompt_for_int(prompt: str) -> int:
    return int(input(prompt))

def prompt_for_list(prompt: str) -> list[str]:
    return input(prompt).split()

def prompt_for_set(prompt: str) -> set[int]:
    return set(map(int, input(prompt).split()))

def main():
    print("Choose a function to execute:")
    print("[C]ount Vowels")
    print("[M]ost Frequent")
    print("[S]um Numbers")
    print("[B]eginning Zeros")
    print("[E]nd Zeros")
    print("[D]igit Count")
    print("[U]pper Check")
    print("[R]emove All Before")
    print("[P]Replace First")
    print("[X]Max Digit")
    print("[T]Between Markers")
    print("[L]Split Pairs")
    print("[O]Correct Sentence")
    print("[N]earest Value")
    print("[W]Backward String by Word")
    
    choice = input("Enter your choice: ").upper()

    if choice == 'C':
        text = prompt_for_text("Enter text: ")
        print(count_vowels(text))

    elif choice == 'M':
        data = prompt_for_list("Enter a list of strings separated by spaces: ")
        print(most_frequent(data))

    elif choice == 'S':
        text = prompt_for_text("Enter text with numbers: ")
        print(sum_numbers(text))

    elif choice == 'B':
        a = prompt_for_text("Enter a number as a string: ")
        print(beginning_zeros(a))

    elif choice == 'E':
        a = prompt_for_int("Enter an integer: ")
        print(end_zeros(a))

    elif choice == 'D':
        text = prompt_for_text("Enter text: ")
        print(count_digits(text))

    elif choice == 'U':
        text = prompt_for_text("Enter text: ")
        print(is_all_upper(text))

    elif choice == 'R':
        items = prompt_for_list("Enter a list of integers separated by spaces: ")
        border = prompt_for_int("Enter the border integer: ")
        print(remove_all_before(items, border))

    elif choice == 'P':
        items = prompt_for_list("Enter a list of integers separated by spaces: ")
        print(replace_first(items))

    elif choice == 'X':
        value = prompt_for_int("Enter an integer: ")
        print(max_digit(value))

    elif choice == 'T':
        text = prompt_for_text("Enter text: ")
        start = prompt_for_text("Enter start marker: ")
        end = prompt_for_text("Enter end marker: ")
        print(between_markers(text, start, end))

    elif choice == 'L':
        text = prompt_for_text("Enter text: ")
        print(split_pairs(text))

    elif choice == 'O':
        text = prompt_for_text("Enter text: ")
        print(correct_sentence(text))

    elif choice == 'N':
        values = prompt_for_set("Enter a set of integers separated by spaces: ")
        one = prompt_for_int("Enter the reference integer: ")
        print(nearest_value(values, one))

    elif choice == 'W':
        text = prompt_for_text("Enter text: ")
        print(backward_string_by_word(text))

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()


