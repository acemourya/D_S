import os
import shutil #copy or move or remove the file

#return list of all files or directory
files = os.listdir(r'C:\Users\vkumar15\Documents')

#copy all .txt files to other location
#shutil.copy(src,dest)
#shutil.move(src,dest)
#shutil.unlink(src)


for f in files:
     if f.endswith('.txt'):
          shutil.copy(r'C:\Users\vkumar15\Documents\\'+f,r'C:\Users\vkumar15\Desktop\Content')



print('all txt files are copied')

