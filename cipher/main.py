from alphabet import a_z as letters


def caesar(start_text, shift_number, cipher_directon):
    end_text = ""
    if cipher_directon == "decode":
        shift_number *= -1
    for char in start_text:
        if char in letters:
            position = letters.index(char)
            new_position = position + shift_number
            end_text += letters[new_position]
        else:
            end_text += char
    print(f"Your {cipher_directon}d text is {end_text}")


again = True
while again:
    direction = (input("Enter encode to encrpt. Decode to decrpt \n")).lower()
    text = (input("Enter text \n")).lower()
    shift = int(input("Enter shift number \n"))
    shift %= 26

    caesar(start_text=text, shift_number=shift, cipher_directon=direction)

    result = str(input("Do you to run the program again? :"))
    if result == "no":
        again = False
        print("Goodbyeee")
