import time, sys, os, random
from colorama import Fore, Back, Style
from rich.progress import track

g_monero = 0.0
_stage = 0 
g_art = """
                  -===========-
             -=====================-
          -===========================-
        -===============================-
      -===================================-
    -=======================================-
   -=====+=============================+=====-
  -======   -=======================-   ======-
 -=======     -===================-     =======-
 ========       -===============-       ========
-========         -===========-         ========-
=========           -=======-           =========
=========     .       -===-       .     =========
-========     ::.       +       .::     ========-
 ========     ::::.           .::::     ========
              ::::::.       .::::::
              ::::::::.   .::::::::
              ::::::::::.::::::::::
   ...........:::::::::::::::::::::...........
    *:::::::::::::::::::::::::::::::::::::::*
      *:::::::::::::::::::::::::::::::::::*
        *:::::::::::::::::::::::::::::::*
          *:::::::::::::::::::::::::::*
              *:::::::::::::::::::*
                    *********
"""

os.system("clear")
print(g_art)


print(Fore.RED, "Program will start in 10 seconds", Style.RESET_ALL)
        
for i in track(range(1), description="Time Left"): #default value is 10
    time.sleep(1)



def mining():
    global g_monero
    global g_art
    ra = random.randint(10,100)
    
        
    for i in track(range(ra), description="Mining"):
        print(Fore.YELLOW, f"Value {Style.RESET_ALL} {g_monero}")
        g_monero += 0.01
        time.sleep(0.1)

for x in range(2):
    try:
        #save the monero to txt file
        """

        data conflict error.

        v = open("mywallet.txt", "r")
        print(v.readline())
        data = v.readline()
        print(data)
        data = int(data)
        print(type(data))

        #data = data.strip()
        data += g_monero
        print(g_monero)
        time.sleep(3)
        """
        mining()
        if g_monero > _stage:
            _stage += 1
            print(Style.RESET_ALL,Fore.GREEN, f"Stage {_stage}", Style.RESET_ALL)
            f = open("mywallet.txt", "w")
            f.write(str(g_monero))
            f.close()
    except Exception as errorr:
        print(errorr)
        sys.exit()


