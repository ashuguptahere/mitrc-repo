import numpy as np
import pandas as pd

data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\train.csv")
data.isnull().sum()

data.info()
#data["Embarked"].fillna("S",inplace=True)
data["Embarked"].fillna(method="ffill",inplace=True)
data.isnull().sum()

pos=data["Embarked"]
pos
s=0
c=0
q=0
for i in pos:
    if(i=='S'):
        s=s+1
    elif(i=="Q"):
        q=q+1
    else:
        c=c+1
print(s,c,q)
####################################
data.columns
data=data.drop(["PassengerId","Name","Ticket",
                "Cabin"],axis=1)

data.columns
data.info()
#####################################
from sklearn import preprocessing
le=preprocessing.LabelEncoder()

data["Embarked"]=le.fit_transform(data["Embarked"])
data["Sex"]=le.fit_transform(data["Sex"])

data.isnull().sum()

data["Age"].plot.hist()
data["Age"].fillna(data["Age"].median(),
    inplace=True)

y=data["Survived"]
x=data.drop(["Survived"],axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=0.25,
                                              random_state=520 )
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train,y_train)
#######################################33
THRESHOLD = 0.67
import numpy as np
y_pred=np.where(model.predict_proba(x_test)[:,1] > THRESHOLD, 1, 0)
print(model.predict_proba(x_test))
#model test and take y_pred value
print(y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))
##################################################

