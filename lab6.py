# Matthew Cardenas

# encoder & decoder functions
def encoder(passw):
    encoded_passw = ''

    for num in passw:
        val = int(num)
        # nums that would overflow -7
        if val >= 7:
            val -= 7
        # rest +3
        else:
            val += 3
        encoded_passw += str(val)
    return encoded_passw


def decoder(encoded_passw):
    # your code here
    pass


# main loop for menu
while True:

    # print menu
    print('Menu')
    print('-' * 13)
    print("1. Encode\n2. Decode\n3. Quit\n")
    menu_choice = int(input("Please enter an option: "))

    # encode option chosen
    if menu_choice == 1:

        # encodes & saves password
        encoded_password = encoder(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!\n")

    # decode option chosen
    if menu_choice == 2:

        # decodes and prints original password
        print(f"The encoded password is {encoded_password}, and the original password is ", end='')
        print(decoder(encoded_password), end=".\n\n")

    #quit option chosen 
    if menu_choice == 3:
        break
