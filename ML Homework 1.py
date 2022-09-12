import numpy as np


# Question 1

np.__version__

# ------------

import pandas as pd

df = pd.read_csv('data.csv')
df.head()


# Question 2

df.index

# ----------


df.loc[1]
df.describe()


# Question 3

df['Make'].value_counts().nlargest(3)

# ----------


df['Make'].mode()

df.loc[df['Make'] == 'Audi']



# Question 4

df.groupby('Make')['Model'].nunique()['Audi']

# ---------


# Question 5

df.isnull().sum()

# -----------


# Question 6

df['Engine Cylinders'].median()

modeEC = df['Engine Cylinders'].mode()
modeEC

df['Engine Cylinders'] = df['Engine Cylinders'].fillna(4.0)

df['Engine Cylinders'].isnull().sum()

df['Engine Cylinders'].median()

# -------


