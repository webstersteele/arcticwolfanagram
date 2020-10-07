import anagramStore
import anagramService

#Defining the default classes needed

_anagramStoreDict = dict()

anagramStore = anagramStore.AnagramStore(_anagramStoreDict)

anagramService = anagramService.AnagramService(anagramStore)