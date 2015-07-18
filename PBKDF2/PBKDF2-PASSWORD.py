
from binascii import hexlify
import Crypto.Protocol.KDF as KDF
from Crypto.Hash import HMAC, SHA, SHA224, SHA256, SHA384, SHA512, MD2, MD4, MD5
import Crypto.Random 

password = "password"

for h in [SHA, SHA224, SHA256, SHA384, SHA512, MD2, MD4, MD5]:
    hashed_salted_password = KDF.PBKDF2(password,
                                        Crypto.Random.new().read(32), # salt
                                        count=6000,
                                        dkLen=32, 
                                        prf=lambda password, salt: HMAC.new(password, salt, h).digest())

    print ("{:20s}: {:s}".format(h.__name__, 
                                 hexlify(hashed_salted_password).decode('ascii')))
