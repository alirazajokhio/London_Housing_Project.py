# # LONDON HOUSING DATASET

# The dataset is primarity centered around the housing market of London. It contains a lot of additional relevant data.
# 
# -- Monthly average house prices
# -- Yearly number of houses sold
# -- Monthly number of crimes commited
# 
# The data used here is from year 1995 to 2019 of each different area.
# 
# This data is a CSV file, downloaded from Kaggle.
# 
# We will analyze the data using the Pandas DataFrame.
# 
# Here, random sets of questions are given for which we have to find the correct resutls.
# 

# In[6]:
import pandas as pd

# In[7]:
data = pd.read_csv(r"E:\London_Housing_Dataset.csv")

# In[8]:
data

# In[11]:
data.count()

# In[12]:
data.isnull().sum()

# To see the null values in heatmap, we'll import seaborn as sns and mtplotlib.pyplot as plt
# In[14]:
import seaborn as sns
import matplotlib.pyplot as plt

# In[15]:
sns.heatmap(data.isnull())

# #### (A). Convert the datatype of 'Date' column to Date-Time format
# In[17]:
data.head()

# In[19]:
data.dtypes

# In[20]:
data.date = pd.to_datetime(data.date)

# In[21]:
data.dtypes

# #### (B.1) Add a new column "year" in the dataframe, which contains years only.
# In[22]:

data.head()

# In[25]:
data['year'] = data.date.dt.year

# In[26]:
data

# #### (B.2) Add a new column "month" as 2nd column in the dataframe, which contains month only.
# In[27]:
data.insert(1, 'month', data.date.dt.month)

# In[29]:
data.head()

# #### (C) Remove the columns 'year' and 'month' from the dataframe.
# In[31]:

data.drop(['month','year'] , axis = 1, inplace = True)
# In[32]:

data.head()
# #### (D) Show all the records where "No. of Crimes' is 0. And, how many such records are there?

# In[33]:
data.head()

# In[34]:
data[data.no_of_crimes == 0]

# In[35]:
len(data[data.no_of_crimes == 0])

# #### (E) What is the maximum and minimum average_price per year in england?
# In[36]:
data['year'] = data.date.dt.year

# In[37]:
data.head()

# In[39]:
df1 = data[data.area == 'england']

# In[40]:
df1

# In[50]:
#df1.groupby('year').average_price.max()
#df1.groupby('year').average_price.min()
df1.groupby('year').average_price.mean()

# #### (F) What is the Maximum and Minimum No. of Crimes recorded per area?
# In[53]:
data.groupby('area').no_of_crimes.max().sort_values()

# In[54]:
data.groupby('area').no_of_crimes.min().sort_values()


# #### (G) Show the total count of records of each area, where average price is less than 100,000
# In[55]:
data.head()

# In[56]:
data[data.average_price < 100000]

# In[57]:
data[data.average_price < 100000].area.value_counts()
