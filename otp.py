import time
import pyotp

def test():
    totp = pyotp.TOTP("MZXW633PN5XW6MZX") 
    print(totp.now()) 
    print(totp.verify(totp.now()))
    totp.provisioning_uri("alice@google.com") 
test()