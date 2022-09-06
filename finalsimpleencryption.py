from cryptography.fernet import Fernet
from colorama import Fore
from colorama import Style

# we will be encryting the below string.
message = str(input("Type the messages:"))

# generate a key for encryptio and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key

key = Fernet.generate_key()

# Instance the Fernet class with the key

fernet = Fernet(key)

# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())

#print("original string: ", message)
print("encrypted message:",encMessage)

# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods

#print("Enter the password first and then input the encrypted message to decrypt")
while True:
    decrypt1=str(input("Enter the encrypted string:"))
    if str(decrypt1)==str(encMessage):
        
        def rep():
         a=str(input("NOW Enter the secret password:"))
         if a == "1234":
            maindecrypt = fernet.decrypt(encMessage).decode()
            print("The decrypted message: ", maindecrypt)
            
         else:
            print( f'{Fore.RED}The secret password you entered is incorrect!,\nPLEASE TRY AGAIN!' + '\x1b[0m')
            rep()
        rep()
        break
                     
    else:
        print( f'{Fore.RED}Invalid Encrypted string' + '\x1b[0m') 
        

                           


