def code214(s: str) -> str:
    # Function to find the longest palindrome suffix of a string
    def longest_palindrome_suffix(string):
        for i in range(len(string) - 1, -1, -1):
            if string[i:] == string[i:][::-1]:
                return string[i:]
        return ""

    # If the string is empty or already a palindrome, return it as is
    if s == "" or s == s[::-1]:
        return s

    # Find the longest palindrome suffix
    palindrome_suffix = longest_palindrome_suffix(s)

    # If the original string is a palindrome, return it as is
    if palindrome_suffix == s:
        return s

    # Append the remaining part of the string to the palindrome suffix
    return s[len(palindrome_suffix):][::-1] + s
