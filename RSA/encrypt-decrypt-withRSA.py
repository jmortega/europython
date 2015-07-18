#!/usr/python 
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import zlib
import base64


def encrypt_string(plaintext):

	print "Compressing: %d bytes" % len(plaintext)
	plaintext = zlib.compress(plaintext)
	print "Encrypting %d bytes" % len(plaintext)

	random_generator = Random.new().read
	rsakey = RSA.generate(1024, random_generator)

	rsakey = PKCS1_OAEP.new(rsakey)
	encrypted = ""

	encrypted += rsakey.encrypt(plaintext)

	encrypted = encrypted.encode("base64")
	print "Base64 encoded crypto: %d" % len(encrypted)
	return encrypted,rsakey


def decrypt_string(text,rsaKey):

	chunk_size= 256
	offset = 0
	
	decrypted = ""
	encrypted = base64.b64decode(text)

	while offset < len(encrypted):
	    decrypted += rsakey.decrypt(encrypted[offset:offset+chunk_size])
	    offset += chunk_size
	    # now we decompress to original
	    plaintext = zlib.decompress(decrypted)

	return plaintext
    
encrypted,rsakey = encrypt_string("MESSAGE TO ENCRYPT")
print encrypted

decrypted = decrypt_string(encrypted,rsakey)
print decrypted


