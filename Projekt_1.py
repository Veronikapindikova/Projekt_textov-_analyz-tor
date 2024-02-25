"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Veronika Pindíková
email: veronika.pindikova@gmail.com
discord: Veronika77
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
part1 = TEXTS[0]
words = part1

Username = ["Bob", "Ann", "Mike", "Liz"]
Password = ["123", "pass123", "password123", "pass123"]

users = dict(zip(Username, Password))  

Username = input("Username:")
Password = input("Password:")

USERS = users.get(Username)
if USERS == Password:
    print("-"*45)
    input("Welcome to the app "+ Username +".")
    input("We have 3 texts to be analyzed." )             
    print("-"*45)
else:
    print("unregistred user, determinating program.,")
    exit()
for index, text in enumerate(TEXTS, start=1):
    print(index, text)         
    print("-"*45)
enter = (input("Enter a number btw. 1 and 3 to select:"))
print("-"*45)
try:
    cislo =int(enter)
except ValueError:
    print("-"*45)
    print("Invalid number or character, determinatig program...")
    print("-"*45)
    exit()
if int(enter)> 3 or int(enter) < 1:
    print("-"*45)
    print("Wrong number, choose between 1-3, determinating program...")  
    print("-"*45)
    exit()
if int(enter) == 2 or int(enter) == 3:
    exit()
if int(enter) == 1:   
        part1 = TEXTS[0]
        words = part1.split()  
        word_count = len(words)
        print(f"There are {word_count} words in the selected text.")        
        uppercase_words = []
for word in words:
    if word.isupper() and not any(character.isdigit() for character in word):
        uppercase_words.append(word)
        number_of_uppercase_words = sum (1 for upperword in uppercase_words if upperword.isupper())
        print(f"There are {number_of_uppercase_words} uppercase words.")
        number_of_title_letters= sum (1 for titleword in words if titleword.istitle())
        print(f"There are {number_of_title_letters} titlecase words.")
        number_of_lower_letters = sum (1 for lowerword in words if lowerword.islower())
        print(f"There are {number_of_lower_letters} lowercase words.")
        count_of_number = sum (1 for number in words if number.isdigit())
        print(f"There are {count_of_number} numeric strings.")
        count_of_numbers = [int(numbers) for numbers in words if numbers.isdigit()]
        sum_of_numbers = sum(count_of_numbers)
        print(f"The sum of all the numbers: {sum_of_numbers}")            

if int(enter) == 1:
    part1 = TEXTS[0]
    text1 = part1
def analyze_text(text1):   
    words1 = text1.split()  
    word_lengths = {}  
    for word1 in words1:
        cleaned_word = word1.strip(".,!?\"'()[]{}")
        word_length = len(cleaned_word)
        if word_length in word_lengths:
            word_lengths[word_length] += 1
        else:
            word_lengths[word_length] = 1            
    print("-" * 45)
    print(f"LEN:|\t OCCURENCES\t|NR. ") 
    print("-" * 45)       
    for length, frequency in sorted(word_lengths.items()):
        print(f"{length:^4}|{"*"*frequency:12}\t|{frequency:}")         
input_text = text1
analyze_text(input_text)
