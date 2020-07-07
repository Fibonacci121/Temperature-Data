import matplotlib.pyplot as pt

time_len = input("What is the time span for this data (day,week,month,year)")
temp = None

temps = []

if time_len == 'day':

    for i in range(24):
        t = int(input("Enter the temperature by the hour"))
        temps.append(t)
if time_len == 'week':

    for i in range(7):
        t = int(input("Enter the temperature by the day"))
        temps.append(t)
if time_len == 'month':

    for i in range(30):
        t = int(input("Enter the temperature by the day"))
        temps.append(t)
if time_len == 'year':

    for i in range(365):
        t = int(input("Enter the temperature by the month ( avg )"))
        temps.append(t)

pt.plot(temps)
pt.ylabel('temperatures')
pt.show()
