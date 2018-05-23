import time
import pyotp

def test():
    totp = pyotp.TOTP("LNZREXIQXPNXUESK") 
    print(totp.now()) 
    print(totp.verify(totp.now()))
    totp.provisioning_uri("alice@google.com") 
