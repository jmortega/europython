#!/usr/python 
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import cPickle

KEYSIZE = 256 * 8
 
def readfile(filename):
    fh = open(filename, 'rb')
    string = fh.read()
    fh.close()
    return string
     
def writefile(filename, string):
    fh = open(filename, 'wb')
    fh.write(string)
    fh.close()

def read_serial(filename):
    fh = open(filename, 'rb')
    data = cPickle.load(fh)
    fh.close()
    return data

def write_serial(filename, data):
    fh = open(filename, 'wb')
    cPickle.dump(data, fh, protocol=cPickle.HIGHEST_PROTOCOL)
    fh.close()
 
random_generator = Random.new().read
RSAkey = RSA.generate(KEYSIZE, 
                      randfunc=random_generator, 
                      progress_func=None, 
                      e=65537)
public_key = RSAkey.publickey()
 
# Export the public key
pke = public_key.exportKey(format='PEM', passphrase=readfile('public_passphrase.txt'), pkcs=1)
writefile('public_key.txt', pke)
 
# Export the private key
pke = RSAkey.exportKey(format='PEM', passphrase=readfile('private_passphrase.txt'), pkcs=1)
writefile('private_key.txt', pke)

#encrypt file 
PASSPHRASE_PRIVATE = readfile('private_passphrase.txt')
plainfile = readfile('encrypt.txt')
 
RSAkey = readfile('private_key.txt')
RSAkey = RSA.importKey(RSAkey, passphrase=PASSPHRASE_PRIVATE)
 
h = SHA256.new(plainfile)
signer = PKCS1_v1_5.new(RSAkey)
signature = signer.sign(h)
 
# Save signature
write_serial('signature.pkl', signature)
 
# Encrypt file
write_serial('encryptedfile.pkl', RSAkey.encrypt(plainfile, ''))


encodedfile = read_serial('encryptedfile.pkl')
 
RSAkey = readfile('private_key.txt')
RSAkey = RSA.importKey(RSAkey, passphrase=readfile('private_passphrase.txt'))
 
# Decrypt data
plaindata = RSAkey.decrypt(encodedfile)
 
# Verify author
h = SHA256.new(plaindata)
verifier = PKCS1_v1_5.new(RSAkey)
signature = read_serial('signature.pkl')
if verifier.verify(h, signature):
    print "The signature is authentic.\n"
    print plaindata
else:
    print "The signature is not authentic."
    
