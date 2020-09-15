'convert second into hrs minute and sec'

import math

seconds = int(input("Enter the time in seconds: "))

hr = math.trunc(seconds / 3600)
minute = math.trunc(seconds/60 - hr*60)
sec = math.trunc(seconds - (minute*60 + hr*3600))

print (hr,"Hr:",minute,"Min:",sec,"Sec")