def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def are_anagrams(word1, word2):
    return count_letters(word1) == count_letters(word2)


def find_anagrams(word_list):
    anagram_dict = {}

    for word in word_list:
        found = False
        for key in anagram_dict:
            if are_anagrams(word, key):
                anagram_dict[key].append(word)
                found = True
                break

        if not found:
            anagram_dict[word] = [word]

    return {key: value for key, value in anagram_dict.items() if len(value) > 1}


if __name__ == "__main__":
    word_list = ["rat", "tar", "art", "dog", "god", "cat", "act", "pat", "tap", "apt", "bat", "tab"]
    anagrams = find_anagrams(word_list)
    for key, value in anagrams.items():
        print(f"Anagramy dla {key}: {', '.join(value)}")
