#IMPORTS
from secrets import *
from random import *
from math import *
from os import *

def dataset():
    while True:
        input_var=input('What Dataset would you like to use? ')
        if input_var=="-h" or input_var=="--help" or input_var=="help":
            print("""This is where you determine what characters you want to appear in your password.

Some common datasets include:
01
01234567
0123456789
01233456789ABCDEF
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~€‚ƒ„…†‡ˆ‰Š‹.‘’“”•–—˜™›¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿÷
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹Œ.Ž‘’“”•–—˜™š›œžŸ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
        
You can copy and paste any of these for your password, or make your own.""")
            continue
        else:
            return input_var

def lngth(Rlngth):
    while True:
        input_var=input('How long do you want your passwords(s)? Recommended: '+str(Rlngth)+" ")
        if input_var=="-h" or input_var=="--help" or input_var=="help":
            print("""\nThis is where you determine how many characters you want to appear in your password.
The recommended length is set to provide AES-256 grade security or better, 
so it is a good option if you don't know what to choose. \n""")
            continue
        else:
            return input_var

def itrtn():
    while True:
        input_var=input('How many passwords do you want to create? ')
        if input_var=="-h" or input_var=="--help" or input_var=="help":
            print("""\nThis is just where you determine how many passwords you want to
create that use the parameters set above.\n""")
            continue
        else:
            return input_var

#GENERATOR
def make_password():
    dataset_val=dataset()
    Rlngth=str(int(ceil(log(2**256,len(dataset_val)))))
    lngth_val=lngth(Rlngth)
    itrtn_val=int(itrtn())
    for i in range(itrtn_val):
        datasetvalues=[]
        for i in range(21384):
            datasetvalues.append(dataset_val[randbelow(len(dataset_val))])
        shuffle(datasetvalues)
        largearray=[]
        for i in range(40000):
            largearray.append(datasetvalues[randbelow(len(datasetvalues)-36)+trunc(1+((randbelow(1000000)-1)%9))+trunc(1+((randbelow(1000000)-1)%9))+trunc(1+((randbelow(1000000)-1)%9))])
        shuffle(largearray)
        passwordarray=[]
        for i in range(int(lngth_val)):
            passwordarray.append(largearray[randbelow(len(largearray)-36)+trunc(1+((randbelow(1000000)-1)%9))+trunc(1+((randbelow(1000000)-1)%9))+trunc(1+((randbelow(1000000)-1)%9))])
        password_string = ''.join(map(str, passwordarray))
        print(password_string)
def recursion():
    while True:
        make_password()
        while True:
            answer = str(input('Would you like to generate another password? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            continue
        else:
            print("Goodbye, "+ getlogin())
            break


print("Hello, "+ getlogin())
str(recursion())
