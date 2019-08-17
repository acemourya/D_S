#numpy: numerical python which provides function to manage multiple dimenssion array
#array : collection of similar type data or values

import numpy as np

#create array from given range
x = np.arange(1,10)
print(x)

y = x*2
print(y)


#show data type
print(type(x))
print(type(y))


#convert list to array
d = [11,22,4,45,3,3,555,44]
n = np.array(d)
print(n)
print(type(n))

print(n*2)

##change data type
n = np.array(d,dtype=float)
print(n)

#show shpae
print(n.shape)


#change demenssion
n = np.array(d).reshape(-1,2) #read from 1st element , 2 two dimenssion
print(n)

d = [11,22,4,45,3,3,555,44,3]
n = np.array(d).reshape(-1,3) #read from 1st element , 3 dimenssion
print(n)


#generate the array of zeors
print(np.zeros(10))


#generate the array of ones
print(np.ones(10))


#matrix or two dimession array and operation

x = [[1,2,3],[5,6,7],[66,77,88]] #list
y = [[11,20,3],[15,26,70],[166,707,88]] #list

#convert to array 
x = np.array(x)
y = np.array(y)

print(x)
print(y)


#addition
print(np.add(x,y))
print(np.subtract(x,y))
print(np.divide(x,y))
print(np.multiply(x,y))












