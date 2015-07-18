#!/usr/python 
# -*- coding: utf-8 -*-

import os
import hashlib

from Crypto.Cipher import AES


password = 'mysecretpassword'
key = hashlib.sha256(password).digest()

IV = 16 * '\x00'           # Initialization vector
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = 'EUROPYTHON--2015'
ciphertext = encryptor.encrypt(text)

print(ciphertext.encode('hex'))

decryptor = AES.new(key, mode, IV=IV)
plain = decryptor.decrypt(ciphertext)

print(plain)


 
key = 'mysecretpassword'
plaintext1 = 'Secret Message A'
plaintext2 = 'Secret Message B'
plaintext3 = 'Secret Message C'
plaintext4 = 'Secret Message A'
 
encobj = AES.new(key, AES.MODE_ECB)
ciphertext1 = encobj.encrypt(plaintext1)
ciphertext2 = encobj.encrypt(plaintext2)
ciphertext3 = encobj.encrypt(plaintext3)
ciphertext4 = encobj.encrypt(plaintext4)
 
# Resulting ciphertext in hex
print ciphertext1.encode('hex')
print ciphertext2.encode('hex')
print ciphertext3.encode('hex')
print ciphertext4.encode('hex')


key = 'mysecretpassword'
iv = os.urandom(16)
 
# Output the initialization vector
print 'IV: ' + iv.encode('hex')
 
plaintext1 = 'Secret Message A'
plaintext2 = 'Secret Message B'
plaintext3 = 'Secret Message C'
plaintext4 = 'Secret Message A'
 
encobj = AES.new(key, AES.MODE_CBC, iv)
ciphertext1 = encobj.encrypt(plaintext1)
ciphertext2 = encobj.encrypt(plaintext2)
ciphertext3 = encobj.encrypt(plaintext3)
ciphertext4 = encobj.encrypt(plaintext4)
 
# Resulting ciphertext in hex
print 'A:  ' + ciphertext1.encode('hex')
print 'B:  ' + ciphertext2.encode('hex')
print 'C:  ' + ciphertext3.encode('hex')
print 'A:  ' + ciphertext4.encode('hex')


