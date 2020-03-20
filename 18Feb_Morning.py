import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X=np.array([[185,72],[170,56],[168,60],[179,68],[182,72],
            [188,77],[180,71],[180,70],[183,84],[180,88],
            [180,67],[177,76]],dtype=int)
###################################################
#algo
from sklearn.cluster import KMeans
model=KMeans(n_clusters=2)
y_kmeans=model.fit_predict(X)
print(y_kmeans)
####################################
#import lib
import numpy as np
import pandas as pd
#import data
data=pd.read_csv(r"file:///C:/Users/fluXcapacit0r/Documents/Python/MITRC/Mall_Customers.csv")

data.head()
data.columns
#extract data in to np array form type
X=data.iloc[0:,[3,4]].values
################################
from sklearn.cluster import KMeans#KMeans class
wcss=[]
for i in range(1,12):
    kmean=KMeans(n_clusters=i)
    kmean.fit_predict(X)
    wcss.append(kmean.inertia_)
plt.plot(range(1,12),wcss)
plt.xlabel("cluster value")
plt.ylabel("WCSS")
plt.title("CLUSTER VS WCSS")
plt.show()
#############################
#final model 
model_final=KMeans(n_clusters=5)
print(model_final)
y_pred=model_final.fit_predict(X)
###############################################
res=pd.DataFrame({"prediction":y_pred})
data1=pd.read_csv(r"file:///C:/Users/fluXcapacit0r/Documents/Python/MITRC/Mall_Customers.csv")
#extract data in to np array form type
X=data1.iloc[0:,[3,4]]
final_val=pd.concat((X,res),axis=1)
#############################################
#################exp###################
#import lib
import numpy as np
import pandas as pd
#import data
data=pd.read_csv(r"file:///C:/Users/fluXcapacit0r/Documents/Python/MITRC/Mall_Customers.csv")
data.head()
data.columns
#extract data in to np array form type
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
data["Gender"]=le.fit_transform(data["Gender"])
data.info()
data.pop("CustomerID")
X=data.iloc[0:,0:].values
################################
from sklearn.cluster import KMeans#KMeans class
wcss=[]
for i in range(1,50):
    kmean=KMeans(n_clusters=i)
    kmean.fit_predict(X)
    wcss.append(kmean.inertia_)
plt.plot(range(1,50),wcss)
plt.xlabel("cluster value")
plt.ylabel("WCSS")
plt.title("CLUSTER VS WCSS")
plt.show()
#############################
#final model 
model_final=KMeans(n_clusters=6)
print(model_final)
y_pred=model_final.fit_predict(X)














