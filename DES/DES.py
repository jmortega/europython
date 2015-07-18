#!/usr/python 
# -*- coding: utf-8 -*-

from Crypto.Cipher import DES
from Crypto import Random

des = DES.new('01234567', DES.MODE_ECB)
text = 'EUROPYTHON--2015'

#cipher dechiper with DES mode ECB
cipher_text = des.encrypt(text)
print('Cipher_text'+cipher_text)
decipher_text = des.decrypt(cipher_text)
print('Decipher_text'+decipher_text)

#cipher dechiper with DES mode ECB with random iv
iv = Random.get_random_bytes(8)
des1 = DES.new('01234567', DES.MODE_ECB, iv)
cipher_text = des1.encrypt(text)
print('Cipher_text'+cipher_text)
decipher_text = des1.decrypt(cipher_text)
print('Decipher_text'+decipher_text)


