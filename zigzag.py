# This program creates a small animation zigzag

import time, sys

def zigzag1():
    print('    *******')
    time.sleep(0.1)
    zigzag2()  

def zigzag2():
    print('   *******')
    time.sleep(0.1)
    zigzag3()

  
def zigzag3():
    print('  *******')
    time.sleep(0.1)
    zigzag4()

    
def zigzag4():
    print(' *******')
    time.sleep(0.1)
    zigzag5()
  

def zigzag5():
    print('*******')
    time.sleep(0.1)
    zigzag6()

def zigzag6():
    print(' *******')
    time.sleep(0.1)
    zigzag7()  

def zigzag7():
    print('  *******')
    time.sleep(0.1)
    zigzag8()

  
def zigzag8():
    print('   *******')
    time.sleep(0.1)
    zigzag9()

    
def zigzag9():
    print('    *******')
    time.sleep(0.1)
    zigzag2()

try:
    zigzag1()

except KeyboardInterrupt:
    sys.exit()
    
  


   
    

