def is_palindrome(s: str) -> bool:
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is the same forwards and backwards
    print(cleaned)
    return cleaned == cleaned[::-1]

# Example usage:
string = "A man, a plan, a canal, Panama!"
# print((''.join(string.split())).replace(',','').lower())
print(is_palindrome(string))  # Output: True
