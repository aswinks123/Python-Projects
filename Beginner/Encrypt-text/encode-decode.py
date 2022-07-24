#CAESAR CIPHER : Encode and Decode message based on shift.
#Note : This works with only letters. Add symbols and numbers to list to add additional functionalities.
#Created by Aswin ks



#Function to do the operation


def endecode(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *=  -1
    for char in start_text:   #Checking whether the char is in our alphabet list if not then leave it as it is in output
        if char in alphabet:

            position=alphabet.index(char)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char


    print(f"The {direction}d text is : {end_text}")





print("This program encrypt and decrypt text.You can add text in any format.Dont forget the salt!.Give it a try.")
alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
alphabet=2*alphabet  # To avoid out of index issues

continues=True
while continues==True:   # for continuous usage of program
    direction=input("Type' encode' to encrypt and 'decode' to decrypt:\n" )
    text=input("Type your message:\n").lower()
    shift=int(input("Enter the salt number : \n"))
    shift=shift % 26

    endecode(text,shift,direction)

    x=input("Do you want to continue?(y/n) :").lower()   #Asking user to continue?
    if x!='y':
        print("Exiting.See you soon Good bye...")
        continues=False









