import pandas as pd
import numpy as np
df=pd.read_csv("ecommerce_customers_unit1.csv")
#df.info()
#df.describe()

import matplotlib.pyplot as plt
# b=df.isnull().sum().sort_values(ascending=False)
#print(b)

# b.plot(kind='bar')
# plt.xticks(rotation=45)
# plt.show()

# c=df.select_dtypes(include=['number']).columns
# print(c)

Q1=df['age'].quantile(0.25)
Q3=df['age'].quantile(0.75)
IQR=Q3-Q1
print(IQR)

lower_bound=Q1-(1.5*IQR)
upper_bound=Q3+(1.5*IQR)
outliers=df[(df['age']<lower_bound) | (df['age']>upper_bound)]
print(outliers)

d=df.describe().loc['mean','age']
df['age']=df['age'].fillna(d)
