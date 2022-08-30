 # Datum
 # https://open.kattis.com/problems/datum
 
import calendar
year=2009
i=str(input())
s=i.split()
date=s[0]
month=s[1]
d=calendar.weekday(year,int(month),int(date))
print(calendar.day_name[d])
