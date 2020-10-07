import itertools

class AnagramStore:
    def __init__(self, anagramStore):
        self.anagramStore = anagramStore

    def addAnagram(self, word1, word2):
        ##Sorting legigraphically will increase runtime for long anagrams, but checking both orders is constant time
        frequency = 1
        if (word1, word2) in self.anagramStore:
            frequency += self.anagramStore[(word1, word2)]
            self.anagramStore[(word1, word2)] = frequency
        elif (word2, word1) in self.anagramStore:
            frequency += self.anagramStore[(word2, word1)]
            self.anagramStore[(word2, word1)] = frequency
        else:
            self.anagramStore[(word1, word2)] = frequency


    def getMostFrequent(self, num):
        sortedAnagrams = {k: v for k, v in sorted(self.anagramStore.items(), key=lambda item: item[1], reverse=True)}
        if(len(self.anagramStore) < num):
            return self.prettyPrintAnagram(sortedAnagrams.items())
        else:
            return self.prettyPrintAnagram(itertools.islice(sortedAnagrams.items(), num))
        
    def prettyPrintAnagram(self, iterator):
        lst = list()
        for i in iterator:
            lst.append({
                "words": i[0],
                "frequency": i[1]    
            })
        return lst