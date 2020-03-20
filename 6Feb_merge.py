import matplotlib as pl
import matplotlib.pyplot as plt

import pandas as pd
#create dataframe 
d={"Id":[1,2,3,4,5],
   "name":["raja","teja","goga","ramlal","sammer"],
   "Education":["pg","ug","phd","ug ","phd"]}
data1=pd.DataFrame(d)

d1={"Id":[1,2,3,4,5],
   "salary":[5000,2000,3000,4000,6000],
   "City":["alwar","tijara","kishanghar","jaipur","delhi"]}
data2=pd.DataFrame(d1)

data_merge=pd.merge(data1,data2,on="Id")
print(data_merge)

data_merge=pd.merge(data1,data2,on="Id",how="inner")
print(data_merge)
#####################################
#concat
r=pd.concat((data1,data2),axis=1)
print(r)
c=pd.concat((data1,data2),axis=0)
print(c)
###################################3
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,1,3,5,4]
plt.plot(x,y,color="red")
plt.show()
##############################



