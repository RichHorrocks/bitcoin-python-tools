# A very simple example of how iterating a nonce changes a hashing
# algorithm's output.

import hashlib

text = "I am Satoshi Nakamoto"

for nonce in xrange(20):
    # Add the current nonce to the input string.
    input = text + str(nonce)

    # Calculate the SHA-256 of the input.
    hash = hashlib.sha256(input).hexdigest()

    # Show the input and hash result.
    print("{0} => {1}".format(input, hash))
