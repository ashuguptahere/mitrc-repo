from sklearn.datasets import load_iris
data=load_iris()

x=data.data
y=data.target

from sklearn.svm import SVC
model=SVC()

model.fit(x,y)
####cross validation####
from sklearn.model_selection import cross_val_score
acc=cross_val_score(model,x,y,cv=20)
print(acc)

########################
from sklearn.model_selection import GridSearchCV
par=[{"C":[1,10,100,1000],"kernel":["linear"]},
      {"C":[1,10,100,1000],"kernel":["rbf"],
       "gamma":[0.1,0.01,0.001,0.0001]}]
#############################
GS=GridSearchCV(estimator=model,
                param_grid=par,
                scoring="accuracy",
                cv=10,
                n_jobs=-1)
#############################
model_gs=GS.fit(x,y)
#############################
print(model_gs.best_score_)
print(model_gs.best_params_)
####final model#####
opt_model=SVC(C=1,kernel="linear")
#prep the data for test
x_test=[2,2,4,2]
#prep opt model and fit to data
opt_model.fit(x,y)
#pred value aacc to opt model
y_pred=opt_model.predict([x_test,])
print(opt_model.score(x,y))
print(y_pred)
print(data.target_names[y_pred])
####################################################
####################################################
####################################################
# different model
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()

from sklearn.svm import SVC
svm_m=SVC()

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()

from sklearn.ensemble import VotingClassifier
model_en=VotingClassifier([("Decision_tree",dt),
                           ("support_vector",svm_m),
                           ("KNN",knn)])
#fitting ensemble model to data
model_en.fit(x,y)
#########################
x_test=[2,2,4,2]
#pred value aacc to opt model
y_pred=model_en.predict([x_test,])
print(model_en.score(x,y))
print(y_pred)
print(data.target_names[y_pred])
#####################################################
#bagging
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
model_bagging=BaggingClassifier(dt)
model_bagging.fit(x,y)
x_test=[2,2,4,2]
#pred value aacc to opt model
y_pred=model_en.predict([x_test,])
print(model_en.score(x,y))
print(y_pred)
print(data.target_names[y_pred])
#############################################
###random forest
from sklearn.ensemble import RandomForestClassifier
model_rf=RandomForestClassifier()
model_rf.fit(x,y)
x_test=[2,2,4,2]
#pred value aacc to opt model
y_pred=model_rf.predict([x_test,])
print(model_rf.score(x,y))
print(y_pred)
print(data.target_names[y_pred])














