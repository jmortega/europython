#!/usr/python 
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random

key_size = 32 #AES256
iterations = 10000
key = 'password'
secret = 'a secret message'

salt = Random.new().read(key_size)
iv = Random.new().read(AES.block_size)
derived_key = PBKDF2(key, salt, key_size, iterations)
cipher = AES.new(derived_key, AES.MODE_CFB, iv)

encodedtext = iv + cipher.encrypt(secret)

print encodedtext.encode('hex')

decodedtext = str(cipher.decrypt(encodedtext))[16:]

print decodedtext

