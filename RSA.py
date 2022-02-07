##Contributers: Andrew Farmer, Clayton McEntire


##Generates both public and private keys
def generate():
    print("RSA keys have been generated.")
    
##Generate digital signature
def digital():
    print("test")

##Authenticates the digital signature
def authenticate():
    print("test")
    
##Encrypts with a public key
def encrypt():
    print("test")
    
##Decrypts with a private key
def decrypt():
    print("test")
    
## Main Selection Menu
def menu():
    print("Please select your user type:")
    print("1. Public User \n2. The owner of the keys \n3. Exit Program")
    choice = None
    choice = int(input("\nPlease Enter your choice: "))  
    if choice == 1:
        publicusr()
## Public User
def publicusr():
     print("\nAs a public user, what would you like to do?")
     print("1. Send an encrypted message \n2. Authenticate a digital signature \n3. Exit")
     choice = None
     choice = int(input("Enter your choice: "))
     if choice ==1:
        string = None
        string = str(input("Enter a message: "))
                
        ## CALL ENCRYPT AND send string
        print("Message encrypted and sent.")
     elif choice == 3:
        menu()

##Driver Function
def main():
    generate()
    digital()
    authenticate()
    encrypt()
    decrypt()
   ## menu()
   ## publicusr()
    
main()
# Runs the main menu
menu()