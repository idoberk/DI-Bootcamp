# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

# Note: None of the methods in the class should print anything.


class AnagramChecker:
    def __init__(self, file_path):
        """
        The AnagramChecker class constructor.
        Initializes an empty set for the words, and call the load_file method.
        """
        self.word_set = set()
        self._load_file(file_path)

    def _load_file(self, file_path):
        """
        Opens the given file and populates the word_set attribute with words from the file.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                word = line.rstrip("\n").lower()
                if word:
                    self.word_set.add(word)

    def is_valid_word(self, word: str):
        """
        Checks if a given word is valid.
        """
        return word.lower() in self.word_set

    def is_anagram(self, word1: str, word2: str):
        """
        Compares 2 words and checks if they're anagrams.
        """
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word: str):
        """
        Returns a list of anagrams of a given word.
        """
        word = word.lower()

        return [
            anagram
            for anagram in self.word_set
            if anagram != word and self.is_anagram(word, anagram)
        ]
