import libnacl.public

msg = 'Once upon a time and a very good time it was there was a moocow coming down along the road.'.encode()

bob = libnacl.public.SecretKey()
alice = libnacl.public.SecretKey()

# in NaCl lingo, the box combines the sender's secret and the receiver's public
# keys
bob_box = libnacl.public.Box(bob.sk, alice.pk)
alice_box = libnacl.public.Box(alice.sk, bob.pk)

encrypted = bob_box.encrypt(msg)
decrypted = alice_box.decrypt(bob_ctxt)
