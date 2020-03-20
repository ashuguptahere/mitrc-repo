import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
########################################################
data=pd.read_csv(r"C:\Users\fluXcapacit0r\Documents\Python\MITRC\bigml_59c28831336c6604c800002a.csv")
#########################################################
#row and col
data.shape
#############
data.columns
##############
data.info()
###################
data.isnull().sum()
#######################
#remove some irrevalant data
dataset=data.iloc[0:,4:]
dataset.info()
##########################
from sklearn import preprocessing 
# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 
#####################################################
dataset['international plan']= label_encoder.fit_transform(dataset['international plan'])
dataset['voice mail plan']= label_encoder.fit_transform(dataset['voice mail plan'])
dataset['churn']= label_encoder.fit_transform(dataset['churn']) 

##############################################################
dataset.isnull().sum()

####################################
#sep dataset into dep and indep
y=dataset["churn"]
x=dataset.drop(["churn"],axis=1)
#####################################
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
#model test and take y_pred value
y_pred=model.predict(x_test)
print(y_pred)
#########################################
from sklearn.metrics import accuracy_score
print("Model accuracy is : ",accuracy_score(y_test,y_pred))
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))

##########################################################################
##########################################################################
##########################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
########################################################
data=pd.read_csv(r"C:\Users\fluXcapacit0r\Documents\Python\MITRC\bigml_59c28831336c6604c800002a.csv")
#########################################################
#row and col
data.shape
#############
data.columns
##############
data.info()
###################
data.isnull().sum()
#######################
#remove some irrevalant data
dataset=data.iloc[0:,4:]
dataset.info()
##########################
from sklearn import preprocessing 
# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 
#####################################################
dataset['international plan']= label_encoder.fit_transform(dataset['international plan'])
dataset['voice mail plan']= label_encoder.fit_transform(dataset['voice mail plan'])
dataset['churn']= label_encoder.fit_transform(dataset['churn']) 

##############################################################
dataset.isnull().sum()

####################################
#sep dataset into dep and indep
y=dataset["churn"]
x=dataset.drop(["churn"],axis=1)
#####################################
## data split train and test 70/30 train/test
acc=[]
for i in range(20,600):
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,
                                               test_size=0.30,
                                               random_state=i)
    from sklearn.linear_model import LogisticRegression
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    from sklearn.metrics import accuracy_score
    a=accuracy_score(y_test,y_pred)
    acc.append(a)

print(acc)

######################################################
d=[]
for i in range(20,600):
    d.append(i)
######################################################
random_state_acc=pd.DataFrame({"random_state":d,
                               "accuarcy":acc})
######################################################
import matplotlib.pyplot as plt
plt.scatter(d,acc,color="Red")
plt.show()

