text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    key_index = 0

    for char in message.lower():
        if char == ' ':
            #Append space to the message
            final_message += char
        else:
            #Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            #Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

encryption = vigenere(text, custom_key)
decryption = vigenere(encryption, custom_key, -1)
print(encryption)
print(decryption)