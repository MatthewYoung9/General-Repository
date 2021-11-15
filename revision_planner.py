import datetime as dt
from random import sample
import math

def allocate(the_thing, the_list, the_index):
    # 
    dummy_1 = the_list[:the_index]
    dummy_2 = the_list[the_index +1 :]
    return dummy_1 + [the_thing] +dummy_2

def upto(my_list, element):
    critical_point = my_list.index(element)
    return my_list[:critical_point]

def onlyint(my_list):
    dummy = []
    for elem in my_list:
        if type(elem) == int:
            dummy.append(elem)
    return dummy


# Set year
y = 2021
# Here list all the names of the modules for which you have exams
modules = ["Spanish", "German", "AMMT","Stats", "Project","Free"]


# Then list the dates that you have these exams on 

sp = dt.date(y, 12, 17)
ge = dt.date(y ,12, 18)
ammt = dt.date(y, 12, 19)
stat = dt.date(y, 12, 20)
proj = dt.date(y, 12, 21)
free = dt.date(y,12,22)


dates = [sp,ge,ammt,stat,proj,free]

# Now give weights. 
# If I spent t_1 hours on module 1
# I want to spend t_2 hours on subject 2 etc.

weights = [10,15,30,30,40,15]
weight_sum = sum(weights)

# now merge all this info you've just put in 

merged = [modules, dates, weights]
# When is the date you wish to start revising?

start = dt.date(y, 11, 15 )

# I then start the process of dividing up the schedule. I start with 
# splitting up each day into two half days from the start day to the very last exam
# I then fill in the days with an exam so that no revision may take 
# place on these days. I also allow for allocation of free days

frees = []
slots = (abs(max(dates)- start).days + 1)*2
subject_slot = [math.floor( slots*i/weight_sum  ) for i in weights]
timespan = slots*["Empty"]

# Allcoate what you want

preplanned = [("Spanish",0),("Stats",1), ("Stats",2)]

for i in preplanned:
    timespan[i[1]]= i[0]
# Allocate exams. Note this this overrides exams that occur on the same day

for i in range( len(modules)):
    timespan[((abs(merged[1][i] - start ).days) )*2 ] = merged[0][i]+ " Exam"
    timespan[((abs(merged[1][i] - start ).days) )*2 +1 ] = merged[0][i]+ " Exam"
    


# Allcoate frees

for i in frees:
    timespan[i] = "Free"


# Find the unallocated spots

empty_spots = []
for i in range(slots):
    if timespan[i]== "Empty":
        empty_spots.append(i)
        
subject_slot = [math.floor( len(empty_spots)*i/weight_sum  ) for i in weights]

# Allocate revision slots

for i in range(len(modules)):
    module = modules[i]
    possible_slots = [j*(j < ((abs(dates[i] - start ).days) )*2) for j in empty_spots ]
    to_allocate = sample(possible_slots, subject_slot[i])
    for time in to_allocate:
        timespan[time] = module
        empty_spots.remove(time)

print(timespan)

# Displaying timetable in a nice way

for t in range(int(slots/2)):
    print(str (start + dt.timedelta(days=t)) + " " +str(timespan[2*t])+ " " + str(timespan[2*t+1]) )


    

            
    




