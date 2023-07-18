class Anagram:
    def __init__(self, word):
        self.word=word
        self.sorted_word=sorted(word.lower())

    def match(self, candidates):
        correct_anagrams = []

        for candidate in candidates:
            if sorted(candidate.lower()) == self.sorted_word and candidate.lower() != self.word.lower():
                correct_anagrams.append(candidate)
    
        return correct_anagrams 

anagram_finder = Anagram('listen')
candidates = ['enlist', 'google', 'inlets', 'banana']
results = anagram_finder.match(candidates)
print(results)
