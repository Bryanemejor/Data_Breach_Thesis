#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import pandas as pd
import joblib

# In[2]:

st.markdown('Data Breach Classification')

cat_list = ['AL', 'AK', 'AZ']

for i in cat_list:
    exec("%s = %d" % (i,0)) 
        
city = st.selectbox(
    'Please Select City',
        ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'WA', 'WV', 'WI', 'WY'))

cause = st.selectbox(
    'Please Select Cause of Breach',
        ('Disclosure', 'Disposal', 'Exposure', 'IT Incident', 'loopholes', 'Vulnerability'))

method = st.selectbox(
    'Please Method of Breach ',
        ('Hacking', 'Unauthorized Access', 'Paper Data'))


    
if city=='AL':
        AL =0
elif city=='AK':
        AK =1

else: 
        AZ =2
 
      
if st.button('Click to Predict'):        
    X = pd.DataFrame({'AL':[AL], 
                      'AK':[AK], 
                      'AZ':[AZ]
                       
                     })
    
  
        
    model =joblib.load('lsvm_multi.pkl')
    
    Y = model.predict(X)
    
    if Y==0:
        st.write('The impact of data breach in', city, 'is digital')
    elif Y==1:
         st.write('The impact of data breach in', city, 'is economic')
    elif Y==2:
         st.write('The impact of data breach in', city, 'is physical')
    elif Y==3:
         st.write('The impact of data breach in', city, 'is psychological')
    elif Y==4:
         st.write('The impact of data breach in', city, 'is reputational')
    elif Y==5:
         st.write('The impact of data breach in', city, 'is societal')
    else:
        st.write('The impact of data breach in', city, 'is unknown')
    

   



