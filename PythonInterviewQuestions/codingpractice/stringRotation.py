def left_rotate(s, n):
    n = n % len(s)  # Ensure n is within the length of the string
    return s[n:] + s[:n]

def right_rotate(s, n):
    n = n % len(s)  # Ensure n is within the length of the string
    return s[-n:] + s[:-n]


s = "hello"
l = 2
r = 3

# Left rotation by 2
left_rotated = left_rotate(s, l)
print(f"Left rotated: {left_rotated}")  # Output: "llohe"

# Right rotation by 2
right_rotated = right_rotate(left_rotated, r)
print(f"Right rotated: {right_rotated}")  # Output: "lohel"
