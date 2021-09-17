import numpy as np
import pyautogui as p
import time as t
import PIL
# handy functions

def find_index(my_list, my_item):
    
    # returns the indices at which the list has a particular value but can be replaced by the index() method. 
    indices = []
    for i in range(len(my_list)):
        if my_list[i] == my_item:
            indices.append(i)
    return indices

def sumIndexMultData(my_list):
    answer = 0
    for i in range( len(my_list)):
        answer += i*my_list[i]
    return answer

def sumData(my_list):
    #sums the data in a list. not needed: in-built sum() function
    answer = 0
    for i in my_list:
        answer += i
    return answer

def onlyType(my_list, the_type):
    # returns the data in a list of a given type. input type as a string
    dummy = []
    if the_type == "int":
         for elem in my_list:
            if type(elem) == int:
                dummy.append(elem)
    elif the_type == "str":
         for elem in my_list:
            if type(elem) == str:
                dummy.append(elem)
    elif the_type == "bool":
         for elem in my_list:
            if type(elem) == bool:
                dummy.append(elem)
    elif the_type == "float":
         for elem in my_list:
            if type(elem) == float:
                dummy.append(elem)
    return dummy

def reversed(my_list):
    Reverse = [ my_list[-i-1] for i in range(len(my_list))]
    return Reverse


# stats functions

def linReg(x_data, y_data):
    # returns linear regression coefficients [alpha, beta]. 
    n = len(x_data)
    A = np.zeros((n,2))
    for i in range(n):
        A[i,0] = i 
    A[:,1] = 1
    Atrans = np.zeros((2,n))
    for i in range(n):
        Atrans[0,i] = A[i,0]
        Atrans[1,i] = A[i,1]
    ATA = Atrans@A
    [alpha , beta] =np.linalg.solve(ATA, Atrans@y_data)
    return [alpha, beta]

def mean(my_list):
    return sumData(my_list)/len(my_list)

def brown(n):
    # return and plot a brownian motion sequence with n items.
    # if you want 0,1,2,3,4,.....,10 then you have to n=11 
    br = np.zeros(n)
    step = 1/np.sqrt(n)
    r = 0
    for i in range(1,n):
        coin_toss = 2*np.random.binomial(1,0.5)-1
        br[i] = r + step*coin_toss
        r = br[i]
    return br

def three_day_rolling(my_list):
    n = len(my_list)-2
    rolling = np.zeros(n)
    for i in range(n):
        rolling[i] = mean( [my_list[i], my_list[i+1], my_list[i+2] ])
    return rolling

def rolling_ave(my_list,r):
    n = len(my_list)-r+1
    rolling = np.zeros(n)
    for i in range(n):
        rolling[i] = mean( [my_list[i+j] for j in range(r)  ])
    return rolling

def get_pixel_colour(i_x, i_y):
    # taken from https://rosettacode.org/wiki/Color_of_a_screen_pixel#Python
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[i_x, i_y]

def wait_to_load(position,colour):
    while get_pixel_colour(position[0],position[1])!= colour:
        n = 0
    t.sleep(1)
    
def auto_sbi(account_code, numbers):
    BLUE = (51,102,153)
    WHITE = (255,255,255)
    for number in numbers:
        p.click(x=432, y=172)
        p.write(account_code)  # tpye in acct num
        p.click(1791,241) # click search
        wait_to_load((936,674),BLUE)
        p.press("enter") #click to process SBI doc
        wait_to_load((1097,767),BLUE)
        p.write(str(number))
        p.hotkey('alt', 's') # search for the iunvoice
        wait_to_load((902,610),WHITE)   
        p.click(1265,389)
        p.hotkey('alt', 'a')
        a = p.position()
        t.sleep(8)
        if get_pixel_colour(831,538) == (255, 255, 0):
            the_index = numbers.index(number)
            numbers = numbers[the_index+1:]
            p.press("enter")
            t.sleep(2)
            p.hotkey("alt","c")
            t.sleep(2)
            p.doubleClick(x=129, y=418)
            t.sleep(5)
            auto_sbi(account_code, numbers)
        wait_to_load((1012,168),WHITE)
        p.click(1664,417)
        wait_to_load( (859,694) , (255,255,192) )
        p.click(1069,587)
        wait_to_load( (1099,723), BLUE  )
        p.click(1252,723)
        wait_to_load( (859,694) , (255,255,192) )
        t.sleep(1)
        p.click(1436,909)
        wait_to_load((959, 700), WHITE)
        t.sleep(2)
        p.doubleClick(848,381)
        wait_to_load((1104, 612),BLUE)
        wait_to_load((581, 232),BLUE)
        t.sleep(2)
        p.doubleClick(x=1089, y=615)
        t.sleep(2)
        p.doubleClick(x=1089, y=615)
        t.sleep(2)

        

def log_on_vpn():
    p.doubleClick(145,294)
    wait_to_load((929, 559),(0, 120, 189))
    p.click(908, 695)
    p.write("matthew.young") #not my actualy username
    p.click(968,728)
    p.write("Uga#390DAN") #not my actual password
    p.press("enter")

