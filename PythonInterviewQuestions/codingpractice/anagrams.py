def are_anagrams(str1, str2):
    # Remove any whitespace and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage:
word1 = "listen"
word2 = "silent"
print(f"Are '{word1}' and '{word2}' anagrams? {are_anagrams(word1, word2)}")
