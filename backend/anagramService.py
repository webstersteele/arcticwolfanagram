import anagramStore

class AnagramService:
    def __init__(self, anagramStore):
        self.anagramStore = anagramStore

    def isAnagram(self, word1, word2):
        word1Compare = ''.join(e for e in word1.lower() if e.isalnum())
        word2Compare = ''.join(e for e in word2.lower() if e.isalnum())

        if len(word1Compare) == len(word2Compare):
            charsInWord1 = dict()
            
            for chr in word1Compare:
                count = 1
                if chr in charsInWord1:
                    count += charsInWord1[chr]
                charsInWord1[chr] = count
            
            for chr in word2Compare:
                count = -1
                if chr in charsInWord1:
                    count += charsInWord1[chr]
                charsInWord1[chr] = count
            
            #.values() returns a dictionary view, not a list in python3, 
            # so its quicker to check manually then convert to a list and use np.any()
            for i in charsInWord1.values():
                if(i!=0):
                    return False
            
            self.anagramStore.addAnagram(word1, word2)
            return True
        
        return False



