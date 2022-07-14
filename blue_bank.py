#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 23:26:46 2022

@author: jacob
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json file

json_file = open('loan_data_json.json')
data = json.load(json_file)


#transform list to data frame

loanData = pd.DataFrame(data)

#using exp to get the annual income
income = np.exp(loanData['log.annual.inc'])

loanData['annualIncome'] = income

length = len(loanData)
ficocat = []
for x in range(0,length):
    category = loanData['fico'][x]
    
    try:
        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 400:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat='error unkown'        
    ficocat.append(cat)    
ficocat = pd.Series(ficocat)        

loanData['fico.category']= ficocat

#NEW COLUMN FOR INTREST RATE with condition

loanData.loc[loanData['int.rate']>0.12, 'int.rate.type'] = 'high'
loanData.loc[loanData['int.rate']<0.12, 'int.rate.type'] = 'low'


#plot

catplot = loanData.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green' , width =0.1)
plt.show()



purposecount = loanData.groupby(['purpose']).size()
purposecount.plot.area()
plt.show()


#scatterplot

ypoint = loanData['annualIncome']
xpoint = loanData['dti']
plt.scatter(xpoint,ypoint)
plt.show()


#writing to csv

loanData.to_csv('loan_cleaned' , index = True)


















