##Contributers: Andrew Farmer, Clayton McEntire
import math
import random

##Generates both public and private keys
def generate():
    divisor = 2
    while(divisor != 1):
        e = random.randint(0, 10200)
        divisor = math.gcd(e, 10200)
        
    
    print("Divisor: " + str(divisor))
    print("Public Key: " + str(e))
    
    
##Generate digital signature
def digital():
    print("test")

##Authenticates the digital signature
def authenticate():
    print("test")
    
##Encrypts with a public key
def encrypt(str):
    print("test")
    
##Decrypts with a private key
def decrypt():
    print("test")
    
## Public User
def publicusr():
     print("\nAs a public user, what would you like to do?")
     print("1. Send an encrypted message \n2. Authenticate a digital signature \n3. Exit")
     choice = int(input("Enter your choice: "))
     if choice ==1:
        string = None
        string = str(input("Enter a message: "))
        encrypt(string)
        ## CALL ENCRYPT AND send string
        print("Message encrypted and sent.")
     if choice ==2:
        print("TEST REPLACE LATER")
    #Exit to menu
     elif choice == 3:
         exit()

## Owner of keys
def owner():
    print("temp")


##Driver Function
def main():
    generate()
    choice = 0;
    
    while(choice != 3):
        print("\nPlease select your user type:")
        print("1. Public User \n2. The owner of the keys \n3. Exit Program")
        choice = int(input("\nPlease Enter your choice: "))  
        if choice == 1:
            publicusr()
        elif choice == 2:
            owner()
    
        
    
main()
