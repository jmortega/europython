#!/usr/python 
# -*- coding: utf-8 -*-


import hashlib
import os
 
password = 'uSh{ei3aiV'
iterations = 100000
key = ''
salt = os.urandom(32)
 
for i in xrange(iterations):
    m = hashlib.sha256()
    m.update(key + password + salt)
    key = m.digest()
 
print 'Random salt (in hex):'
print salt.encode('hex')
print 'SHA256 hash (in hex) of password after %d iterations with salt: ' % iterations
print m.digest().encode('hex')



