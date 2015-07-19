# europython 2015

## Introduction

^ When we are talking about cryptography these are the key terms and more important concepts for introducing.

^ We will see that the key is a secret shared between sender and receiver.

^ The most important point is the cipher, that is ,the algorithm that converts plaintext in ciphertext

^ We have more advanced terms like salt, initialization vector and derived key.

^ These terms are used internally in the algorithm for generating the ciphertext

^ The idea of these terms are make as random as possible the generation of the key and avoid or prevent brute force attacks by rainbow tables or dictionary.

^ Key: The piece of information that allows you to either encrypt or decrypt your data.

^ Plaintext: The information that you want to keep hidden, in its unencrypted form. The plaintext can be any data at all: a picture, a spreadsheet, or even a whole hard disk

^ Ciphertext: The information in encrypted form

^ Cipher: The algorithm that converts plaintext to ciphertext and vice-versa

^ Salt – randomizes the hash of the key; prevents rainbow table attacks against the key

^ IV (initialization vector) – randomizes the encrypted message; prevents rainbow table attacks against the message

^ Derived Key – lengthens and strengthens the key via hashing; used instead of the original key; slows down brute-force attacks against the key


```objectivec

^ The salt creates a random string and prepend it to passwords to make brute forcing harder
^ A salt is a random sequence added to the password string before using the hash function. The salt is used in order to prevent dictionary attacks and rainbow tables attacks

```

---

## Caesar cipher


^ Caesar cipher is a monoalphabetic cipher

^ This was one of the first ways for cipher text in romans time

^ The idea is replace each symbol of the plaintext with a symbol of ciphertext using a single new alphabet

^ In this example we can see that with the alphabet LETTERS and the key=5 we generate the ciphertext ...

^ For example the space character is translated to %(percent) because in letters alphabet % is 5 positions to the left respect space character



## Hash functions

^ I want to make clear that hash functions are not a cryptographic protocol, they do not encrypt or decrypt information, but they are a fundamental part of many cryptographic protocols and tools.

^ You take an input text(for example a password) an it produces a digest with fixed size.

^ The generation is in one way, that means the input cannot be obtained  from the digest string, but there are functions like MD5 o SHA1 that are cryptography broken and it could be possible obtain the text from the digest

^ In python the most known is the hashlib library and its supports all know hash functions like MD5 or SHA

^ The hashlib module, included in The Python Standard library is a module containing an interface to the most popular hashing algorithms

^ If you use hash function to store passwords in database I recommend at least use SHA512 for avoid brute force and attacks

^ Another possibility is combine hash with salt(random number) for storing in database ,we can use also a key derivation function(KDF)

^ If we have a login in our web site ,the best for the user is store the hash of the password in the database and the best is use an algorithm that will not be broken like SHA256 or SHA512

^ You shouldn’t directly hash a password and store it. It’s much better to use a key derivation function such as PBKDF or scrypt, to avoid precomputation attacks.
•	SHA-1 is no longer considered secure.
•	The output size of SHA-256 is 256 bits.
•	The initialization vector for CFB mode (or any other mode) must be random for each encryption; it should not be a fixed string. Otherwise, a chosen-ciphertext attack applies.

## Compare passwords in login user

^ When the user logs in, the hash of the password input is generated and compared to the hash value stored in the database

^ we have tools like hash identifier that allows checking the type of a hash and the algorithm that is using in the hash


## Digital signature

^ Digital signature allows sign a message with your private key and check the authenticity of the message with your public key

^ You only need to know the public key to verify that the message is sended from a trustly source.


## WHY IS signature IMPORTANT?

^ The signature can establish a relationship of trust so that if a message is signed and you get verify the validity of the signature with the public key, that means the message is authentic and has not been altered or supplanted by a third person

## Dictionary attacks

^ if we use a direct hash function for the same message we obtain the same digest. This could be WEAK for brute force attacks

^ The best option for encrypt a password is use the pbkdf2 function for introduce random in the key generation



## Key stretching

^ Key stretching functions make it harder for an attacker to generate keys from a long list of passwords

^ Each iteration creates a new hash out of the concatenation of the previous key and the password

^ For having a strong password we can use a key stretching technique for make n iterations 

^ One of the simplest ways to stretch a key is to simply run the password through a hash function some pre-determined number of times. While a single execution of a hash function is quite fast, thousands of sequential executions of a hash function will not be. We take advantage of this for key stretching.


```objectivec

import hashlib
 
password = 'password'
iterations = 100000
key = ''
 
for i in xrange(iterations):
    m = hashlib.sha256()
    m.update(key + password)
    key = m.digest()
 
print 'SHA256 hash (in hex) of password after %d iterations:' % iterations
print m.digest().encode('hex')
```


## django security

^ Are you vulnerable to the heartbleed bug?

^ Are you enforcing SSL correctly? 

^ Did you set the proper flags for your cookies? 

^ Did you remember to disable weak ciphers?

^ How are you managing your secret keys?

^ Are you sure you authorise users correctly?

^ I will comment some libraries we can use for getting better security in web applications with django

^ The architecture in django was developed to be secure by default

^ These frameworks provide protection against sql injection,cross site scripting

## Security best practices

^ If we are using sessions in django,it uses session cookies

^ we can configure sending this cookies by a secure channel like https

^ if you have allowed_host=* you are vulnerable to attacks




## OWASP Python Security Project

^ Is a set of best practices for security professionals and developers to write applications more resilient to attacks and manipulations

^ These are the two important vulnerabilities when we are developing web applications with django

^ OWASP Top 10, put injection as the number one risks. If an application has SQL injection vulnerability, an attacker could read the data in the database.


## SQL Injection

^ SQL injection is a type of attack where a malicious user is able to execute arbitrary SQL code on a database.

^ An attack technique that allows hackers to gain control of a website’s underlying database due to flaws in the website’s application code.

## Cross-Site Scripting (XSS)

^ In general, an attack technique that allows an attacker to run script on a victim’s computer under the context of a another website the victim trusts. 

^ This attack exploits the trust the user has for a particular site


##Steganography

^ Steganography is the process of hiding secret information within other information.

^ the question we can make is, where is store de data?

^ The idea is use the LSB in each pixel in the image to store our secret message

^ We are going to take over the least significant bit of the amount of red color information in order to encode an image within an image






