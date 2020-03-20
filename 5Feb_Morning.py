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






