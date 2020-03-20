from sklearn import svm, datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

breast_cancer = load_breast_cancer()

X = breast_cancer.data
y = breast_cancer.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, random_state=44)

clf = LogisticRegression(penalty='l2', C=0.1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy", metrics.accuracy_score(y_test, y_pred))

y_pred_proba = clf.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()






data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\train.csv")
data.isnull().sum()
# filling a null values using fillna()  
a=data["Embarked"]
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

data["Embarked"].fillna("S", inplace = True) 
data.isnull().sum()


################################################
data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\train.csv")
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
                                               test_size=0.30,
                                               random_state=10)
#dataset: row:3333 
print(3333*0.70)
x_train.shape
##################################################
#model classification logistic reg
from sklearn.linear_model import LogisticRegression
###########################
#building a model
model=LogisticRegression()
##############################
#model train using x_train and y_train data means i am fitting data
model.fit(x_train,y_train)
###################
THRESHOLD = 0.67
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

