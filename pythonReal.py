#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 23:03:35 2022

@author: jacob
"""

import pandas as pd

data = pd.read_csv('transaction.csv',sep=';')

data.info()

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

data['CostPerTransaction'] = CostPerTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculations
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding Markup

data['Markup'] = round(data['Markup'],2)

data['CostPerTransaction'] = round(data['CostPerTransaction'],2)
data['SalesPerTransaction'] = round(data['SalesPerTransaction'],2)
data['ProfitPerTransaction'] = round(data['ProfitPerTransaction'],2)


day = data['Day'].astype(str)
month = data['Month']
year = data['Year'].astype(str)

my_date = day+'-'+month+'-'+year
data['Date'] = my_date

split_col = data['ClientKeywords'].str.split(',' , expand =True)

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ClientPeriod'] = split_col[2]


data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['ClientPeriod'] = data['ClientPeriod'].str.replace(']' , '')

data['ItemDescription'] = data['ItemDescription'].str.lower()

seasons = pd.read_csv('value_inc_seasons.csv' , sep= ';')
data = pd.merge(data,seasons,on='Month')

data = data.drop('ClientKeywords', axis =1)

data = data.drop('Year', axis =1)
data = data.drop('Month', axis =1)
data = data.drop('Day', axis =1)

data.to_csv('ValueInc_Cleaned_real.csv', index = False)







