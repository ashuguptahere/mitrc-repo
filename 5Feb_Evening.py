#2nd library for Machine Learning
import pandas as pd
#create dataframe 
d={"Id":[1,2,3,4,5],
   "name":["raja","teja","goga","ramlal","sammer"],
   "Education":["pg","ug","phd","ug ","phd"]}
data=pd.DataFrame(d)
print(data)
print(type(data))
######################################
import pandas as pd
#data=pd.read_excel(r"path",sheet_name="name of sheet")
data_info=pd.read_excel(r"C:\Users\fluXcapacit0r\Desktop\abc.xlsx", sheet_name="info")
data_info

import pandas as pd
data_sal=pd.read_excel(r"C:\Users\fluXcapacit0r\Desktop\abc.xlsx", sheet_name="sal")
data_sal
###reading csv######
data=pd.read_csv("path")
###########################################
import pandas as pd
#create dataframe 
d={"Id":[1,2,3,4,5],
   "name":["raja","teja","goga","ramlal","sammer"],
   "Education":["pg","ug","phd","ug ","phd"]}
data=pd.DataFrame(d)
print(data)
#convert dataframe to csv
data.to_csv("C:/Users/fluXcapacit0r/Desktop/data_1.csv")
#data.to_json(r"C:\Users\fluXcapacit0r\Desktop\dat_1.json")



###########reading retail datastore###########
import pandas as pd
data=pd.read_excel(r"C:\Users\fluXcapacit0r\Downloads\online_retail_II.xlsx")
data
#######################################
#analysis of data
data.head()#top
data.head(15)
data.tail()#last
##########################
data.info()
###########################
data.describe()
########################
#missing data
data.isnull()
data.isnull().sum()
################################
data_1=pd.read_excel(r"C:\Users\fluXcapacit0r\Downloads\online_retail_II.xlsx",sheet_name="abc")
data_1
########################
data_1.isnull().sum()
#########################
var=data_1["Price"]
var
#########missing value fill###########
import matplotlib.pyplot as plt
import matplotlib as pl
data_1["Price"].plot.hist()
plt.hist(var)
##################################
data_1["Price"].plot.hist()#mean value
###############################
data_1["Quantity"].plot.hist()# median
#########################################
data_1["Price"].mean()
data_1["Price"].fillna(data_1["Price"].mean(),
                       inplace=True)
data_1.isnull().sum()
#####################################3
data_1["Quantity"].fillna(data_1["Quantity"].median(),
                          inplace=True)
data_1.isnull().sum()
############################################
import pandas as pd
#create dataframe 
d={"Id":[1,2,3,4,5],
   "name":["raja","teja","goga","ramlal","sammer"],
   "Education":["pg","ug","phd","ug","phd"]}
data=pd.DataFrame(d)
print(data)
#################################
data.iloc[0:,0:2]
#extract specific row and col
data.loc[0:,["Id","Education"]]
##################################
#dummy varaible
var=pd.get_dummies(data["Education"])
var
###drop to make rule valid of number of dummy
var.pop("phd")
var
###############################
var=pd.get_dummies(data["Education"],drop_first=True)
var
##############################################

####################################################################################
import pandas as pd
data_mitrc={"name":["pulkit","uday","pravi","saiyam","ruchi"],
            "age":[19,20,21,20,20],
            "branch":["cs","it","cs","ee","ec"],
            "Gender":["male","male","male","male","female"],
            "Salary":[2000,3000,1200,1500,1700],
            "home_rent":[100,200,350,150,123]}

#convert dict_type  to dataframe
data=pd.DataFrame(data_mitrc)
print(data)
print(type(data))
####################################################
#importing data from external file like csv/excel etc
import pandas as pd
my_data=pd.read_csv(r"C:\Users\fluXcapacit0r\Documents\abc.csv")
print(my_data)

data_excel=pd.read_excel(r"C:\Users\fluXcapacit0r\Desktop\dat.xlsx",
                         sheet_name="data")
print(data_excel)

data_city=pd.read_excel(r"C:\Users\fluXcapacit0r\Desktop\dat.xlsx",
                         sheet_name="city")
print(data_city)
#####convert dataframe to csv
import pandas as pd
data_mitrc={"name":["pulkit","uday","pravi","saiyam","ruchi"],
            "age":[19,20,21,20,20],
            "branch":["cs","it","cs","ee","ec"],
            "Gender":["male","male","male","male","female"],
            "Salary":[2000,3000,1200,1500,1700],
            "home_rent":[100,200,350,150,123]}

#convert dict_type  to dataframe
data=pd.DataFrame(data_mitrc)
data.to_csv(r"C:\Users\fluXcapacit0r\Documents\abc.csv")
#################################################################
#data explore and analysis
data_excel.head()
data_excel.head(2)
#top 5 row and all col
data_excel.tail()
#last 5 row adn all col
data.head(2)

####################################
data.info()
####################################
mydata=pd.read_csv(r"C:\Users\fluXcapacit0r\Desktop\data_1.csv")
print(mydata)

##missig value analysis
mydata.isnull().sum()
#################################
mydata["salary"].plot.hist()
mydata["salary"].median()
mydata["salary"].fillna(mydata["salary"].median(),
                        inplace=True)
mydata["salary"]
mydata.isnull().sum()
#----------------------------------
mydata["age"].plot.hist()
mydata["age"].mean()
mydata["age"].fillna(mydata["age"].mean(),
                        inplace=True)
mydata["age"]
mydata.isnull().sum()
#--------------------------------
mydata["rent"].plot.hist()
mydata["rent"].median()
mydata["rent"].fillna(mydata["rent"].median(),
                        inplace=True)
mydata["rent"]
mydata.isnull().sum()
#--------------------------------
#data extract
#mydata.iloc[row,col]
mydata.iloc[0:5,0:4]
mydata.iloc[0:5,0::+2]
#######################
#extract using loc method
mydata.loc[0:5,["Id","name","salary",
                "Education","rent"]]
####################################
#dummy variable
gen=pd.get_dummies(mydata["gender"],drop_first=True)
print(gen)

edu=pd.get_dummies(mydata["Education"])
print(edu)
#del using pop("col_name")
edu.pop("ug ")
print(edu)
######################################
t=(1,)
print(type(t))
#############
t=(1,2,3,4,5,6)
print(t[0])
#yes indexing is supported y tuple
t[0:]#slicing
t[::-1]
##########
t[0]=5000
print(t)
########################
t=(1,2,3,4,[1,2,3],4)
t[4][0]=50000
print(t)
######################
t=(1,1,1,2,1,2,3,2,14)
print(t.count(14))
########################
t=(23,56,32,12,54,8)
print(t.index(32))
##################################
l=[12,23,54,21,65,98,3212,45]
d=[]
for i in l:
    if(i%2==0):
        d.append(i)
print(d)
###################################
###comprehesive form##############
print([ i for i in l if i%2==0 ])
print({i:i**2 for i in range(1,11)})
###############################
import keyword
print(keyword.kwlist)
#lambda args:expression
var=lambda x,y:[x+y,x-y]
var(50,15)
##########################################



