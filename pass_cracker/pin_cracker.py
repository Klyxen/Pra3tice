#This is the main Script for Pin cracker
pin = "3"

#Checks the length of the pin
pin_len = len(pin)

#Finds the password and bases the length of the given pin
for test in range(10 ** pin_len):
    guess = str(pin).zfill(pin_len) 
    print(f"Trying : {guess}")
    if guess == pin:
        print(f"PIN found! : {guess}")
        break
