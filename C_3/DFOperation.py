##dataframe operation

import pandas as pd

data = pd.read_csv(r'C:\Users\Anurag\Desktop\D_S\C_2\employee.csv')

print(data)



#convert dataframe to series or array
d = data.values

print(d)


#read data by index
print(d[:,:])  #row1  : row .. ,  col2 : col44
print(d[0:3,:])  #row 0,1 2 , and all columns

print(d[:,0])  #all rows and selected cols

#order by
print(data.sort_values('name',ascending=True))
print(data.sort_values('name',ascending=False))


#group by
print(data.groupby('name').size())

print(data.groupby('name').sum())
print(data.groupby('name').max())
print(data.groupby('name').min())

print(data.groupby('name').max()['eid'])

#print(data.groupby('name').max()[['eid','']])




'''
Q. eid name gender country basic hra da 


Q. show highest, lowest and total salary per country and write the result in new .csv file

'''

gender=['F','M','M','M']
country=['India','Chin','India','Dubai']
basic=[200,300,400,500]

#HRA
HRA=[]
for x in basic:
    HRA.append(x*.4)
print(type(HRA))    

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

a=pd.DataFrame(data)


#b={'eid':4,'name':'Asha','Gender':'F','Country':'Delhi','Basic_Sal':400,'HRA':200,'DA':500}
#dff=pd.DataFrame(b)


print(data.groupby('Country').max()['Basic_Sal'])
print(data.groupby('Country').min()['Basic_Sal'])
print(data.groupby('Country').sum()['Basic_Sal'])



#x = [data,b]

#print(x)
#print(data.shape)
#print(dff.shape)

#print(x.shape)




#save emp data to csv file
#a.to_csv('employeess.csv',index=False)
#print('data is saved')
#print(a)

#data

print(a)
print(data)

x = [a,data]
print(x)
print(type(x))

x = pd.concat(x)
print(x)
print(x.shape)









