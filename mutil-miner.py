import threading
from mining import mine
import math
from pathlib import Path
from coil.wallet import readWallet


def primeNumber(count):
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
            
        if isprime:
            return(str(count))
            
        count += 1
    

def main():
    WALLET_FOLDER = str(Path.home()) + "/.config/coil/wallets/"
    miner = readWallet(WALLET_FOLDER + "master.json")

    print("Wallet address: " + miner.address)
    print("welcome to hacky miner2")
    print("we be mining all t'day")

    threads = 40
    
    for i in range(1, threads):
        threading.Thread(target=mine, args=(primeNumber(i*10^i),)).start()
        


main()
