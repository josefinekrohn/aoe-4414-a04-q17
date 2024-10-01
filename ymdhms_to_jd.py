# ymdhms_to_jd.py
#
# Usage:  python3 ymdhms_to_jd.py year month day hour minute second
#  Converts year, month, day, hour, minute, second to fractional Julian date
# Parameters:
#  year: year-component of time
#  month: month-component of time
#  day: day-component of time
#  hour: hour-component of time
#  minute: minute-component of time
#  second: second-component of time
#  ...
# Output:
#  #  Prints the fractional Julian date
#  Inputs time in year, month, day, hour, minute, second and prints out fractional Julian date
#
# Written by Josefine Krohn
# Other contributors: Brad Denby (format) 
#

# import Python modules
import math # math module
import sys # argv

# "constants"
#  n/a 

# helper functions

## integer division with truncation toward zero
def intdiv(num,den):
    if (num//den) > 0:
        return (num//den)
    else:
        return (num//den)+1


# initialize script arguments
year = float('nan') # year-component of time
month = float('nan') # month-component of time
day = float('nan') # day-component of time
hour = float('nan') # hour-component of time
minute = float('nan') # minute-component of time
second = float('nan') # second-component of time

# parse script arguments
if len(sys.argv)==7:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()





# write script below this line


JD = day - 32075 + intdiv(1461*(year + 4800 + intdiv(month - 14, 12)), 4) + intdiv(367*(month - 2 - 12*intdiv(month - 14, 12)), 12) - intdiv(3*intdiv((year + 4900 + intdiv(month - 14, 12)), 100), 4)

JD_midnight = JD - 0.5

D_fractional = (second + 60*(minute + 60*hour))/86400

JD_fractional = JD_midnight + D_fractional
jd_frac = JD_fractional

print(jd_frac)