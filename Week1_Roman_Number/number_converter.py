def roman_to_integer(roman):
    roman = roman.strip().upper()

    if not roman:
        raise ValueError("Roman numeral cannot be empty.")

    # Base values and canonical order mapping for strict validation
    lookup = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    # Verify all characters are valid base symbols
    if any(char not in lookup for char in roman):
        raise ValueError("Invalid Roman numeral character.")

    # Check repetition limits (V, L, D cannot repeat; others max 3)
    for char in ("V", "L", "D"):
        if char * 2 in roman:
            raise ValueError("V, L, and D cannot be repeated.")

    for char in ("I", "X", "C", "M"):
        if char * 4 in roman:
            raise ValueError("A Roman numeral cannot repeat more than 3 times.")

    # Validate subtractive pairs
    valid_subtractions = {"IV", "IX", "XL", "XC", "CD", "CM"}
    for i in range(len(roman) - 1):
        if lookup[roman[i]] < lookup[roman[i + 1]]:
            pair = roman[i:i + 2]
            if pair not in valid_subtractions:
                raise ValueError(f"Invalid subtraction: {pair}")

    # Calculate integer total
    total = sum(
        -lookup[roman[i]] if i + 1 < len(roman) and lookup[roman[i]] < lookup[roman[i + 1]]
        else lookup[roman[i]]
        for i in range(len(roman))
    )

    if total < 1 or total > 3999:
        raise ValueError("Roman numeral must represent a number from 1 to 3999.")

    # Strict structure check using canonical re-encoding
    if integer_to_roman(total) != roman:
        raise ValueError("Invalid Roman numeral format.")

    return total


def integer_to_roman(number):
    mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = []
    for val, symbol in mapping:
        count, number = divmod(number, val)
        result.append(symbol * count)

    return "".join(result)


if __name__ == "__main__":
    while True:
        user_input = input("Enter a Roman numeral: ")

        try:
            result = roman_to_integer(user_input)
            print("Integer:", result)
        except ValueError as error:
            print("Invalid input:", error)
            continue

        while True:
            again = input("Do you want to continue? (yes/no): ").strip().lower()
            if again in ("yes", "y"):
                break
            elif again in ("no", "n"):
                print("Goodbye!")
                exit()
            else:
                print("Please enter yes or no.")