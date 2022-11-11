alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cypher_direction):
    end_text=""
    if cypher_direction == 'decode':
        shift_amount *= -1
    for i in start_text:
        if i not in alphabet:
            end_text+= i
            continue
        position = alphabet.index(i)
        new_position = position + shift_amount 
        end_text += alphabet[new_position]
    print(f"Here is the {cypher_direction}d result: {end_text}\n")

from art import logo, greeting

status = 'yes'

while status == 'yes':
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        remainder = shift % 26
        shift = remainder
    caeser(start_text = text, shift_amount = shift, cypher_direction = direction)
    status = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if status == 'no':
        print(greeting)
        break


