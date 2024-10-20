'''
2022 Bjoern Annighoefer

'''

import hashlib
import os
import base64
#type checking
from typing import ByteString

# PASWORD CHECKING

SALT_LEN = 32
HASH_ITER = 100

def GeneratePasshash(password:str)->str:
    bSalt:ByteString = os.urandom(SALT_LEN) #randomly create a salt
    bSaltedAndHashedPassword:ByteString = GenerateSaltedPasshash(password,bSalt)
    passhash = base64.b64encode(bSalt + bSaltedAndHashedPassword).decode('utf-8')
    return passhash

def VerifyPassword(password:str, passhash:str)->bool:
    #retrieve the salt from passhash
    bPasshash = base64.b64decode(passhash.encode('utf-8'))
    bSalt = bPasshash[:SALT_LEN] #first part of the passhash
    bSaltedAndHashedPassword = bPasshash[SALT_LEN:] #second part of the passhash
    #calculate a salted hash for the given password
    bSaltedAndHashedPassword2 = GenerateSaltedPasshash(password,bSalt)
    #finally compare both hashed passwords
    return bSaltedAndHashedPassword == bSaltedAndHashedPassword2

def GenerateSaltedPasshash(password:str, bSalt:ByteString):
    '''Encapsulates the hashing function
    '''
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bSalt, HASH_ITER)

def IsValidPasshash(passhash:str)->bool:
    isValid = False
    try:
        bPasshash = base64.b64decode(passhash.encode('utf-8'))
        bSalt = bPasshash[:SALT_LEN] #first part of the passhash
        bSaltedAndHashedPassword = bPasshash[SALT_LEN:] #second part of the passhash
        if(bSalt and bSaltedAndHashedPassword):
            isValid = True
    except: #catch everything but do not set the result to true
        pass
    return isValid