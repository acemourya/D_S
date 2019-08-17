import os


#return list of all files or directory
files = os.listdir(r'C:\Users\vkumar15\Documents')

print(files)

#get files and folder count
print(len(files))


#iterate file one by one
for f in files:
     print(f)


#get count of all .txt files
c = 0
for f in files:
     if f.endswith('.txt'):
          c +=1

print(c)

     
#get count of all .py files
c = 0
for f in files:
     if f.endswith('.py'):
          c +=1

print(c)


###read all txt files and write the content in another file

nf = open('all_content.txt','w') #w : create new file in wirte mode

for f in files:
     if f.endswith('.txt'): #if txt file 
          r = open(r'C:\Users\vkumar15\Documents\\'+f) #read the file  #error ... need full path of file  
          
          nf.write(r.read()) #write to new file 
          nf.write('------------------------------------') #write seperator 
          
nf.close() #save the file 

print('all text file content is saved in new file')





     






