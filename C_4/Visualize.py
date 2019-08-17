import os
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Anurag\Desktop\D_S\C_2\employee.csv')

print(data)


gender=['F','M','M','M']
country=['India','Chin','India','Dubai']
basic=[200,300,400,500]

#HRA
HRA=[]
for x in basic:
    HRA.append(x*.4)

# DA
DA=[]
for j in basic:
    DA.append(j*.2)   


# Add new cloumn in datafame
data['Gender']=gender
data['Country']=country
data['Basic_Sal']=basic
data['HRA']=HRA
data['DA']=DA

print(data)
#show graph for every numeric column
#data.plot() #default graph type is line or relational graph by plot('col1','col2')

#data.plot(kind='bar')
#data.plot(kind='box')

#data.plot(kind='line',subplots=True)
'''
data.plot(kind='line',subplots=True,layout=(1,4))

plt.show()
'''


####
'''
SID NAME  HS ES CS MS  TOTAL ? AVG? 
1    RAMAN  77 88  99  
'''

hs=[200,300,400,500]
cs=[100,600,300,800]
es=[300,400,500,900]
ms=[400,300,700,200]


total=[]
avg=[]
for i in range(0,len(basic)):
        t =basic[i]+hs[i]+cs[i]+es[i]+ms[i]
        total.append(t)
        a = t / 5
        avg.append(a)#basic[i]+hs[i]+cs[i]+es[i]+ms[i]/5)
        

#total=data.groupby('Country').sum()['Basic_Sal']


data["HS"]=hs
data["ES"]=es
data["CS"]=cs
data["MS"]=ms
data["Total"]=total
data['Avg']=avg
a=pd.DataFrame(data)
print(a)

nd = a[['name','Gender','Avg']]
print(nd)

import matplotlib.pyplot as plt
import numpy as np

nd.plot(kind='bar',color='red')
#b=nd.plot(kind='bar',color='red')
#nd.set_hatch('/')
#plt.bar(ypos,revnue, label='revenu')
#plt.bar(ypos,profile, label='profile')



fig, ax = plt.subplots()    
width = 0.25 # the width of the bars 
ind = np.arange(len(avg))  # the x locations for the groups
ax.barh(ind, avg, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(es, minor=False)
plt.title('title')
plt.xlabel('es')
plt.ylabel('avg')   



plt.xlabel('X label')
#b.set_yticks(rotation='vertical')
plt.ylabel('Y Label')
plt.legend('top right')

plt.show()
plt.savefig(os.path.join('test.png'), dpi=300, format='png', bbox_inches='tight')








