##Contributers: Andrew Farmer, Clayton McEntire
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
    
    y, d,x = extended_gcd(e, n)
       

    
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


    

##Encrypts with a public key
def encrypt(string, pubkey):
    
    
    e, n = pubkey
    
    string = string.upper()
   
    letters = [pow(ord(string[i]),e,n) for i in range(len(string))]
    
    i =0
    while i != len(string):
    letters[i] = pow(ord(string[i]),e,n)
    print("Test " + str(letters[i]))
    i += 1
    
    return letters
        
    
##Decrypts with a private key
def decrypt(privkey, encryptedMessage):
    # Unpack the key into its components

    d, n = privkey
   
   
    j=0
    message = ""
    while j != len(encryptedMessage):
        hold = encryptedMessage[j]
        letter = (pow(hold,d,n)
        message += chr(int(letter))
        print("letter ".join(message[j]))
        letter =0
        j += 1
   
    k=0
    while k != len(encryptedMessage):
       print(str(message[k]))
       k += 1
     
    return message
        

 
##Generate digital signature
def digitalSign(message, privkey):
    key, n = privkey
    
    signature = (ord(message)**key) % n
    
    return signature

def digitalVerify(signature, pubkey, message):
    
    key, n = pubkey
    
    verification = (signature ** key) % n
    
    if(verification == message):
        print("Verification successful, message accepted")
    else:
        print("Verification unsuccessful, message not accepted")

##Authenticates the digital signature
def authenticate():
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
            print("message encrypted")
            break
         elif (choice ==2):
            print("TEST REPLACE LATER")
            return ciphertext
    
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
            sys.exit();
  
       
## Starts Main   
main()
