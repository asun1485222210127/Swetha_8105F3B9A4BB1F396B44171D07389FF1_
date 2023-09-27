def isLeapYear(Year):
  if(Year%4==0 and Year %100!=0) or Year%400==0:
    return True
  else:
    return False 
Year=int(input("Enter a year:"))
if isLeapYear(Year):
  print('{} is a leap year,',format(Year))
else:
  print('{} is not a leap year,', format(Year))