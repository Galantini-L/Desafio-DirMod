"""
#  DirMod Challenge  #
Author: Lautaro Galantini

"""
LETTER_COMBINATIO = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def letter_combination(letter:str):
    """ Get the letter of the user and search in what number is.

    Arguments:
        letter {str} -- The letter that the user input

    Returns:
        {str} -- The numbers of times that a keynumber has to be presset to show the letter
    """
    for key, value in LETTER_COMBINATIO.items():
        if letter in value:
            position = value.find(letter) + 1
            return key * position

def words_combination (word:str):
    """Apply letter_combination for each word. Apply a pause (whitespace) if the letter is in the same
    number that the letter before.

    Arguments:
        word {str} -- words passed by the user

    Returns:
        {str} -- words into one string
    """
    words_comb = list(map(letter_combination, word))
    for i, v in enumerate(words_comb):
        if i + 1 != len(words_comb) and words_comb[i+1][0] == v[-1]:
            words_comb[i] += ' '
    return ''.join(words_comb)


def main():
    while True:
        print('Typpe a text and will get the numbers:')
        user_input = input()
        if user_input == '000':
            break
        word = user_input.split()
        combination_input = list(map(words_combination,word))
        print('\n','0'.join(combination_input),'\nTyppe "000" if you want exit\n')

if __name__ == "__main__":
    main()
