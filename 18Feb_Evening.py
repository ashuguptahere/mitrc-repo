#lib import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ld=[[185,72],[170,56],[168,60],[179,68],[182,72],
    [188,77],[180,71],[180,70],[183,84],[180,80],
    [180,67],[177,76]]
#convert into np arrayy
data=np.array(ld)
X=data
#clustering Kmean
from sklearn.cluster import KMeans
kmean=KMeans(n_clusters=2)
y_kmeans=kmean.fit_predict(data)
print(y_kmeans)


# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], 
            s = 300, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], 
            s = 200, c = 'blue', label = 'Cluster 2')
plt.title('Clusters of customers')
plt.xlabel('Height')
plt.ylabel('wt')
#plt.legend()
plt.show()

############model###############
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\Mall_Customers.csv")
data.info()

data.pop("CustomerID")
#final info
data.info()
#missing vlue
data.isnull().sum()
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
data["Gender"]=le.fit_transform(data["Gender"])
#####-----------find best number of cluster--------
#modfiy 
X=data.iloc[0:,[2,3]].values
print(X)
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmean=KMeans(n_clusters=i)
    kmean.fit_predict(X)
    wcss.append(kmean.inertia_)
print(wcss)
plt.plot(range(1,11),wcss)

#model on x dataset
kmean=KMeans(n_clusters=5)
y_kmeans=kmean.fit_predict(X)
y_kmeans

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], 
            s = 300, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], 
            s = 200, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], 
            s = 150, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], 
            s = 100, c = 'purple', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], 
            s = 50, c = 'black', label = 'Cluster 5')
plt.xlabel("Accuanl income")
plt.ylabel("Spending score")
plt.legend()
plt.show()
##############################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\Mall_Customers.csv")
data.info()
data.pop("CustomerID")
#final info
data.info()
#missing vlue
data.isnull().sum()
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
data["Gender"]=le.fit_transform(data["Gender"])
#####################################
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmean=KMeans(n_clusters=i)
    kmean.fit_predict(data)
    wcss.append(kmean.inertia_)
print(wcss)
plt.plot(range(1,11),wcss)

################model on x dataset###
kmean=KMeans(n_clusters=7)
y_kmeans=kmean.fit_predict(data)
y_kmeans

##############################################