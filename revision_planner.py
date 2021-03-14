import datetime as dt
import random 

def summit(my_list):
    # returns the sum of items in a list
    ans = 0 
    for i in my_list:
        ans += i
    return ans
def allocate(the_thing, the_list, the_index):
    # 
    dummy_1 = the_list[:the_index]
    dummy_2 = the_list[the_index +1 :]
    return dummy_1 + [the_thing] +dummy_2

def upto(my_list, element):
    for i in range(len(my_list)):
        if my_list[i] == element:
            crit = i-1
            pass
        pass
    new_list = [my_list[i] for i in range(crit) ]
    return new_list

def onlyint(my_list):
    dummy = []
    for elem in my_list:
        if type(elem) == int:
            dummy.append(elem)
    return dummy



# Set year
y = 2021
# Here list all the names of the modules for which you have exams
modules = ["Num", "Biomath", "Ecology", "Decision", "Finance", "German", "Japanese"]


# Then list the dates that you have these exams on 

nm = dt.date(y, 4, 26)
bm = dt.date(y ,5, 5)
ec = dt.date(y, 5, 20)
dr = dt.date(y, 4, 29)
fi = dt.date(y, 5, 13)
ge = dt.date(y, 5, 18)
ja = dt.date(y, 5, 11) 

dates = [nm, bm, ec, dr, fi, ge, ja]


# Now give weights. 
# If I spent t_1 hours on module 1
# I want to spend t_2 hours on subject 2 etc.

weights = [20,15,14,15,15,5,8]
weightSum = summit(weights)

# now merge all this info you've jsut put in 

merged = [modules, dates, weights]
# When is the date you wish to start revising?

start = dt.date(y, 4, 5 )

# I then start the process of dividing up the schedule. I start with 
# splitting up each day into two half days from the start day to the very last exam
# I then fill in the days with an exam so that no revision may take 
# place on these days. I also allow for allocation of free days

frees = []
slots = (abs(max(dates)- start).days + 1)*2

timespan = [i for i in range(slots)]

# allocate exams

for subject in range(len(modules)):
    timespan = allocate( merged[0][subject]+ " Exam", timespan, ((abs(merged[1][subject] - start ).days) )*2    )
    timespan = allocate( merged[0][subject]+ " Exam", timespan, ((abs(merged[1][subject] - start ).days) )*2  +1  )
    if type(timespan[((abs(merged[1][subject] - start ).days) )*2 -1]) == int:
        timespan[((abs(merged[1][subject] - start ).days) )*2 -1] = merged[0][subject]
        merged[2][subject] -= 1


# allocate frees 

for i in range(len(frees)):
    timespan = allocate("free", timespan, frees[i])


    
    
# Number of unallocated spots

unallocatedspots = len(onlyint(timespan))

# Now it's time to change weights into times. 

for i in range(len(modules)):
    merged[2][i] = math.floor(merged[2][i]*unallocatedspots / weightSum )
    
# # This is now where the magic happens. We take the schedule and 
# # the slots which are unallocated which lie before the exam.
# # we then allocate the days 


for i in range(len(modules)):
    toAlloc = onlyint(upto(timespan, merged[0][i] + " Exam"))
    toSet = random.choices(toAlloc, k= merged[2][i])
    for j in toSet:
        timespan = allocate(merged[0][i] , timespan, j)

for i in range(len(timespan)):
    if type(timespan[i]) == int :
        timespan[i] = "free"
        
print(timespan)
    


    

            
    




