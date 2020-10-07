import unittest

import anagram

class TestAnagramMethods(unittest.TestCase):
    
    def test_anagram(self):
        #base/short cases
        self.assertTrue(anagram.isAnagram('', ''))
        self.assertTrue(anagram.isAnagram('a', 'a'))
        
        #medium length words
        self.assertTrue(anagram.isAnagram('wolf', 'flow'))
        self.assertTrue(anagram.isAnagram('restful', 'fluster'))
        self.assertTrue(anagram.isAnagram('knee', 'keen'))
        self.assertTrue(anagram.isAnagram('knee', 'knee'))
        
        #medium length with spaces/capitals/punctuation
        self.assertTrue(anagram.isAnagram('Dormitory', 'Dirty Room'))
        self.assertTrue(anagram.isAnagram('The eyes', 'they See'))
        self.assertTrue(anagram.isAnagram('they See', 'The eyes'))
        self.assertTrue(anagram.isAnagram('they See', 'they See......'))
        
        #long anagrams with spaces, capitals and punctuation
        str1 = "To be or not to be: that is the question; whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune..."
        str2 = "In one of the Bard's best-thought-of tragedies our insistent hero, Hamlet, queries on two fronts about how life turns rotten."     
        self.assertTrue(anagram.isAnagram(str1, str2))
        
        str1 = "To be or not to be: that is the question; whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and by opposing, end them?"
        str2 = " Is a befitting quote from one of Shakespeare's greatest tragedies. But why won't Hamlet's inspiring motto toss our stubborn hero's tortuous battle for life, on one hand, and death, on another?"
        self.assertTrue(anagram.isAnagram(str1, str2))
        
        #wrong length
        self.assertFalse(anagram.isAnagram('wolf', 'floww'))
        self.assertFalse(anagram.isAnagram('restfulw', 'fluster'))
        
        #wrong characters
        self.assertFalse(anagram.isAnagram('wolf', 'flew'))
        self.assertFalse(anagram.isAnagram('restful', 'bluster'))
        
if __name__ == '__main__':
    unittest.main()
        
        