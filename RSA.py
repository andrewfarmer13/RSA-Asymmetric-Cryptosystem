##Contributers: Andrew Farmer, Clayton McEntire, Chandler Richmond
#import math
import random
## Importing allows for exiting of program without error. 
import sys

##Generates both public and private keys
def generate():
    
    t= False
    ##We need to add a generate prime number function to get a larger n
    ##Max Size
    n = 500000
    ## Min Size
    m = 10000
   
    while(t == False):
        ## Generate Public Key
        p = random.randint(m,n);
        
        q = random.randint(m,n);
       
        ## Call Fermats test
        ## Function will determine true or false if prime 
        t = determine_prime(p,q)
        ## If it is not prime re-call the function untill a prime is found 
        
   
    ## Euclid's GCD (FINDS e )
    ## Finds Realitive prime from psudo primes
    e=(p-1)*(q-1) 
    n = p*q;
    
    ## Calles Extended Euclid 
    ## Finds d multiplicative inverse of e
    d, y,x = extended_gcd(e, n)
       
    # public key (e) # Private key (d)

    ## public key and Private key
    return(((e,n), (d,n)))
   


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
    
    
    e, n = pubkey
    
    string = string.upper()
    
    ## Creates a list of the encrypted text as intigers
    letters = [pow(ord(string[i]),e,n) for i in range(len(string))]
    
    ## DELETE AFTER DECODING IS IMPLEMENTED
    i =0
    while i != len(string):
       # letters[i] = pow(ord(string[i]),e,n)
        print("Test " + str(letters[i]))
        i += 1
    
    return letters
        
    
##Decrypts with a private key
def decrypt(privkey, encryptedMessage):
    # Unpack the key into its components
    key, n = privkey
    plaintext = ""
   
    for char in str(encryptedMessage):
        plaintext += chr(pow(ord(char), key, n))
        
    print(plaintext)

    
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
            print("message encrypted")
            break
         elif (choice ==2):
            print("TEST REPLACE LATER")
            return ciphertext
        
       
   

## Owner of keys
def owner(privkey,encryptedMessage):
   print("\nAs an owner, what would you like to do?")
   print("1.Decrypt an encrypted messaged")
   
   message = decrypt(privkey, encryptedMessage)
   print(message)


##Driver Function
def main():
    public, private = generate()
    choice = 0;
    
    print(str(public) + " " +str(private))
    

    while(choice != 3):
        print("\nPlease select your user type:")
        print("1. Public User \n2. The owner of the keys \n3. Exit Program")
        choice = int(input("\nPlease Enter your choice: "))  
        if choice == 1:
          encryptedMessage = publicusr(public)
        elif choice == 2:
            owner(private, encryptedMessage)
        elif choice ==3:
             print("Bye for now!")
             sys.exit();
  
       
## Starts Main   
main()
