#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
sum = 0
print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n")) 
sum+=nr_letters

nr_symbols = int(input(f"How many symbols would you like?\n"))
sum+=nr_symbols

nr_numbers = int(input(f"How many numbers would you like?\n"))
sum+=nr_numbers

#52 letters
#10 numbers
#9 symbols

random_letters = []
for letter in range(0, nr_letters):
    random_index1 = random.randint(0,len(letters))
    random_letters.append(letters[random_index1])


random_symbols = []
for symbol in range(0, nr_symbols):
    random_index2 = random.randint(0,len(symbols))
    random_symbols.append(symbols[random_index2])


random_numbers= []
for number in range(0, nr_numbers):
    random_index3 = random.randint(0,len(numbers))
    random_numbers.append(numbers[random_index3])


password = ''
chars = random_letters + random_symbols + random_numbers
random.shuffle(chars)
for x in chars:
    password+=x
print(password)

    
 