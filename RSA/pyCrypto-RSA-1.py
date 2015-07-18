#!/usr/python 
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5


def generate_RSA(bits=1024):    
    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    secret_key = new_key.exportKey("PEM")
    return new_key


RSAKey = generate_RSA()
#public key for encrypting
#private key for decrypting

print RSAKey.exportKey('PEM')

pubkey = RSAKey.publickey()
print pubkey.exportKey('PEM')


message = 'EUROPHYTON 2015'

hash_message = MD5.new(message).digest()
signature = RSAKey.sign(hash_message+"",'')

# Encrypt message with public key
encrypted_message = pubkey.encrypt(message, 32)

print encrypted_message

# Decrypt message with private key
decrypted_message = RSAKey.decrypt(encrypted_message)


# Signature validation and console output...
hash_decrypted = MD5.new(decrypted_message).digest()
if RSAKey.verify(hash_decrypted, signature):
    print "Message received:"
    print decrypted_message
    print ""
