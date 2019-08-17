import pandas as pd

#pip install sklearn
from sklearn.linear_model import LinearRegression

age = [3,4,5,6,4,5,6,8,9,10,5,10,7]
gender = [1,1,0,1,0,1,1,1,0,0,0,1,0]
wt = [12,14,16,10,14,18,25,19,31,13,8,32,18]
name=['Aman','Ace','Yashi','Anu','Parul','Akash','Rahul','Anurag','Yashika','Aarti','Sandhya','Abhi','pooja']
hour=[2,3,4,7,5,6,8,5,3,7,4,6,5]
score=[20,30,40,50,45,55,30,35,50,25,48,58,49]

child = pd.DataFrame(data={'Name':name,'Age':age,'Gender':gender,'WT':wt,'Hour':hour,'Score':score})

# Save data in CSV file
child.to_csv('LR.csv')
print(child)

# Read data CSV file 
child_r=pd.read_csv(r'C:\Users\Anurag\Desktop\D_S\C_5\LR.csv')

#Extract y and x attribuates
y = child_r['WT']
x = child_r[['Age','Gender']]

print(x)
print(y)


import numpy as np

h=child_r['Hour']    # h=child_r[['Hour']]
h = np.arange(len(h)).reshape(-1,1)  # reshape(-1,1) : -1 for give data shape line by line of column data and 1 for col select 

s=child_r['Score']

##corr
print(child_r.corr())



o = LinearRegression()
#o.fit(x,y)
o.fit(h,s)

print(o.intercept_)
print(o.coef_)


##predict the weight based on age and gender
#take input from user
#nage = int(input('enter age :'))
#ngen = int(input('press 1 for male and 0 for female :'))
nhour=int(input('Enter the hour of worker work :'))

#print('Exptect  wt for given age and gender :',o.predict([[nage,ngen]]))
print('Expect score accoring to hour :',o.predict([[nhour]]))
      
          
'''
Apply regression model for dataset
sid   name   hours    score
1    nitin   5        45

'''










