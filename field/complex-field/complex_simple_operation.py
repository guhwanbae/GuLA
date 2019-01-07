#!/usr/bin/env python
# coding: utf-8

# In[18]:


x = 3+4j
print('x =', x)
print('abs(x) =', abs(x))

x = 1+1j
print('x =', x)
print('abs(x) =', abs(x))


# In[19]:


x = 3+4j
print('x =', x)

conj_x = x.conjugate()
print('conjugate(x) =', conj_x)

print('x + conjugate(x) =', x+conj_x)
print('Real[x * conjugate(x)] =', (x*conj_x).real)
print('abs(x)^2 =', abs(x)**2)

