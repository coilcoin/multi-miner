import threading
from mining import mine

def main():
    
    print("welcome to hacky miner2")
    print("we be mining all t'day")
    
    t1 = threading.Thread(target=mine, args=("1",))
    t2 = threading.Thread(target=mine, args=("27",))
    t3 = threading.Thread(target=mine, args=("97",))
    t4 = threading.Thread(target=mine, args=("193",))
    t5 = threading.Thread(target=mine, args=("941",))
    t6 = threading.Thread(target=mine, args=("571",))
    t7 = threading.Thread(target=mine, args=("409",))
    t8 = threading.Thread(target=mine, args=("719",))

    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
        
main()
    


