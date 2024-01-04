def main():
  # pass
  card_number = "4111-1111-4555-1142"
  card_translation = card_number.maketrans({'-': '', ' ':''})
  translated_card_number = card_number.translate(card_translation)
  print(translated_card_number)

main()