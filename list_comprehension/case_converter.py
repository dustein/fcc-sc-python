def convert_to_snake_case(pascal_or_camel_cased_string):
  # snake_cased_char_list = []
  # for char in pascal_or_camel_cased_string:
  #   if char.isupper():
  #     converted_character = '_' + char.lower()
  #     snake_cased_char_list.append(converted_character)
  #   else:
  #     snake_cased_char_list.append(char)
  
  # snake_cased_string = ''.join(snake_cased_char_list)
  # clean_snake_cased_string = snake_cased_string.strip('_')
  # return snake_cased_string
  snake_cased_char_list = [
    #Python will interpret this expression as "append '_' + char.lower() to the list if char is in uppercase" and this will convert the case for the capital letters in the input string.
    '_' + char.lower() if char.isupper()
    else char
    #The final piece of the puzzle is the input string itself. The list comprehension needs to know about the object it'll iterate upon. In this case, you need to iterate upon all the characters of the string.
    for char in pascal_or_camel_cased_string
  ]
  return ''.join(snake_cased_char_list).strip('_')


def main():
  return convert_to_snake_case('aLongAndComplexString')
#Before running the main() function, you need to make sure that the file is running as a script. Add an if statement on the same level as the two existing functions and check whether __name__ == '__main__' evaluates to True or not.

if __name__ == "__main__":
  print(main())