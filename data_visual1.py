import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
df=pd.read_csv('student.csv')
df
name=['chetan','bhavya','aryan','anuj']
NMF=df['Marks']
#df['Marks'].plot(kind='pie')
Age=df['Age']
SH=df['Study_Hours']
#plt.pie(Age,labels=name, shadow=True)
plt.pie(SH,labels=name, shadow=True,autopct='%1.1f')
#plt.pie(NMF,labels=name, shadow=True,autopct='%1.1f')
