import datetime

x = datetime.datetime.now()
# Write a Python program to print yesterday, today, tomorrow.


print(x - datetime.timedelta(days=1))
print((x - datetime.timedelta(days=1)).strftime("%A"))
print(datetime.datetime.now())
print(x.strftime("%A"))
print(x + datetime.timedelta(days=1))
print((x + datetime.timedelta(days=1)).strftime("%A"))
