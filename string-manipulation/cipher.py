text = 'mrttaqrhknsw ih puggrur'
# custom_key = 'python'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    key_index = 0

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
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

def encrypt(message, key):
    #The pass keyword can be used as a placeholder for future code. It does not have any effect in your code but it can save you from errors you would get in case of incomplete code
    pass
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

encryption = encrypt(text, custom_key)
decryption = decrypt(text, custom_key)
print(f'criptografada: \n{encryption}')
print(f'Key: {custom_key}')
# print("decifrada: " + decryption)
print(f'decifrada: \n{decryption}')