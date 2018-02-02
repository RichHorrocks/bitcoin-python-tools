import hashlib
import time

max_nonce = 2 ** 32 # ~4 billion

def proof_of_work(header, difficulty_bits):
    # Calculate the difficulty target.
    target = 2 ** (256 - difficulty_bits)

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header) + str(nonce)).hexdigest()

        # Check if this is a valid result - i.e. below the target.
        if long(hash_result, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hash_result)
            return (hash_result, nonce)

    print("Failed after %d (max_nonce) tries" % nonce)

if __name__ == '__main__':
    nonce = 0
    hash_result = ''

    # Let's run some tests at different difficulties.
    for difficulty_bits in xrange(32):
        difficulty = 2 ** difficulty_bits
        print("Difficulty %ld (%d bits)" % (difficulty, difficulty_bits))
        print("Searching...")

        # Checkpoint the current time.
        start_time = time.time()

        # Make a new block which includes the hash from the previous block.
        # To do this, we fake a block of transactions - we just use a string,
        # and make it different each time, not by adding new transactions, but
        # by including the previous hash result.
        new_block = 'test block with transactions' + hash_result

        # Find a valid nonce for the new block.
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

        # Checkpoint how long it took to find the PoW.
        end_time = time.time()

        elapsed_time = end_time - start_time
        print("Elapsed time: %.4f seconds" % elapsed_time)

        if elapsed_time > 0:
            # Estimate the number of hashes per second.
            hash_power = float(long(nonce) / elapsed_time)
            print("Hashing power: %ld hashes per second" % hash_power)
