#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[2]:


if 5 > 2:
    print("Five is greater than two")


# In[5]:


x = 5
y = "Hello World"
print(x)
print(y)


# In[6]:


#comment
print("Hello world")


# In[7]:


print("hello world") #comments


# In[8]:


#print("Hello, WOrld")
print("KBTU student")


# In[9]:


#comment
#also comment
#comment too
print("it is not multicomment")


# In[10]:


"""
comment
also comment
comment too
"""
print("it is multicomment")


# In[11]:


x = 5
y = "John"
print(x)
print(y)


# In[12]:


x = 5 #integer
x = "John" #now x is string type
print(x)


# In[13]:


x = str(3) #x is str type "3"
y = int(3) #y will be 3
z = float(3) # will be 3.0
print(x)
print(y)
print(z)


# In[14]:


x = 5
y = "John"
print(type(x))
print(type(y))


# In[16]:


x = "John"
# "__" the same as '__'
x = 'John'
print(x)


# In[18]:


a = 4
A = "Sally"
print(a)
print(A)
#not same registers


# In[19]:


myvar= 'John'
my_var='john'
_my_var='john'
myvar2='john'
MYVAR='john'
myVar='john'
print(myvar)
print(my_var)
print(_my_var)
print(myvar2)
print(MYVAR)
print(myVar)


# In[21]:


#CamelCase
myVariableName='john'
#Pascal case
MyVariableName='john'
#SnakeCase
my_variable_name='john'
print(myVariableName)
print(MyVariableName)
print(my_variable_name)


# In[23]:


x, y, z = 'banana', 'smoke', 'computer'
print(x)
print(y)
print(z)
#Make sure the number of variables matches the number of values, or else you will get an error


# In[24]:


x = y = z = 'banana'
print(x)
print(y)
print(z)


# In[26]:


#unpacking
fruits = ['banana', 'cherry', 'apple']
x,y,z = fruits
print(x)
print(y)
print(z)


# In[27]:


x = 'Python is awesome'
print(x)


# In[28]:


x = 'python'
y = 'is'
z = 'awesome'
print(x,y,z)


# In[31]:


x = 'python '
y = 'is '
z = 'awesome '
print(x+y+z)


# In[33]:


x = 5
y =10
print(x+y)


# In[34]:


x = 5
y = 'john'
print(x+y)


# In[35]:


x = 5
y = 'john'
print(x,y)


# In[37]:


x = 'awesome'
def myfunc():
    print('python is ' + x)
myfunc()


# In[39]:


x = 'awesome' #global var
def myfunc():
    x = 'fantastic' #local var
    print ("python is " + x)
myfunc()

print('python is '+ x)


# In[40]:


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[41]:


x = 5
print(type(x))


# In[42]:


x = 20
print(type(x))


# In[43]:


x = 20.6
print(type(x))


# In[44]:


x = 'john'
print(type(x))


# In[55]:


x = ['apple' , 'banana', 'cherry']
print(x)
print(type(x))


# In[54]:


x = 1j
print(x)
print(type(x))


# In[53]:


x = ('banana' , 'apple', 'cheerry')
print(x)
print(type(x))


# In[56]:


x = range(5)
print(x)
print(type(x))


# In[58]:


x = {'name' : 'john', 'age' : 35}
print(x)
print(type(x))


# In[59]:


x = {'name', 'john', 'age'}
print(x)
print(type(x))


# In[60]:


x = frozenset({'apple', 'banana', 'cherry'})
print(x)
print(type(x))


# In[62]:


x = True
print(x)
print(type(x))


# In[63]:


x = b'hello'
print(x)
print(type(x))


# In[64]:


x = bytearray(5)
print(x)
print(type(x))


# In[67]:


x = memoryview(bytes(5))
print(x)
print(type(x))


# In[68]:


x = None
print(x)
print(type(x))


# In[69]:


x = 1
y = 97979797979784521215445151
z = -21454512112
print(type(x))
print(type(y))
print(type(z))


# In[70]:


x = 1.0
y = 56446.025656
z = -34659.0254848
print(type(x))
print(type(y))
print(type(z))


# In[71]:


x = 14e5
y = 77E7
z = -355.45e445
print(type(x))
print(type(y))
print(type(z))


# In[72]:


x = 3 +5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))


# In[73]:


x = 1 #int
y = 4.4 #float
z = 5j #complex

a = float(x)
b = int(y)
c = complex(x)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))


# In[74]:


import random
print(random.randrange(1,10))


# In[75]:


x = int(1)
y = int(2.88)
z = int('346')
print(x)
print(y)
print(z)


# In[76]:


x = float(1)
y = float(3.333)
z = float("46")
c = float("345.566")
print(x)
print(y)
print(z)
print(c)


# In[77]:


x = str('grjrk')
y = str(2)
z = str(3.595)
print(x)
print(y)
print(z)


# In[83]:


a = """Lorem
consectetur adipiscing eli
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)


# In[84]:


a = 'hello, world'
print(a[1])


# In[87]:


for x in 'banana':
    print(x)


# In[88]:


x = 'hello, world'
print(len(x))


# In[89]:


txt = 'python is awesome programm in worldwide'
print('programm' in txt)


# In[91]:


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# In[92]:


txt = 'python is awesome programm in worldwide'
print('programm' not in txt)


# In[93]:


txt = 'python is awesome programm in worldwide'
print('grod' not in txt)


# In[94]:


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# In[95]:


a = 'hello, world'
print(a[4:7])


# In[96]:


a = 'hello, world'
print(a[:7])


# In[97]:


a = 'hello, world'
print(a[4:])


# In[98]:


a = 'hello, world'
print(a[-7:-4])


# In[99]:


a = 'hello, world'
print(a.upper())


# In[100]:


a = 'JGGGGejjej'
print(a.lower())


# In[101]:


a = " hello, world "
print(a.strip())


# In[102]:


a = 'hello, world'
print(a.replace('world', 'Maxat'))


# In[103]:


a = 'hello, world'
print(a.split())


# In[104]:


a = 'hello'
b = 'world'
c = a+b
print(c)


# In[105]:


a = 'hello'
b = 'world'
c = a + " " + b
print(c)


# In[109]:


age = 36
txt = 'my name is John, i am {}'

print(txt.format(age))


# In[110]:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# In[111]:


txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# In[ ]:




