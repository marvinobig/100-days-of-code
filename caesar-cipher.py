from art import logo

print(logo)

def cipher(original_text, shift_amount, alphabet_list, encode_or_decode):
    original_text_list = [char for char in original_text]
    cipher_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text_list:
        if char in alphabet_list:
            cipher_index = alphabet_list.index(char) + shift_amount
            cipher_text += alphabet_list[cipher_index] if cipher_index < len(alphabet_list) else alphabet_list[cipher_index - len(alphabet_list)]
        else:
            cipher_text += char

    return cipher_text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop = False

while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(cipher(text, shift, alphabet, direction))

    confirmation = input("Do you want to run another message through the cipher? (yes/no)").lower()

    stop = confirmation in ["n", "no"]