from language_tools import LanguageHelper
import unittest

# We define the custom lexicon that we will use for our controlled tests
sample = ('car', 'cat', 'Cate', 'cater', 'care',
          'cot', 'cute', 'dare', 'date', 'dog', 'dodge',
          'coffee', 'pickle', 'grate','Missouri','Blech','bleach','weird','wired','Rome','unnecessary','some','written','agate','ate','bate','date','fate','Gabe',
          'grate','hate','kate','late','mate','nate','pate','rate','sate','tate','yate','bom','com','Dom','Hom','Kum','mom','Nom','Pom','Rom','Tom','Yom'
          ,'Pate','Sate','Tate','Yate','gate','Rome','brome','come','crome','dome','drome','frome','home','krome', 'mome','nome','pome',
          'rame','rime','robe','rode', 'roe','roke','role', 'rone','rope','rose','rote','roue','rove','ryme','some','tome','wield', 'wird')

rhymesWithDog = ('bog', 'cog', 'clog', 'fog', 'frog', 'hog', 'log','Blech','cat')


class BasicTest(unittest.TestCase):
  
    # make sure that all the words in the lexicon are recognized
    def testContainment(self):
        helper = LanguageHelper(sample)
        for w in sample:
            self.assertTrue(w in helper)
  
    def testFailures(self):
        helper = LanguageHelper(sample)
        self.assertFalse('cate' in helper)     # only allowed when capitalized
        self.assertFalse('fox' in helper)      # word is not there
        self.assertFalse('cofee' in helper)    # mis-spell word is not there

    def testSuggestInsertion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('pikle'), ['pickle'])
        self.assertEqual(helper.getSuggestions('ct'), ['cat','cot'])
        self.assertEqual(helper.getSuggestions('writen'), ['written'])

    def testSuggestDeletion(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('gratle'), ['grate'])
        self.assertEqual(helper.getSuggestions('unneccessary'), ['unnecessary'])

    def testSugeestionsMany(self):
        helper = LanguageHelper(rhymesWithDog)
        self.assertEqual(helper.getSuggestions('rog'), ['bog','cog','fog','frog','hog','log'])

    def testSugeestionsCapitalization(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('Gate'), ['Agate','Ate','Bate','Cate','Date','Fate','Gabe','Grate','Hate','Kate','Late','Mate','Nate','Pate','Rate','Sate','Tate','Yate','gate'])
        self.assertEqual(helper.getSuggestions('missouri'), ['Missouri'])
        
    def testSuggestionsNone(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('Blech'), [])
        self.assertEqual(helper.getSuggestions('cat'), [])

    def test_Swap_letters(self):
         helper = LanguageHelper(sample)
         self.assertEqual(helper.getSuggestions('wierd'), ['weird', 'wield', 'wird', 'wired'])

    def test_case_sensitvity(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('rome'), ['Rome','brome','come','crome','dome','drome','frome','home','krome', 'mome','nome','pome',
                                                         'rame','rime','robe','rode', 'roe','roke','role', 'rone','rope','rose','rote','roue','rove','ryme','some','tome'])
        self.assertEqual(helper.getSuggestions('soMe'), ['some'])
        self.assertEqual(helper.getSuggestions('SOME'), ['some'])
        self.assertEqual(helper.getSuggestions('Some'), ['Come', 'Dome', 'Home', 'Mome', 'Nome', 'Pome', 'Rome', 'Tome', 'some'])

    def test_non_english_words(self):
        helper = LanguageHelper(sample)
        self.assertEqual(helper.getSuggestions('Kom'), ['Bom','Com','Dom','Hom','Kum','Mom','Nom','Pom','Rom','Tom','Yom'])
         

if __name__ == '__main__':
    unittest.main()
