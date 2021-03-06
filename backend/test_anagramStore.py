import unittest

import anagramStore

class TestAnagramStore(unittest.TestCase):
    
    def test_addDict(self):
        dct = dict()
        dct[('listen', 'silent')] = 2
        dct[('flow', 'wolf')] = 3
        dct[('state', 'taste')] = 1
        dctCopy = dict(dct)
        
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        anagramStoreTest.addAnagram('cider', 'cried')
        
        self.assertEqual(dctCopy[('cider', 'cried')], 1)
        
        anagramStoreTest.addAnagram('cider', 'cried')
        
        self.assertEqual(dctCopy[('cider', 'cried')], 2)
        
        anagramStoreTest.addAnagram('cried', 'cider')
        
        self.assertEqual(dctCopy[('cider', 'cried')], 3)
    
    def test_updateDict(self):
        dct = dict()
        dct[('listen', 'silent')] = 2
        dct[('flow', 'wolf')] = 3
        dct[('state', 'taste')] = 1
        dctCopy = dict(dct)
        
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        anagramStoreTest.addAnagram('state', 'taste')
        
        self.assertEqual(dctCopy[('state', 'taste')], 2)
        
        anagramStoreTest.addAnagram('wolf', 'flow')
        
        self.assertEqual(dctCopy[('flow', 'wolf')], 4)
    
    def test_getFrequentMoreThenDict(self):
        dct = dict()
        dct[('listen', 'silent')] = 2
        dct[('flow', 'wolf')] = 3
        dct[('state', 'taste')] = 1
        dctCopy = dict(dct)
        
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
        dct = dict()
        dct[('listen', 'silent')] = 2
        dct[('flow', 'wolf')] = 3
        dct[('state', 'taste')] = 1
        dctCopy = dict(dct)
    
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
        dct = dict()
        dct[('listen', 'silent')] = 2
        dct[('flow', 'wolf')] = 3
        dct[('state', 'taste')] = 1
        dctCopy = dict(dct)
    
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
        dct = dict()
        dct[('listen', 'silent')] = 2
        dct[('flow', 'wolf')] = 3
        dct[('state', 'taste')] = 1
        dctCopy = dict(dct)
    
        anagramStoreTest = anagramStore.AnagramStore(dctCopy)
        
        expectedReturnValue = []
        
        actualReturnValue = anagramStoreTest.getMostFrequent(0)
        
        self.assertEqual(expectedReturnValue, actualReturnValue)
        
if __name__ == '__main__':
    unittest.main()
        
        