from calendar import *
from datetime import date
y,m,d = map(int,input('Enter year , month and date of your birth:').split())
dob = date(y,m,d)
curr_date = date.today()
age = ((curr_date - dob).days)//365
print('Your age is',age)
