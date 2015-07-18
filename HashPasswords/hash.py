#!/usr/python 
# -*- coding: utf-8 -*-

import os
	
from Crypto.Hash import MD5
from Crypto.Hash import SHA256

print(MD5.new('python').hexdigest())
#print(SHA256.new('python').hexdigest())


#hashlib from default python installation
from hashlib import md5
from hashlib import sha256
from hashlib import sha512

print(md5('europython').hexdigest())
print(sha256('europython').hexdigest())
#print(sha512('EuroPython').hexdigest())
