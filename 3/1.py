def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(words):
    palindromes = []
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes
words = ['some', 'example', 'palindromes', 'are', 'madam', 'aibohphobia', 'and', 'a', 'man', 'a', 'plan', 'a', 'canal', 'panama']
print(find_palindromes(words))
input()