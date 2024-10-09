import string
import random


#check length is greater than 7 or not
def checkLen():
    while True:
        password_len=int(input('Enter the length of desired password: '))
        if(password_len>7):
            return password_len
        else:
            print('Minimum length should be "8"')
            
words= string.ascii_letters+string.digits+string.punctuation     #concate letters,digits and punctuation
password_len=checkLen()
password=''
while(password_len>0):
    password+=random.choice(words)
    password_len-=1
print('The desired password is ',password)
