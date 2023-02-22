import datetime

x = datetime.datetime.now()

# Write a Python program to calculate two date difference in seconds.


date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')  #strptime used to convert string to date

date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')


differ = (date2 - date1).total_seconds()

#result
print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", differ)
