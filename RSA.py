##Contributers: Andrew Farmer, Clayton McEntire, Chandler Richmond
import math
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
        
       
    z=p*q 
    
    pq=(p-1)*(q-1)
    e = random.randint(m,pq)
    divisor = math.gcd(e, pq)
    while(divisor !=1):
        e = random.randint(m,z)
        divisor = math.gcd(e,pq)
        
    pubkey=e
    
    privkey = multiplicative_inverse(e, pq)
    
    ## ALSO TEMPARARY DELETE WHEN BELOW IS UNCOMMMENTED
    return(((pubkey,n), (privkey,n)))
   
## TEMPARARALY COMMENTED OUT 
## TO UNCOMMENT PLEASE SELECT TEXT AND PRESS CTRL + 1

    # ##Generates public Key
    # divisor = 2
    # while(divisor != 1):
    #     e = random.randint(0, n)
    #     divisor = math.gcd(e, n)
        
    # x, y,d = extended_gcd(e, n)
    
    
    # print("Divisor: " + str(divisor))
    # print("Public Key: " + str(e))
    # print("Private Key: " + str(x))
    # return ((e,n),(x,n))



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

def multiplicative_inverse(e, pq):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_pq = pq

    while e > 0:
        temp1 = temp_pq//e
        temp2 = temp_pq - temp1 * e
        temp_pq = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_pq == 1:
        return d + pq

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
   ciphertext = ""
   string = string.upper()
   for char in string:
       ciphertext = (pow(ord(char), key, n))

   return ciphertext
        
    
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
            sys.exit();
          
    
        
## Starts Main   
main()
