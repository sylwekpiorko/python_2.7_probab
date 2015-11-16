import random
# test od Piotrka v2 - v3 od Piotrka
dates = []
for i in range (50):
    a = int(random.random()*365)
    dates.append(a)
    
# print dates
dlugosc=len(dates)
    
datesSorted = sorted(dates)
# print datesSorted


dubel = 0

for i in range(dlugosc-1):
    pierwsza = datesSorted[i]
    druga = datesSorted[i+1]
    
    if pierwsza == druga:
        dubel += 1
        break
            

print 'Jest dubelek ', pierwsza
