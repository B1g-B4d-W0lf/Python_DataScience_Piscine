import time
from datetime import datetime

i = time.localtime()
y = time.mktime(i)
u = time.time()

print("Seconds since January 1, 1970:",
      f"{u:,.4f}", "or", "{:.2e}".format(u), "in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
