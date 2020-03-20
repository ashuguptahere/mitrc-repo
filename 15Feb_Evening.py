from sklearn.datasets import load_iris
data=load_iris()

x=data.data
y=data.target
#################################
from sklearn.svm import SVC
model=SVC()
model.fit(x,y)

from sklearn.model_selection import cross_val_score
acc=cross_val_score(model,x,y,cv=10)
print(acc)

from sklearn.model_selection import GridSearchCV
par=[{"C":[1,10,100,1000,10000],"kernel":["linear"]},
      {"C":[1,10,100,1000,10000],"kernel":["rbf"],
       "gamma":[0.5,0.1,0.01,0.001,0.001]}]

gs_model=GridSearchCV(model,
                      param_grid=par,
                      scoring="accuracy",
                      n_jobs=-1)

gs_model.fit(x,y)
print(gs_model.best_params_)
print(gs_model.best_score_)

##########model optim
model_op=SVC(C=100,kernel="rbf",gamma=0.01)
model_op.fit(x,y)
model_op.score(x,y)

x_test=[2,2,4,2]
y_pred=model_op.predict([x_test,])
print(data.target_names[y_pred])

###########################################
#ensemble learning
from sklearn.svm import SVC
model_svm=SVC()
from sklearn.tree import DecisionTreeClassifier
model_dt=DecisionTreeClassifier()
from sklearn.neighbors import KNeighborsClassifier
model_knn=KNeighborsClassifier()
from sklearn.ensemble import VotingClassifier
model_vt=VotingClassifier([("svm",model_svm),
                           ("Dec_tree",model_dt),
                           ("KNN",model_knn)])
model_vt.fit(x,y)
model_vt.score(x,y)
x_test=[2,2,4,2]
y_pred=model_vt.predict([x_test,])
print(data.target_names[y_pred])
###################################
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
model_dt=DecisionTreeClassifier()
model_bg=BaggingClassifier(model_dt)
model_bg.fit(x,y)
model_bg.score(x,y)
x_test=[2,2,4,2]
y_pred=model_bg.predict([x_test,])
print(data.target_names[y_pred])
######################################################
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(501)
rf.fit(x,y)
rf.score(x,y)
x_test=[2,2,4,2]
y_pred=rf.predict([x_test,])
print(data.target_names[y_pred])
##############################################
