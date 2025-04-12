from lists import VINEGRE_TABLE, ALPHABET

def encode_message(message, key):
    ciphertxt = []
    key_index = 0
    for character in message:
        if key_index == len(key):
            key_index = 0
        key_letter = ALPHABET.index(key[key_index])

        if character.isalpha():
            ciphertxt.append(VINEGRE_TABLE[key_letter][ALPHABET.index(character)])
            key_index = key_index + 1
        else:
            ciphertxt.append(character)

    ciphertext = "".join(ciphertxt)
    return ciphertext