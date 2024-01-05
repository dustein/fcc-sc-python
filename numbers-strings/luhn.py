
def verify_card_number(card_number):
  sum_of_odd_digits = 0
  # do indice -1 ate -5 em ordem tras pra frente
  # card_number_reversed = card_number[-1:-5:-1]
  card_number_reversed = card_number[::-1]
  odd_digits = card_number_reversed[::2]
  print(f'card-number-reversed: {card_number_reversed}')
  print(f'odd_digits: {odd_digits}')
  
  for digit in odd_digits:
    sum_of_odd_digits += int(digit)

  print(f'sum_of_odd_digits: {sum_of_odd_digits}')
  sum_of_even_digits = 0
  even_digits = card_number_reversed[1::2]
  print(f'even_digits: {even_digits}')
  for digits in even_digits:
    number = int(digits)*2
    print(number)
    if number >= 10:
      print(f'even numero maior que dez: {number}')
      number = number//10 + number%10
    sum_of_even_digits += number
    
  print(f'sum_of_even_dgits: {sum_of_even_digits}')

  total = sum_of_odd_digits + sum_of_even_digits
  print(f'Total: {total}')

  return 0 == total % 10

  if verify_card_number:
    print('VALID!')
  else:
    print('INVALID')

def main():
  card_number = "4111-1111-4555-1142"
  card_translation = card_number.maketrans({'-': '', ' ':''})
  translated_card_number = card_number.translate(card_translation)

  print(f'print translated_card_number: {translated_card_number}')

  if verify_card_number(translated_card_number):
    print('VALID!')
  else:
    print('INVALID!')

main()