import numpy as np
import pandas as pd
data=pd.read_csv(r"C:\Users\fluXcapacit0r\Documents\Python\MITRC\train.csv")
#########################
data.isnull().sum()
# filling a null values using fillna()  
var=data["PassengerId"]
print(var)
a=data["Embarked"]
print(a)
s=0
c=0
q=0
for i in a:
    if(i=="S"):
        s=s+1
    elif(i=="C"):
        c=c+1
    else:
        q=q+1
print(s,c,q) 
data.isnull().sum()
#data["Embarked"].fillna("S",inplace=True) 
data.isnull().sum()

data=data.drop(["PassengerId","Name","Ticket","Cabin"],axis=1)
data.info()

data["Age"].fillna(data["Age"].median(),inplace=True)
data["Embarked"].fillna(method="ffill",inplace=True) 
data.isnull().sum()
data.info()
######label encoding
from sklearn import preprocessing 
# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 
#####################################################
data['Embarked']= label_encoder.fit_transform(data['Embarked'])
data['Sex']= label_encoder.fit_transform(data['Sex'])

y=data["Survived"]
x=data.drop(["Survived"],axis=1)
## data split train and test 70/30 train/test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,
                                               test_size=0.25,
                                               random_state=10)
#dataset: row:3333 
print(3333*0.70)
x_train.shape

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5,
                           metric='euclidean')

model.fit(x_train,y_train)


THRESHOLD = 0.56
import numpy as np
y_pred=np.where(model.predict_proba(x_test)[:,1] > THRESHOLD, 1, 0)
#print(model.predict_proba(x_test))
#model test and take y_pred value
print(y_pred)
#########################################
from sklearn.metrics import accuracy_score
print("Model accuracy is : ",accuracy_score(y_test,y_pred))
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
#####################################################3333
#model 2 dist:eud
from sklearn.neighbors import KNeighborsClassifier
model2=KNeighborsClassifier(n_neighbors=5)

model2.fit(x_train,y_train)

THRESHOLD = 0.67
import numpy as np
y_pred=np.where(model2.predict_proba(x_test)[:,1] > THRESHOLD, 1, 0)
#print(model.predict_proba(x_test))
#model test and take y_pred value
print(y_pred)
#########################################
from sklearn.metrics import accuracy_score
print("Model accuracy is : ",accuracy_score(y_test,y_pred))
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))