import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('http://13.234.66.67/summer19/datasets/bank.csv')
df.info()

df['EstimatedSalary'].plot(kind='hist')
df['EstimatedSalary'].plot(kind='kde')
x=df['EstimatedSalary']
y=df['Age']
df.plot.scatter(x='EstimatedSalary',y='Age' )
plt.xlabel('EstimatedSalary')
plt.ylabel('Age')
plt.plot(x,y)
df['EstimatedSalary'].plot(kind='pie')


m=0
f=0
#for Male in df['Gender']:
 #       m=m+1
for i in df['Gender']:
    if i=='Male':
        m=m+1
    else:
        f=f+1
    
#print(m,f)

Gender=['Male','Female']
NMF=[m,f]
plt.pie(NMF,labels=Gender, shadow=True,autopct='%1.1f')



fr=0
sp=0
ger=0
#for Male in df['Gender']:
 #       m=m+1
for i in df['Geography']:
    if i=='France':
        fr+=1
    elif i=='Spain':
        sp+=1
    else:
        ger+=1
    
#print(m,f)

Geo=['France','Spain','Germany']
Count=[fr,sp,ger]
plt.pie(Count,labels=Geo, shadow=True,autopct='%1.1f')
