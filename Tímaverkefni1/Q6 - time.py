secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
# hours =
hours = secs_int // 3600
# minutes =
minutes = secs_int % 3600 // 60
# seconds =
seconds = secs_int % 3600 % 60
print(hours,":",minutes,":",seconds) # do not change this line
