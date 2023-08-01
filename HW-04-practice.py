''' Списки. Практика 31/07/2023 '''

''' Автоперевірка. Задача 07/14. Визначення відстані польоту дрону'''

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }

# def calculate_distance(coordinates):
#     if len(coordinates) == 0:        #Якщо відстань між точками 0, повертаємо 0. 
#         return 0
#     result = 0
#     for iterator in range(len(coordinates)):
#         #print(coordinates[(coordinates[iterator], coordinates[iterator+1])])
        
#         try:
#             result += points[(coordinates[iterator], coordinates[iterator+1])]
#         except KeyError:
#             result += points[(coordinates[iterator+1], coordinates[iterator])]

#     return result

''' Автоперевірка. Задача 08/14. Накопичення енергії гравця'''

def game(terra, power):
    #print(terra)
    #print(power)
    for i in range(len(terra)): 










# def best_fit_line(data):
# list_x = list()
# list_y = list()

# for coord in data:
#     list_x.append(coord[0])
#     list_y.append(coord[1])

# data = list()

''' Азбука Морзе '''

# morze_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
#               'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
#               'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
#               'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
#               'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
#               '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
#               '8':'---..', '9':'----.'}

# def convert_to_morze(text):
#     text = text.upper()
#     result = list()
#     for char in text:
#         if char in morze_dict:
#             result += morze_dict.get(char) + ' '
#     return result[:1]

# def convert_to_morze(text):
#     text = text.upper()
#     result = list()
#     for char in text:
#         if char in morze_dict:
#             result.append(morze_dict.get(char))
#     return ' '.join

# from random import randrange

# def create_deck():
#     svits = ['s', 'h', 'd', 'c']
#     values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#     deck = list()
#     for svit in svits:
#         for value in values:
#             deck.append(f'{value}{svit}')
#     return deck

# #print(create_deck())

# def shuffle_deck(deck):
#     new_deck = deck.copy()
#     for i in range(0, len(deck)):
#         other_index = randrange(0, len(new_deck))
#         new_deck[i], new_deck[other_index] = new_deck[other_index], new_deck[i]
#         return new_deck
    
# #print(shuffle_deck(new_deck))

# def deal(players, cards, deck):
#     if player * cards > len(deck):
#         return deck
    
#     table = list()

#     for _ in range(0, cards):
#         for player in range(0, players):
#             if player >= len(table):
#                 table.append([deck.pop()])
#             else:
#                 table[player].append(deck.pop())
#     return table

# def main(players, cards):
#     init_deck = create_deck()
#     print(f'Open new deck: {init_deck}')

#     deck = shuffle_deck(init_deck)

#     print(f'Shuffle deck')


# from pathlib import Path
# import sys

# p = Path(sys.argv[1])

# def parse_folder(path):
#     for elements in path.iterdir():
#         if elements.is_dir():
#             print(f'Parse folder: This is folder - {elements.name}')
#         if elements.is_fike():
#             print(f'Parse folder: This is file - {elements.name}')

# def parse_folder_recursion():
#     for elements in path.iterdir():
#         if elements.is_dir():
#             parse_folder_recursion(elements)
#         else:
#             print(f'parse file: This is file - {elements.name}')


''' Гра Hangman '''

# hangman_pics = [
#     """
#       +---+
#           |
#           |
#           |
#          ===""",
#     """
#       +---+
#       O   |
#           |
#           |
#          ===""",
#     """
#       +---+
#       O   |
#       |   |
#           |
#          ===""",
#     """
#       +---+
#       O   |
#      /|   |
#           |
#          ===""",
#     """
#       +---+
#       O   |
#      /|\  |
#           |
#          ===""",
#     """
#       +---+
#       O   |
#      /|\  |
#      /    |
#          ===""",
#     """
#       +---+
#       O   |
#      /|\  |
#      / \  |
#          ==="""
# ]

# words = ['python', 'poker', 'programing', 'sunflower', 'Ukraine']

# attemps = 6
# guessed = list()
# def print_word():
#     display_word = ''
#     for char in words:
#         display_word += str(char if char in guessed else '_')

#     print(display_word)
#     return display_word

# while attemps > 0:
#     print(hangman_pics[6 - attemps])
#     display_word = print_word()

#     if '_' not in display_word:
#         print(f'Congratulation! You win this game and still alive. The guessed word was {word}')
#         break
#     guess = input('Guess a letter: ').upper()

#     if quess in guessed:
#         print(f'You already guessed this letter')
#     elif guess in word:
#         print






