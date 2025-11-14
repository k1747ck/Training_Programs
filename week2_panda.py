import pandas as pd
import numpy as np

data = {
    'product_name' : ['Laptop', 'Mouse', 'Keyboards'],
    'category' : ['Electronics', 'Accessories', 'Gadgets'],
    'price' : [70000, 500, 2000],
    'quantity' : [1, 2, 1],
    'discount (%)' : [10, 5, 5]
}

data_frame = pd.DataFrame(data)

# print(data_frame.info)

data_frame['Revenue'] = data_frame['price'] * data_frame['quantity'] * (1 - data_frame['discount (%)']/100)
# print(data_frame.head())

# data_frame.to_csv("data.csv", index=False)

sales = pd.read_csv("data.csv")
sales.head()

# data_frame.tail() # bottom 5
# data_frame.head() # top 5

# print(sales.describe())

# Selecting, Indexing and Filtering
# print(data_frame['product_name'] == 'Laptop')


df = pd.read_csv("zomato.csv", encoding="latin-1")

df1 = pd.read_excel("Country-Code.xlsx")

# print(df.info())
# print("Rows : ", df.shape[0])
# print("Columns : ", df.shape[1])

# print(df.columns)

df_new = pd.merge(df, df1, how="left")

# print(df1['Country Code'].unique()) # prints unique columns

print(df1.columns)
print (df1['Country'].unique())
# 1 load data
# 2 analyze the data
    # rows / columns
    # Na
    # NaN  
    # Na and NaN h toh ya to fill karde
    # duplicate - if duplicate then drop
    
    
# print(df['City'] == 'New Delhi')

# print(df[df["City"] == "New Delhi"])

# print(df[(df["City"] == 'Ghaziabad')&(df['Rating text'] == 'Poor')])


df3 = pd.read_csv("quikr_car.csv",encoding="latin-1")

# print(df3.info())


# print(df3['Price'] == 'Null')
# print(df3.head())

# print(df3['Price'].unique)


# df3 = df3[df3['Price']!= 'Ask For Price']
# df3['Price'] = df3['Price'].str.replace(',','').astype(int)
# # print(df3['Price'])


# this is wrong therefore it is creating an error
# hf = pd.read_csv('zomato.csv')
# hf[hf['Rating text']== 'Excellent']['Country']

import matplotlib.pyplot as plt
import seaborn as sns

data= {
    'Category': ['Electronics','Clothing', 'Grociries', 'Toys' , 'Furniture'],
    'Revenue': [55000,32000,21000,15000,40000],
    'Profit': [12000,7000,5000,2000,9000],
    'Quantity': [120,230,300,150,100]
}

# line plot - to visualize tread over time or continuous data
# why: show how values change sequentially

# print(plt.figure(figsize=(6,4)))
# print(plt.plot(data['Category'],data['Revenue']))


# # plt.show()

# sns.barplot(x='Category', y='Revenue', data=data)
# plt.title("Seaborn Bar Plot - Revenue by Category")

# plt.show()



# histogram

plt.figure(figsize=(6,4))
plt.hist(data['Revenue'],bins=10,color='orange',edgecolor='black')
plt.title("Histogram")
plt.xlabel('Revenue')
plt.ylabel()