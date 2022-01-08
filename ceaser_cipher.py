n = True
while n == True:
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","X","y","z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","X","y","z"]
    direction = input("Type encrypt to 'ENCODE' and decrypt for 'DECODE' : \n" )
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : "))

    def encrypt(plain_text,shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position+shift_amount
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        print(f" The encoded text is '{cipher_text}'")
        n = input(" True for continue  and False for exit : ")

    def decrypt(plain_text,shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position-shift_amount
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        print(f" The encoded text is '{cipher_text}'")
        n = input(" True for continue  and False for exit : ")
    if direction == "encrypt":
        encrypt(plain_text=text,shift_amount=shift)
    elif direction == "decrypt":
        decrypt(plain_text=text,shift_amount=shift)

    print("Have a nice day.")