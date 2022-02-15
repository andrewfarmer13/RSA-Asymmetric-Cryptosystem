##Contributers: Andrew Farmer, Clayton McEntire
import math
import random
## Importing allows for exiting of program without error. 
import sys

##Generates both public and private keys
def generate():
    
    ##We need to add a generate prime number function to get a larger n
    ##Max Size
    n = 500000
    ## Min Size
    m = 10000
    
    ## Generate Public Key
    p = random.randint(m,n);
    
    x = random.randint(2,p);
   
    ## Call Fermats test
    ## Function will determine true or false if prime 
    t = determine_prime(p,x)
    ## If it is not prime re-call the function untill a prime is found 
    if t == False:
        generate()
    
    ## ALSO TEMPARARY DELETE WHEN BELOW IS UNCOMMMENTED
    return((p,p),(p,p))
   
## TEMPARARALY COMMENTED OUT 
## TO UNCOMMENT PLEASE SELECT TEXT AND PRESS CTRL + 1
# 
#     ##Generates public Key
#     divisor = 2
#     while(divisor != 1):
#         e = random.randint(0, n)
#         divisor = math.gcd(e, n)
#         
#     x, y,d = extended_gcd(e, n)
#     
#     
#     print("Divisor: " + str(divisor))
#     print("Public Key: " + str(e))
#     print("Private Key: " + str(x))
#     return ((e,n),(x,n))
# 
# 

## Fermats Test 
def determine_prime(p,x):
## Preform Fermat's Test 40 times
   
    i=0
    t=True
   ## Loop 40 times to determine if prime and if it isnt stop immedately 
    while i!=40 and t == True:
          if pow(x, p-1, p) != 1:
              ## Print can be commented out after viewing
              print("Value "+ str(p) +" Is not prime")
              t = False
              break
          i += 1
    ## IF the full loop has been ran then the number is prime
    ## If and print can be commented out after viewing
    if t == True:
        print("Value "+ str(p) +" Is prime")
    ## Returns t to let generate know if it is prime or not
    return t

 ##Extended GCD
def extended_gcd(a =1, b = 1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a%b)
    return y, x - a//b*y, d

   
##Generate digital signature
def digital():
    print("test")

##Authenticates the digital signature
def authenticate():
    print("test")
    
##Encrypts with a public key
def encrypt(string, pubkey):
   key, n = pubkey
   
   ##Not sold on this, just the intial idea
   ciphertext = ""
   string = string.upper()
   for x in string:
       x = ord(x)
       a = chr((x**key)%n)
       ciphertext += a

   return ciphertext
        
    
##Decrypts with a private key
def decrypt():
    print("test")
    
## Public User
def publicusr(pubKey):
     print("\nAs a public user, what would you like to do?")
     print("1. Send an encrypted message \n2. Authenticate a digital signature \n3. Exit")
     choice = int(input("Enter your choice: "))
    
     while(choice != 3):
         if (choice ==1):
            string = str(input("Enter a message: "))
            ciphertext = encrypt(string, pubKey)
            ## CALL ENCRYPT AND send string
            print(ciphertext)
            break
         elif (choice ==2):
            print("TEST REPLACE LATER")
   
     

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
         main()


## Owner of keys
def owner(privkey):
    print("test")


##Driver Function
def main():
    public, private = generate()
    choice = 0;
    
    while(choice != 3):
        print("\nPlease select your user type:")
        print("1. Public User \n2. The owner of the keys \n3. Exit Program")
        choice = int(input("\nPlease Enter your choice: "))  
        if choice == 1:
            publicusr(public)
        elif choice == 2:
            owner(private)
        elif choice ==3:
            sys.exit();
          
    
        
## Starts Main   
main()
