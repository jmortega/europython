#!/usr/python 
# -*- coding: utf-8 -*-

#	Reverse	Cipher
message	= "Three can keep a secret"
translated  = ""

i = len(message) - 1
while i >= 0:
    translated = translated	+ message[i]
    i =  i - 1
print(translated)
