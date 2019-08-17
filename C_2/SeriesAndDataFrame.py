## Series and DataFrame
'''
DataFrame methods:
    -info()  return data type of very series or column and is null?
    -shape
    -columns
    -describe()
    -head()
    -tail()
'''

#read the file and show number of rows and total salary 

import pandas as pd

#create empty or blank dataframe

df = pd.DataFrame()

print(df)
print(type(df))

#convert list to dataframe
eid =[1,2,3,5]
name=['divya','ayush','mohit','Raman']

emp = pd.DataFrame(data={'eid':eid,'name':name})
print(emp)


#show columns
print(emp.columns)


#print top 2 rows, default count is 5
print(emp.head(2))

#from buttom
print(emp.tail(3))


#read selected column
print(emp['name'])
#read multiple column
print(emp[['name','eid']])



#save emp data to csv file
emp.to_csv('employee.csv',index=False)
print('data is saved')

#read the csv file
data=pd.read_csv(r'C:\Users\Anurag\AppData\Local\Programs\Python\Python37\employee.csv')
print(data)

#count number of rows
import statistics as s
print('number of rows:',s.count(emp))


#insert new clumn in emp dataframe datble
Sal=[2000,3000,4000,5000]
emp['Sal']=Sal          #table_name['New_col_name']=list
print(emp)









