import unittest

import anagramService
import anagramStore

class TestAnagramMethods(unittest.TestCase):
    def test_anagram(self):
        dct = dict()
        anagramStoreTest = anagramStore.AnagramStore(dct)
        
        anagramServiceTest = anagramService.AnagramService(anagramStoreTest)
        
        #base/short cases
        self.assertTrue(anagramServiceTest.isAnagram('', ''))
        self.assertTrue(anagramServiceTest.isAnagram('a', 'a'))
        
        #medium length words
        self.assertTrue(anagramServiceTest.isAnagram('wolf', 'flow'))
        self.assertTrue(anagramServiceTest.isAnagram('restful', 'fluster'))
        self.assertTrue(anagramServiceTest.isAnagram('knee', 'keen'))
        self.assertTrue(anagramServiceTest.isAnagram('knee', 'knee'))
        
        #medium length with spaces/capitals/punctuation
        self.assertTrue(anagramServiceTest.isAnagram('Dormitory', 'Dirty Room'))
        self.assertTrue(anagramServiceTest.isAnagram('The eyes', 'they See'))
        self.assertTrue(anagramServiceTest.isAnagram('they See', 'The eyes'))
        self.assertTrue(anagramServiceTest.isAnagram('they See', 'they See......'))
        
        #long anagrams with spaces, capitals and punctuation
        str1 = "To be or not to be: that is the question; whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune..."
        str2 = "In one of the Bard's best-thought-of tragedies our insistent hero, Hamlet, queries on two fronts about how life turns rotten."     
        self.assertTrue(anagramServiceTest.isAnagram(str1, str2))
        
        str1 = "To be or not to be: that is the question; whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and by opposing, end them?"
        str2 = " Is a befitting quote from one of Shakespeare's greatest tragedies. But why won't Hamlet's inspiring motto toss our stubborn hero's tortuous battle for life, on one hand, and death, on another?"
        self.assertTrue(anagramServiceTest.isAnagram(str1, str2))
        
        #wrong length
        self.assertFalse(anagramServiceTest.isAnagram('wolf', 'floww'))
        self.assertFalse(anagramServiceTest.isAnagram('restfulw', 'fluster'))
        
        #wrong characters
        self.assertFalse(anagramServiceTest.isAnagram('wolf', 'flew'))
        self.assertFalse(anagramServiceTest.isAnagram('restful', 'bluster'))
        
if __name__ == '__main__':
    unittest.main()
        
        