def roman_to_int(s: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev_value = 0

    for char in reversed(s.upper().strip()):
        if char not in roman_map:
            raise ValueError(f"Invalid character '{char}'")

        value = roman_map[char]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value  # Always update prev_value to the current character's value

    return total


if __name__ == "__main__":
    user_input = input("Enter a Roman numeral: ")
    try:
        result = roman_to_int(user_input)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")