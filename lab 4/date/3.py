import datetime

x = datetime.datetime.now()
# Write a Python program to drop microseconds from datetime.

print()
print()
print()


DateWithoutMicro = x.replace(microsecond=0)

print(DateWithoutMicro)
