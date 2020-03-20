import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
########################################################
data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\d.csv")
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
data_pre=data.iloc[0:,4:]
data_pre.info()
##########################
#dummies label encoding
ip=pd.get_dummies(data_pre["international plan"])
ip.head()
ip.pop("no")

vp=pd.get_dummies(data_pre["voice mail plan"])
vp.head()
vp.pop("yes")
vp.head()
#############################
#dummy for churn
chu_red=pd.get_dummies(data_pre["churn"],drop_first=True)
chu_red.head()
###########################
data_p=pd.concat((data_pre,ip,vp,chu_red),axis=1)
data_p.shape
final=data_p.drop(["churn","voice mail plan","international plan"],axis=1)
final.shape
final.info()
##################################
#dep and indepent divide
final.columns
############################
y=final[True]
x=final.drop([True],axis=1)
###################################
#split data into training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,
                                               test_size=0.25,
                                               random_state=20)
#train is 75% and test= 25%
x_train.shape
print(3333*.75)

###################################
from sklearn.linear_model import LogisticRegression
####################################
#make a model on logistic Regression
model=LogisticRegression()
#############################
#model fit data x_train,y_train to train it
model.fit(x_train,y_train)
############################################
#model test
y_pred=model.predict(x_test)
##############
#import module to justify result
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
#################################################
print("Classification report is :" ,classification_report(y_test,y_pred))
print("Accuracy of model is: ",accuracy_score(y_test,y_pred))
print("confusion matrix is :")
print(confusion_matrix(y_test,y_pred))
##################################################

plt.scatter(y_test,y_pred,color="red")
plt.show()
###################################################
#modelling with label encoding
###################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
########################################################
data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\d.csv")
#remove some irrevalant data
data_pre=data.iloc[0:,4:]
data_pre.info()
# Import label encoder 
from sklearn import preprocessing 
# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 
#####################################################
data_pre['international plan']= label_encoder.fit_transform(data_pre['international plan'])
data_pre['voice mail plan']= label_encoder.fit_transform(data_pre['voice mail plan'])
data_pre['churn']= label_encodger.fit_transform(data_pre['churn']) 
##########################################################

y=data_pre["churn"]
x=data_pre.drop(["churn"],axis=1)
from sklearn.preprocessing import StandardScaler
x_sac=StandardScaler()
x_sac.fit(x)

#split data into training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,
                                               test_size=0.25,
                                               random_state=20)
#train is 75% and test= 25%
x_train.shape
print(3333*.75)

###################################
from sklearn.linear_model import LogisticRegression
####################################
#make a model on logistic Regression
model=LogisticRegression()
#############################
#model fit data x_train,y_train to train it
model.fit(x_train,y_train)
############################################
#model test
y_pred=model.predict(x_test)
##############
#import module to justify result
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
#################################################
print("Classification report is :" ,classification_report(y_test,y_pred))
print("Accuracy of model is: ",accuracy_score(y_test,y_pred))
print("confusion matrix is :")
print(confusion_matrix(y_test,y_pred))
  