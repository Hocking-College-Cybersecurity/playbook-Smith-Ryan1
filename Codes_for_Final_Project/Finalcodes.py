
import random
def unique_random_numbers(low,high,count):
    if count> (high - low + 1):
        raise ValueError ("Not Enough Numbers in range")
    return random.sample()
while True:
    Startup = int(input("If you would like a random number, please type '1'; if you wish to exit, type '0'"))
    if Startup in [1, 0]:
        if Startup == 0:
            break
        if Startup == 1:
            
    else:
        print("This input is invalid, please try again.")
        continue
