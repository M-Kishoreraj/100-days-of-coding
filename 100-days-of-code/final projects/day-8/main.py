alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#step-1-Function to encrypt or encode the plaintext using Caesar Cipher into cipher text
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        # Check if the letter is in the alphabet list
        if letter in alphabet:
            # Find the current position of the letter
            position = alphabet.index(letter)
            # Calculate the new position with the shift
            new_position = (position + shift_amount) % 26
            # Append the new letter to the cipher text
            cipher_text += alphabet[new_position]
        
        else:
            # If the letter is not in the alphabet, keep it as is            
            cipher_text += letter
    print(f"the encoded text is {cipher_text}")

#step-2-Function to decrypt or decode the ciphertext using Caesar Cipher into plain text
def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
         # Check if the letter is in the alphabet list
        if letter in alphabet:
            # Find the current position of the letter
            position = alphabet.index(letter)
            # Calculate the new position with the shift
            new_position = (position - shift_amount) % 26
            # Append the new letter to the plain text
            plain_text += alphabet[new_position]
        else:
            # If the letter is not in the alphabet, keep it as is
            plain_text += letter
    print(f"The decoded text is {plain_text}")
#step-3-import the logo from art 

from art import logo
print(logo)
print("helllllllo guyssss welcome to the cipher caesar game!!!!!!!!!!")

end_game= False

# Main loop to keep the game running
while not end_game:
    # Get user input for direction (encode or decode)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Get the message to encode or decode
    text = input("Type your message:\n").lower()
    # Get the shift amount 
    shift = int(input("Type the shift number:\n"))

    # Normalize the shift to ensure it's within the range of 0-25
    shift = shift%26
    
    # Perform encoding or decoding based on user input
    if direction == "encode":
      encrypt(plain_text=text,shift_amount=shift)

    elif direction == "decode":
        decrypt(cipher_text=text, shift_amount=shift)

    else:
        print("Invalid direction. Please type 'encode' or 'decode'.")

    # Ask the user if they want to restart the game
    restart=input("type 'yes',if you want to go again,otherwise go for 'no'.\n")
    if restart == "no":
     end_game = True
    print("adios")



