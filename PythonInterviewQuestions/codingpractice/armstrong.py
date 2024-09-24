def is_armstrong_number(num):
    # Convert the number to a string to easily iterate through its digits
    num_str = str(num)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Sum each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum is equal to the original number
    return total == num

# Example usage:
number = 153
print(f"Is {number} an Armstrong number? {is_armstrong_number(number)}")
