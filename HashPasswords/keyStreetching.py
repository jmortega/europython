#!/usr/python 
# -*- coding: utf-8 -*-


import hashlib
 
password = 'uSh{ei3aiV'
iterations = 100000
key = ''
 
for i in xrange(iterations):
    m = hashlib.sha256()
    m.update(key + password)
    key = m.digest()
 
print 'SHA256 hash (in hex) of password after %d iterations:' % iterations
print m.digest().encode('hex')


