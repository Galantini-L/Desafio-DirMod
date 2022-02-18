import unittest
from desafio_DirMode import letter_combination, words_combination


class TestDesafio(unittest.TestCase):

    def setUp(self):

        def list_word(self,inputWord:str):
            self.word_s = inputWord.split()
            self.listWord = '0'.join(list(map(words_combination,self.word_s)))
            return self.listWord

        self.example1 = list_word(self,'foo bar')
        self.example2 = list_word(self,'hello world')
        self.example3 = list_word(self,'hello dirmod')

    def test_letter_combination(self):
         self.assertEqual(letter_combination('h'), '44')
         self.assertEqual(letter_combination('i'), '444')
         self.assertEqual(letter_combination('y'), '999')
         self.assertEqual(letter_combination('e'), '33')
         self.assertEqual(letter_combination('s'), '7777')
        

    def test_words_combination(self):
        self.assertEqual(words_combination('hi'),'44 444')
        self.assertEqual(words_combination('yes'),'999337777')
        self.assertEqual(self.example1,'333666 666022 2777')
        self.assertEqual(self.example2,'4433555 555666096667775553')
        self.assertEqual(self.example3,'4433555 555666034447776 6663')




if __name__ == '__main__':
    unittest.main()