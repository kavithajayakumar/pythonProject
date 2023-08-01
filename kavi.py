print('hello')

class Project :
    def __init__(self,name, age):
        self.name= name
        self.age= age


    def __init__(self,name,no):
        self.name= name
        self.no= no


p= Project('kavi', '23')
#cl= p.age
print('name:', p.name)
#ca= p.no
c= Project('suba', '9840748212')
print('no:', c.name)

#to delete specified number
li= [1,34,5,546]
li.remove(1)
print(li)

#will delete specific index in the list
del li[2]
print(li)

#to change upper to lower and vice versa
st= "Kavitha"
print(st.swapcase())

#to remove whitespace
st1= "   kavi"
print(st1.strip())

#to remove python file/any file
import os
#os.remove("email.py")

# str to int
a= '3'
print(type(int(a)))

# str to list
s= " kavitha jayakumar"
print(str.split(s))


#lambda
a= lambda s: a^2
print(a)

from numpy import sqrt
def no_ky(n0):
    for i in range(2,int(sqrt(n0)) +1) :
        if n%i ==0:
            return 0
        else  :
            return 1

s= no_ky(33)
print(s)



