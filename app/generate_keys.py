import os
from base64 import b64encode
from M2Crypto import RSA            

key = RSA.gen_key(1024, 65537)
raw_key = key.pub()[1]
b64key = b64encode(raw_key)

username = os.getlogin()
hostname = os.uname()[1]
keystring = 'ssh-rsa %s %s@%s' % (b64key, username, hostname)
print( keystring)
