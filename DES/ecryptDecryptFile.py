#!/usr/python 
# -*- coding: utf-8 -*-


import os

from Crypto.Cipher import DES3
from Crypto import Random


def encrypt_file(in_filename, out_filename, chunk_size, key, iv):
	
	des3 = DES3.new(key, DES3.MODE_CFB, iv)
	
	with open(in_filename, 'r') as in_file:

		with open(out_filename, 'w') as out_file:

			while True:

				chunk = in_file.read(chunk_size)

				if len(chunk) == 0:

					break

				elif len(chunk) % 16 != 0:

					chunk += ' ' * (16 - len(chunk) % 16)

					out_file.write(des3.encrypt(chunk))

 

def decrypt_file(in_filename, out_filename, chunk_size, key, iv):

        des3 = DES3.new(key, DES3.MODE_CFB, iv)

        with open(in_filename, 'r') as in_file:

                with open(out_filename, 'w') as out_file:

                        while True:
                                chunk = in_file.read(chunk_size)

                                if len(chunk) == 0:
                                        break

                                out_file.write(des3.decrypt(chunk))



iv = Random.get_random_bytes(8)
key = Random.get_random_bytes(16)
with open('encrypt.txt', 'r') as f:
        print 'encrypt.txt: %s' % f.read()
        encrypt_file('encrypt.txt', 'encrypted.enc', 8192, key, iv)
with open('encrypted.enc', 'r') as f:
        print 'encrypted.enc: %s' % f.read()
        decrypt_file('encrypted.enc', 'encrypted.dec', 8192, key, iv)
with open('encrypted.dec', 'r') as f:
        print 'encrypted.dec: %s' % f.read()

