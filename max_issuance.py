# Original block reward for miners was 50 BTC
start_block_reward = 50

# 210,000 is around every 4 years given a 10 minute block iterval
reward_interval = 210000

def max_money():
    # 50 BTC is 50,000,000 Satoshis
    current_reward = 50 * 10**8
    total = 0
    while current_reward > 0:
        total += current_reward * reward_interval
        current_reward /= 2

    return total

print("Total issuance is {0} Satoshis".format(max_money()))
