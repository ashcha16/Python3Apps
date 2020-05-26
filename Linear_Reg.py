from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd 
import numpy as np

df= pd.read_csv("C:/Users/Ashish/Desktop/Python_3/ML/data/Real_estate.csv")
df.fillna(value=0,axis=0)
x = df["X2 house age"].values.reshape(-1,1)
y=df["Y house price of unit area"].values.reshape(-1,1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)#0.2 means 20% data will be used for test
lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)

df2=pd.DataFrame(columns=["Ytest","Ypred","x_test"])
df2["Ytest"]=y_test.flatten()
df2["Ypred"]=y_pred.flatten()
df2["x_test"]=x_test.flatten()
print(df2.head(10))

print(mean_squared_error(y_test,y_pred))

