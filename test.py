def rotate_word(word, shift):
    """Rotates each letter in a word by the given shift value."""
    result = ''
    
    for char in word:
        if char.isalpha():  # Only rotate letters
            start = ord('A') if char.isupper() else ord('a')
            rotated = chr(start + (ord(char) - start + shift) % 26)
            result += rotated
        else:
            result += char  # Keep non-letter characters unchanged

    return result

# Example usage:
print(rotate_word("cheer", 7))   # Output: "jolly"
print(rotate_word("melon", -10)) # Output: "cubed"
print(rotate_word("IBM", -1))    # Output: "HAL"
print(rotate_word("Hello, World!", 5))  # Output: "Mjqqt, Btwqi!"

