from datetime import datetime
now = datetime.now()
print("{}/{}/{}".format(now.day, now.month, now.year)) 
print("{}:{:0>2d}:{:0>2d}".format(now.hour, now.minute, now.second))  