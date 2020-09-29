# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter month (first 3 characters, \'Jan\', \'Feb\', etc): ').upper()
if len(month) != 3:
  print('Enter the first three letters of the month, you dingus!')
  month = input('Enter month (first 3 characters, \'Jan\', \'Feb\', etc): ').upper()

day = int(input('Enter day: '))
if month == 'DEC' and day >= 21 or month == 'JAN' or month == 'FEB' or month == 'MAR' and day <= 19:
  season = 'Winter'
elif month == 'MAR' and day >= 20 or month == 'APR' or month == 'MAY' or month == 'JUN' and day <= 20:
  season = 'Spring'
elif month == 'JUN' and day >= 21 or month == 'JUL' or month == 'AUG' or month == 'SEP' and day <= 21:
  season = 'Summer'
elif month == 'SEP' and day >= 22 or month == 'OCT' or month == 'NOV' or month == 'DEC' and day <= 20:
  season = 'Fall'
else:
  print('Type a valid month and date, please!')
print(f'{month} {day} is in {season}')