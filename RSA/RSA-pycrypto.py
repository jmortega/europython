#!/usr/python 
# -*- coding: utf-8 -*-

import os
	
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256

#text to encrypt
text ="EUROPHYTON2015"
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

# can_encrypt() checks the capability of encrypting data using this algorithm
print(key.can_encrypt())

#can_sign() checks the capability of signing messages
print(key.can_sign())

#has_private() returns True if the private key is present in the object
print(key.has_private())

#obtain public key
print 'public_key'
public_key = key.publickey()
print public_key

#encrypt with public key
print 'encrypted data'
enc_data = public_key.encrypt(text, 32)
print(enc_data)

#signing message
print 'signature'
hash = SHA256.new(text).digest()
signature = key.sign(hash, '')
print signature

#decrypt with private key
decrypt_data = key.decrypt(enc_data)
print('decrypt_data '+decrypt_data)


#verify signing
hash = SHA256.new(decrypt_data).digest()
print(public_key.verify(hash, signature))


