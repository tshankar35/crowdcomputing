#A List of Data
data=[100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,286,300,300,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720,1000,1010,1500,1786,2000]
#tr stores the new trimmed length of the data set by 10% of original length
tr=int(0.1*len(data))
#data is trimmed from starting according to the value set in tr
data=data[tr:]
#dta is trimmed from ending according to value set in tr
data=data[:(len(data)-tr)+1]
#data is sorted
data.sort()
from statistics import mean
#mean is calculated
est = mean(data)
print(est)
