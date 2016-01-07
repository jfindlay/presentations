import os

msg = 'Once upon a time and a very good time it was there was a moocow coming down along the road.'.encode()

[c for c in msg]
key = os.urandom(len(msg))
[c for c in key]
[bin(c) for c in msg]
[bin(c) for c in key]
enc = [msg[i] ^ key[i] for i,c in enumerate(msg)]
enc
''.join([chr(c) for c in enc])
[enc[i] ^ key[i] for i, c in enumerate(msg)]
''.join([chr(enc[i] ^ key[i]) for i, c in enumerate(msg)])
