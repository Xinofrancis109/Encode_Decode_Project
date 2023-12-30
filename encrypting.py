alphabets = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode():
    text = input("Message to encode: ")
    shift = int(input("Shifts: "))
    shift = shift % len(alphabets)  # Correcting the shift value
    print(shift)
    cipher_text = ''
    for i in text:
        if i in alphabets:
            new_position = (alphabets.index(i) + shift) % len(alphabets)  # Correcting the index calculation
            new_text = alphabets[new_position]
            cipher_text += new_text
        else:
            cipher_text += i
    print(cipher_text)


def decode():
    text = input("Message to Decode: ")
    shift = int(input("Shifts: "))
    shift = shift % len(alphabets)
    cipher_text = ''
    for i in text:
        if i in alphabets:
            new_position = (alphabets.index(i) - shift) % len(alphabets)
            new_text = alphabets[new_position]
            cipher_text += new_text
        else:
            cipher_text += i
    print(cipher_text)


print("Welcome to Coding class")


def cryption():
    prompt = input('Do you want to encode or decode? ').lower()
    if prompt == 'encode':
        encode()
    elif prompt == "decode":
        decode()


cryption()

prompt2 = input("Will you like to try again? Y/N ").upper()
if prompt2 == "Y":
    cryption()
elif prompt2 == "N":
    print("Goodbye")
else:
    cryption()
