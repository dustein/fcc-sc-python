# import random
import re
import secrets
import string

# def generate_password(length, nums, special_chars, uppercase, lowercase):
#   digits = string.digits
#   symbols = string.punctuation
#   letters = string.ascii_letters

#   all_characters = digits+symbols+letters
#   while True:
#     password = ''
#     #Generate password
#     # for i in range(length):
#     #A standalone single underscore is used to represent a value you don't care or that won't be used in your code. Your iteration variable is not actually used.
#     for _ in range(length):
#       password += secrets.choice(all_characters)
    
#     constraints = [
#       # (nums, '[0-9]'),
#       (nums, r'\d'),
#       (lowercase, r'[a-z]'),
#       (uppercase, r'[A-Z]'),
#       # (special_chars, r'[^a-zA-Z0-9]')
#       (special_chars, fr'{symbols}')
#       ]
    
#   #Check constraits
#     # count = 0
#     # for constrain, pattern in constraints:
#     #   if constrain <= len(re.findall(pattern, password)):
#     #     count += 1
#     #   if count == 4:
#     #     break
#     if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
#       break

#   return password

# # pattern = re.compile('l')
# # texto = 'Not all those who wander are lost.'
# # print(pattern.search(texto))
# pattern = 'l+'
# texto = 'Not all those who wander are lost.'
# # print(re.search(pattern, texto))
# print(re.findall(pattern, texto))

# patter_raw = r'itens'

#------------------
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
   
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
# new_password = generate_password(8, 1, 1, 1, 1)
# new_password = generate_password(length=8, nums=1, special_chars=1, uppercase=1, lowercase=1)
# print(random.choice(all_characters))
# new_password = generate_password()
# print('Generated pasword:', new_password)
if __name__ == '__main__':
  new_password = generate_password()
  print('Generated pasword:', new_password)