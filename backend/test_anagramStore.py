import unittest

import anagramStore

class TestAnagramStore(unittest.TestCase):
    
    def setUp(self):
        self.dct = dict()
        
        self.dct[('listen', 'silent')] = 2
        self.dct[('flow', 'wolf')] = 3
        self.dct[('state', 'taste')] = 1
    
    def test_addDict(self):
        dctCopy = dict(self.dct)
        
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        anagramStoreTest.addAnagram('cider', 'cried')
        
        self.assertEqual(dctCopy[('cider', 'cried')], 1)
        
        anagramStoreTest.addAnagram('cider', 'cried')
        
        self.assertEqual(dctCopy[('cider', 'cried')], 2)
        
        anagramStoreTest.addAnagram('cried', 'cider')
        
        self.assertEqual(dctCopy[('cider', 'cried')], 3)
    
    def test_updateDict(self):
        dctCopy = dict(self.dct)
        
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        anagramStoreTest.addAnagram('state', 'taste')
        
        self.assertEqual(dctCopy[('state', 'taste')], 2)
        
        anagramStoreTest.addAnagram('wolf', 'flow')
        
        self.assertEqual(dctCopy[('flow', 'wolf')], 4)
    
    def test_getFrequentMoreThenDict(self):
        dctCopy = dict(self.dct)
        
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        expectedReturnValue = [
            {'words': ('flow', 'wolf'),
            'frequency': 3},
            {'words': ('listen', 'silent'),
            'frequency': 2},
            {'words': ('state', 'taste'),
            'frequency': 1},
        ]
        
        actualReturnValue = anagramStoreTest.getMostFrequent(10)
        
        self.assertEqual(expectedReturnValue, actualReturnValue)
        
    def test_getFrequentSameAsDict(self):
        dctCopy = dict(self.dct)
    
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        expectedReturnValue = [
            {'words': ('flow', 'wolf'),
            'frequency': 3},
            {'words': ('listen', 'silent'),
            'frequency': 2},
            {'words': ('state', 'taste'),
            'frequency': 1},
        ]
        
        actualReturnValue = anagramStoreTest.getMostFrequent(3)
        
        self.assertEqual(expectedReturnValue, actualReturnValue)
    
    def test_getFrequentLessThenDict(self):
        dctCopy = dict(self.dct)
    
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        expectedReturnValue = [
            {'words': ('flow', 'wolf'),
            'frequency': 3},
            {'words': ('listen', 'silent'),
            'frequency': 2}
        ]
        
        actualReturnValue = anagramStoreTest.getMostFrequent(2)
        
        self.assertEqual(expectedReturnValue, actualReturnValue)
        
    def test_getFrequentZero(self):
        dctCopy = dict(self.dct)
    
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        expectedReturnValue = []
        
        actualReturnValue = anagramStoreTest.getMostFrequent(0)
        
        self.assertEqual(expectedReturnValue, actualReturnValue)
        
if __name__ == '__main__':
    unittest.main()
        
        