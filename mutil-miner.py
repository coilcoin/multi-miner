import threading
from mining import mine
import math

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
    
    print("welcome to hacky miner2")
    print("we be mining all t'day")

    threads = int(input("How many threads would you like to use? "))

    for i in range(1, threads):
        threading.Thread(target=mine, args=(primeNumber(i*10^i),)).start()
        


main()
