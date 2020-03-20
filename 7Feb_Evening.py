import matplotlib.pyplot as plt
x_a=[1,2,3,4,5]
y_a=[3,4,2,4,5]
plt.scatter(x_a,y_a,color="Red")

x_a=[1,2,3,4,5]
y_p=[2.8,3.2,3.6,4.0,4.4]
plt.plot(x_a,y_p)
plt.show()


from sklearn.metrics import r2_score
r2_score(y_a, y_p)

#########modelling###################################
#import library
import pandas as pd
import numpy as np

data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\Regression.csv")
#########################
#missing value
data.isnull().sum()
data["Age"].plot.hist()
data["Age"].fillna(data["Age"].median(),inplace=True)
data.isnull().sum()
data["Age"].median()

########################
#outlier treatment
#use boxplot
#seaborn lib
import seaborn as sns
sns.boxplot(data["Age"])

data["Age"]=np.where(data["Age"]>60,59,data["Age"])
sns.boxplot(data["Age"])
##########################
data.info()
#dummies
jt=pd.get_dummies(data["Job Type"],drop_first=True)
jt.head()

ms=pd.get_dummies(data["Marital Status"])
ms.head(3)
ms.pop("Yes")
ms.head(2)#no

edu=pd.get_dummies(data["Education"],drop_first=True)
edu.head()

mtc=pd.get_dummies(data["Metro City"],drop_first=True)
mtc.head()#yes

pre=pd.concat((data,jt,ms,edu,mtc),axis=1)
print(pre.head())

##droping irrelevant data from dataset
final=pre.drop(["Metro City","Education","Marital Status","Job Type"],axis=1)
final.head()

y=final["Purchase made"]
x=final.drop(["Purchase made"],axis=1)
x.columns
print(y)

# data divide train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                               y,test_size=0.33,
                               random_state=42)
#final data shape
final.shape
x_test.shape
x_train.shape
print(.33*325)
print(.67*325)

#algo call from sklearn
from sklearn.linear_model import LinearRegression
#model
model=LinearRegression()
###########
#model train
model.fit(x_train,y_train)
####model test
y_pre_val=model.predict(x_test)
print(y_pre_val)#predicted
#y_test#actual

from sklearn.metrics import r2_score
r2_score(y_test, y_pre_val)