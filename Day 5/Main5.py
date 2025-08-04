import random

print("Welcome to the PyPassword Geneerator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like? \n"))

select_letters = ''
for repeat in range(0,nr_letters):
    select_letters +=" "+ random.choice(letters)

final_letters=select_letters.split( )


select_num = ''
for repeat in range(0,nr_numbers):
    select_num +=" " + random.choice(numbers)

final_num = select_num.split()

select_sym = ''
for repeat in range(0,nr_symbols):
    select_sym += ' ' + random.choice(symbols)

final_sym = select_sym.split()

final_sum= final_sym + final_letters + final_num

final_passwd =''
for n in range(0,len(final_sum)):
    final_passwd+= random.choice(final_sum)
print(f"Your final password is: {final_passwd}")

