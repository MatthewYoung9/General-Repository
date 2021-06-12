import numpy as np
# handy functions
def find_index(my_list, my_item):
    # returns the indices at which the list has a particular value
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
    #sums the data in a list
    answer = 0
    for i in my_list:
        answer += i
    return answer

def onlyint(my_list):
    dummy = []
    for elem in my_list:
        if type(elem) == int:
            dummy.append(elem)
    return dummy

def reverse(my_list):
    Reverse = [ my_list[-i-1] for i in range(len(my_list))]
    return Reverse


# stats functions

def linReg(x_data, y_data):
    # returns linear regression coefficients [alpha, beta]
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

print(rolling_ave([1,2,3,4,5],3))
