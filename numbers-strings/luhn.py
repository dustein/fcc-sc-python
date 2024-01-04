def main():
  # pass
  card_number = "4111-1111-4555-1142"
  card_translation = card_number.maketrans({'-': '', ' ':''})
  translated_card_number = card_number.translate(card_translation)
  print(f'translated_card_number: {translated_card_number}')
  return translated_card_number

def verify_card_number(card_number):
  sum_of_odd_digits = 0
  #do indice -1 ate -5 em ordem tras pra frente
  # card_number_reversed = card_number[-1:-5:-1]
  card_number_reversed = card_number[::-1]
  odd_digits = card_number_reversed[::2]
  print(f'card-number-reversed: {card_number_reversed}')
  for digits in odd_digits:
    print(digits)

main()
verify_card_number(main())