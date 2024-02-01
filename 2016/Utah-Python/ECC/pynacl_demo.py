import nacl.utils
from nacl.public import PrivateKey, Box

msg = 'Once upon a time and a very good time it was there was a moocow coming down along the road.'.encode()

skbob = PrivateKey.generate()
pkbob = skbob.public_key

skalice = PrivateKey.generate()
pkalice = skalice.public_key

# again, the box
bob_box = Box(skbob, pkalice)
alice_box = Box(skalice, pkbob)

# a nonce is a single-use string of random data
# CAUTION: use it once only
nonce = nacl.utils.random(Box.NONCE_SIZE)

encrypted = bob_box.encrypt(msg, nonce)
decrypted = alice_box.decrypt(encrypted)
