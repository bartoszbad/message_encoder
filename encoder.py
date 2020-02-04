from functions import decode_message, encode_message

choice = 0
print(
    """
    If you would like to encode message: type 1
    If you would like to decode message: type 2
    If you would like to exit: type 3
    """)

while choice != 3:
    choice = int(input("Your choice: "))
    if choice == 1:
        message_to_proceed = input("Please type message to encode: ")
        print(encode_message(message_to_proceed))
    elif choice == 2:
        message_to_proceed = input("Please type message to decode: ")
        print(decode_message(message_to_proceed))
    elif choice == 3:
        pass
    else:
        print("Your choice is out of range")
        choice = int(input("Your choice: "))
