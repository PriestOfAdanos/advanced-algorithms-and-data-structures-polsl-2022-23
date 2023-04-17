def find_anagrams(word_list):
    anagram_dict = {}

    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    return {key: value for key, value in anagram_dict.items() if len(value) > 1}


if __name__ == "__main__":
    word_list = ["rat", "tar", "art", "dog", "god", "cat", "act", "pat", "tap", "apt", "bat", "tab"]
    anagrams = find_anagrams(word_list)
    for key, value in anagrams.items():
        print(f"Anagramy dla {key}: {', '.join(value)}")
