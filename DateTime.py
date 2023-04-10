# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 00:23:17 2023

@author: Korisnik
"""

from datetime import date
from datetime import time
from datetime import datetime
    
today = date.today ()
print("Today's date is", today)
    
print("Date components:", today.day, today.month, today.year )
  
    
# b)
  
  
print("Today's weekday is", today.weekday())
    
days = ["Monday","Tuesday","Wednesday","Thursday","Friday",
                             "Saturday","Sunday"]
today = date.today ()
print("Which is a ", days[today.weekday()])
   
# c) 
   
    
today=datetime.now()
    
print("Current date and time is", today )
 

#formating   
#%Y/%y = Year, %a / %A = weekday, %a/%A = month, %d = day of month
from datetime import datetime
now = datetime.now()

print(now.strftime("The current year is: %y"))
print(now.strftime("%a,%d %B, %y"))

print(now.strftime)

#%c - locale's date and time, %x = locale's date, %X = locale's time

print(now.strftime("Locale date and time: %c "))
print(now.strftime("Locale date: % x"))
print(now.strftime("Locale date: % X"))

#time formating
# %I/ $H -12/24 hour, %M - minute, %S - second, % p - Locale's AM / PM

print(now.strftime("Current time: %I:%M:%S:%p"))

#timedelta
#timedelta is span of time (not particular day, or particular month)

from datetime import timedelta

print (timedelta (days = 365, hours = 5, minutes = 1 ))

# b) 

now = datetime.now ()
print ("Today is", now)
print ("One year from now it will be", str (now + timedelta(days = 365) ))
print ("In two weaks and 3 days it will be", str (now + timedelta(weeks = 2, days = 3)))


# using date calculation with using a date in the past
from datetime import date
from datetime import time
from datetime import datetime
    
from datetime import timedelta
t = datetime.now() - timedelta(weeks = 1)
s = t.strftime("%A %B % d,%Y")

#How many days until April fools day
from datetime import date
from datetime import time
from datetime import datetime
    
from datetime import timedelta
today = date.today()
afd = (today.year,4,1)
if afd < today :
    print("April Fool's already went by:", ((today-afd).days ))
    afd = afd.replace (year = today.year + 1)
    
    time_to_afd = afd - today
    print ("It is ", afd.days, "days until April's fools day")
    
#working with calenders

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
#str = c.formatmonth(2023, 1)
#print(str)

#hc = calendar.HTMLCalendar(calendar.MONDAY)
#str = hc.formatmonth(2023, 1)
#print(str)


#calculate when the first friday happens in each month and calculate the date that represents that day
import calendar
print("Team meeting will be on: ")
for m in range (1,13):
    cal =calendar.monthcalendar(2023,m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] !=0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday: weektwo[calendar.FRIDAY]