
##Contributers: Andrew Farmer, Clayton McEntire
import math
import random
## Importing allows for exiting of program without error. 
import sys



##Generates both public and private keys
def generate():
    
   
   t = False
   s = False
   
   while(t != True) or (s != True):
       p = random.randint(100,1000)
       q = random.randint(100,1000)
       
       t = determine_prime(p, q)
       s = determine_prime(q, p)
       
       
       
   print(str(p))
   print(str(q))
   n = p*q
   phi = (p-1)*(q-1)
   
   e = random.randint(100, phi)
   divisor = math.gcd(e, phi)
   while(divisor != 1):
       e = random.randint(100, phi)
       divisor = math.gcd(e, phi)
       
   x , y, d = extended_gcd(e, phi)
   if x < 0:
       x = phi +x
   ## public key and Private key
   return(((e,n), (x, n)))
   


## Fermats Test 
def determine_prime(p,x):
## Preform Fermat's Test 40 times
   
    i=0
    t=True
   ## Loop 40 times to determine if prime and if it isnt stop immedately 
    while i!=200 and t == True:
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
    length = len(string)
    string = string.upper()
    letters = []
   
    # letters = [pow(ord(string[i]),e,n) for i in range(len(string))]
    
    # i =0
    # while i != len(string):
    #     # letters[i] = pow(ord(string[i]),e,n)
    #     print("Test " + str(letters[i]))
    #     i += 1
    
    # return letters
    
    print(str(e))
    
    for x in range(length):
        temp = ord(string[x])
        temp = pow(temp, e)
        temp = temp % n
        print(str(temp))
        letters.append(temp)
    return letters
 
def encryptFS(string, pubkey):
        
        e, n = pubkey
        length = len(string)
        string = string.upper()
        letters = []
        string1 = ""
       
        # letters = [pow(ord(string[i]),e,n) for i in range(len(string))]
        
        # i =0
        # while i != len(string):
        #     # letters[i] = pow(ord(string[i]),e,n)
        #     print("Test " + str(letters[i]))
        #     i += 1
        
        # return letters
        
        print(str(e))
        
        x = 0
        for x in range(length):
            temp = ord(string[x])
            temp = pow(temp, e)
            temp = temp % n
            #print(str(temp))
            string1 += str(temp)
        return string1
    

    
##Decrypts with a private key
def decrypt(privkey, list):
    # Unpack the key into its components

    d, n = privkey
    letters = []
    length = len(list)
    plain = ""
  
# Iterating the index
# same as 'for i in range(len(list))'



    for x in range(length):
        letters.append(chr(pow(list[x], d, n)))
        print(str(letters[x]))
        
        
    for x in range(len(letters)):
        plain += str(letters[x])
        
    print (plain)
   
    # j=0
    # message = ""
    # while j != len(encryptedMessage):
    #     letter = pow(encryptedMessage[j], d, n)
    #     message += str(chr(letter))
    #     j += 1

     
    # return message
    
    
        
 


    # key, n = privkey
    
    # string = ""
    # x = 0
    
    
    # while x != len(encryptedMessage):
    #     string += str(pow(encryptedMessage[x], key) % n)
 
    # print(string)
    
    return plain
 
##Generate digital signature
def digitalSign(privkey, pubkey,string):
    
    
    key, n = privkey
    
    
    signature = (int(encryptFS(string, pubkey))**key) % n
    print("messaged signed")
    
    return signature


    
## Public User
def publicusr(pubKey, sing):
     print("\nAs a public user, what would you like to do?")
     print("1. Send an encrypted message \n2. Authenticate a digital signature \n3. Exit")
     choice = int(input("Enter your choice: "))
     string = ""
    
     while(choice != 3):
         if (choice ==1):
            string = str(input("Enter a message: "))
            ciphertext = encrypt(string, pubKey)
            ## CALL ENCRYPT AND send string
            print("message encrypted")
            break
         elif (choice ==2):
            print("Sorry nothing here right now")
            break
    
     return (ciphertext, string)

## Owner of keys
def owner(privkey,encryptedMessage, pubkey, string):
   print("\nAs an owner, what would you like to do?")
   print("1.Decrypt an encrypted messaged")
   print("2.Digitally Sign a message")
   choice = int(input("Enter your choice: "))
   
   while(choice != 3):
       if(choice == 1):
           message = decrypt(privkey, encryptedMessage)
           print(message)
           break
       elif(choice == 2):
         sign =  digitalSign(privkey, pubkey, string)
         return sign
         break
 
##Driver Function
def main():
    public, private = generate()
    choice = 0;
    string = ""
    sing  = 0
    
    print(str(public) + " " +str(private))
    
    while(choice != 3):
        print("\nPlease select your user type:")
        print("1. Public User \n2. The owner of the keys \n3. Exit Program")
        choice = int(input("\nPlease Enter your choice: "))  
        if choice == 1:
          encryptedMessage, string = publicusr(public, sing)
        elif choice == 2:
          sign =  owner(private, encryptedMessage, public, string)
        elif choice ==3:
            sys.exit();
  
       
## Starts Main   
main()
