#!/usr/python 
# -*- coding: utf-8 -*-


import os
 
from Crypto.Protocol.KDF import PBKDF2
 
password = 'europython'
iterations = 5000
key = ''
salt = os.urandom(32)
 
key = PBKDF2(password, salt, dkLen=32, count=iterations)
 
print 'Random salt (in hex):'
print salt.encode('hex')
print 'PBKDF2-derived key (in hex) of password after %d iterations: ' % iterations
print key.encode('hex')




