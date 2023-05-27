#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
()
+
6


# In[ ]:


values - -87.8 , 'hello',6
expression - *
-
()
+


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[ ]:


variables is used to store data and that can be any type of data,values and based on thta they take space in 
memory,values stored in variable can change


# In[ ]:


String is a datatype which is used to have sequence of characters in it


# In[ ]:


3. Describe three different data types.
1.Numbers -- this is to store data with values like integer,float,complex numbers
2.String - used for sequence of characters
3.list - stores list of mulitple data -hetrogenous like list=[1,2,"neha","abc",56.78]


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


expression is combination of numbers,operators,variables and gives some required results when evaluated 


# In[ ]:





# In[ ]:


5. This assignment statements, like spam = 10. What is the difference between an
get_ipython().set_next_input('expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')
----
statements is used to create variables and store value like in above as 'spam'  or to print some values 
but in expression ,result is evaluated based on the operators and operations being performed on operands


# In[7]:


#6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
print(bacon)
--
bacon containse 22 only since bacon+1 is not assigned back to bacon


# In[10]:


#7. What should the values of the following two terms be?
'spam'+'spamspam'
--- 'spamspamspam'


# In[11]:


'spam'* 3
---'spamspamspam'


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')
variables can be alphabets or combination of alphabets & digits and _
eggs is valid but 100 invalid as -variable cannot start frm digit


# In[19]:


#9. What three functions can be used to get the integer, floating-point number, or string version of a value?
str()-string,int()-interger,float()-float


# In[20]:


#10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 +'burritos.'
can only concatenate str (not "int") to str


# In[21]:


#correct is 
'I have eaten' + '99' +'burritos.'
--- 'I have eaten99burritos.'


# In[ ]:




