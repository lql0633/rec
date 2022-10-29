
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.title("data")
df=pd.read_csv('Train.csv')
df = df.sample(5000).reset_index(drop=True)

if st.checkbox('Show dataframe'):
    df

#每列特征含义
st.write("Means of data：")
st.write("ID: ID Number of Customers.")
st.write("Warehouse block: The Company have big Warehouse which is divided in to block such as A,B,C,D,E.")
st.write("Mode of shipment:The Company Ships the products in multiple way such as Ship, Flight and Road.")
st.write("Customer care calls: The number of calls made from enquiry for enquiry of the shipment.")
st.write("Customer rating: The company has rated from every customer. 1 is the lowest (Worst), 5 is the highest (Best).")
st.write("Cost of the product: Cost of the Product in US Dollars.")
st.write("Prior purchases: The Number of Prior Purchase.")
st.write("Product importance: The company has categorized the product in the various parameter such as low, medium, high.")
st.write("Gender: Male and Female.")
st.write("Discount offered: Discount offered on that specific product.")
st.write("Weight in gms: It is the weight in grams.")
st.write("Reached on time: It is the target variable, where 1 Indicates that the product has NOT reached on time and 0 indicates it has reached on time.")



st.sidebar.header("filtering widgets")
st.title("filtering widgets")
input= st.sidebar.number_input('Which index data do you want to watch?(<4999)',value=0, min_value = 0, max_value = 5000)
st.write("watch input index data")
data=pd.DataFrame(df.iloc[[input]])
st.dataframe(data)


options = st.sidebar.multiselect(
   'What Warehouse_block do you want to show',
    ('A', 'B', 'C','D','E','F'), ('A'))


#st.write("watch Warehouse_block filter data")
#for i in options:
    #df.loc[df['Warehouse_block']==i]
df=df.loc[df['Warehouse_block'].isin(list(options))]


values = st.sidebar.slider(
'Select a range of values in cost of the product',
   df['Cost_of_the_Product'].min(), df['Cost_of_the_Product'].max(),(120,250))
filter=df.loc[(df['Cost_of_the_Product']<=values[1]) & (df['Cost_of_the_Product']>=values[0])]
#st.write("watch cost of the product filter data")
#st.dataframe(filter)

df=filter

#Warehouse_block分布
st.subheader("Warehouse_block type and nums")
f=plt.figure(figsize=(10,6))
plt.pie(df.Warehouse_block.value_counts(),startangle=90,autopct='%.2f%%',labels=list(df.Warehouse_block.value_counts().index),radius=10,colors=['blue','pink','red','yellow','green'])
plt.axis('equal')
plt.title('Warehouse Block',fontdict={'fontsize':22,'fontweight':'bold'})
st.pyplot(f)

#是否到达分类数量
st.subheader("sum of reach on time or not")
f=plt.figure(figsize=(10,6))
category=df['Reached.on.Time_Y.N'].value_counts()
category.plot(kind='bar',color='r')
st.pyplot(f)


st.title("plots")
#重量花销分布直方图
st.subheader("Weight distribution of product")
f=plt.figure(figsize=(15,6))
plt.hist(df.Weight_in_gms,bins=50,color='violet')
plt.xlabel('Weight',fontsize=20)
st.pyplot(f)


#开销箱型图
st.subheader("boxplot of cost")
f=plt.figure(figsize=(10,6))
plt.boxplot(df.Cost_of_the_Product, widths=0.1,  # 指定箱线图的宽度
            notch=False,
            vert=True,
            meanline=True,
            patch_artist=True,
            showmeans=True,
            showcaps=True,
            showfliers=True,
            meanprops = {"color": "black", "linewidth": 1.5},
            medianprops={"color": "red", "linewidth": 0.5},
            boxprops={"facecolor": "C0", "edgecolor": "black","linewidth": 0.5, "alpha":0.4},
            whiskerprops={"color": "black", "linewidth": 1.5, "alpha":0.8},
            capprops={"color": "C0", "linewidth": 1.5},
            sym="+",labels=['cost of product'])
#plt.xlabel('cost of product',fontsize=20)
st.pyplot(f)


#散点图两两特征关系
st.subheader("Discount_offered with weight and customer rating")
f, ax = plt.subplots(ncols=2,figsize=(20, 10))
ax[0].scatter(df['Discount_offered'],df['Weight_in_gms'],color='orange')
ax[0].set_xlabel('Discount_offered',fontsize=20)
ax[0].set_ylabel('Weight_in_gms',fontsize=20)
ax[1].scatter(df['Discount_offered'],df['Customer_rating'],color='orange')
ax[1].set_xlabel('Discount_offered',fontsize=20)
ax[1].set_ylabel('Customer_rating',fontsize=20)
st.pyplot(f)



