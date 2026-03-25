'''Traffic light simulation'''


import time

def trafic_signal(red=30, green=30, yellow=5):
    try:    
        while True:    
            print("🔴🔴🔴  Stop  ",end="\r")
            time.sleep(red)
            print("🟢🟢🟢  Go",end="\r")
            time.sleep(green)  
            print("🟡🟡🟡  Wait",end="\r")
            time.sleep(yellow)
    except KeyboardInterrupt:
        print("\nTraffic light stopped.")

trafic_signal()  

  