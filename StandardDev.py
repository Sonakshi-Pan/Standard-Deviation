import csv
import math
with open("Standard.csv",newline="") as f:
    r = csv.reader(f)

    data=list(r)

#print(data) 



new_data = []
 
for i in range(len(data[0])):
   n = data[0][i]

def mean(d):
    total =0
    l=len(d)

    for j in d:
      total +=j

    mean=total/l

    return mean

sq = []

for i in new_data:
    dif=float(i) - mean(new_data)
    s =dif**2
    sq.append(s)

result=mean(sq)

stand=math.sqrt(result)
print(stand)







