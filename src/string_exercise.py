class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        input_str = input_str[::-1]
        return input_str

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if( character in l):
            return True
        return False

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        l = text.split(" ")
        lens = list(map(lambda i: len(i), l))
        return lens

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        l = sentence.split(" ")
        lens = self.get_word_lengths(sentence)
        max_len = max(lens)
        max_index = lens.index(max_len)
        return l[max_index]