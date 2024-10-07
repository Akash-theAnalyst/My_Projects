from google.colab import drive
drive.mount('/content/drive')

pip install category_encoders

from pandas import read_csv, get_dummies,Series,DataFrame, to_datetime
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from imblearn.over_sampling import SMOTE
from plotly import graph_objs
import plotly.figure_factory as ff
from category_encoders import TargetEncoder
data1=read_csv('/content/drive/MyDrive/Colab Notebooks/24 April Dataset.csv') # I am reading the data here using read_csv from Pandas
data1.info()

data2 = data1.drop(["Customer Name", "Dealer_Name", "Dealer_No "], axis=1) # Feature Reeduction Technique USED- DROP MANUALLY
data2['Transmission']=data2['Transmission'].map({'Auto':1,'Manual':0}) #Binary Nature
data2['Gender']=data2['Gender'].map({'Male':1,'Female':0}) #Binary Nature
data2['Engine']=data2['Engine'].map({'DoubleÂ\xa0Overhead Camshaft':1,'Overhead Camshaft':0}) #Binary Nature
data2

#date conversion
data2.shape
to_datetime(392175900  , unit='s')
DataFrame(data2['Date'])
data2['Date']=to_datetime(data2['Date'],format='mixed') #format='%d-%m-%y %H:%M:%S'
data2.info()
DataFrame(data2['Date'])

data2['year'] = data2['Date'].dt.year #DATE CONVERSION
data2['month'] = data2['Date'].dt.month
data2['day'] = data2['Date'].dt.day
data2['Day_week'] = data2['Date'].dt.dayofweek
data2.info()

data2=data2.drop(['Date'], axis=1)  #DATE FEATURE REMOVED
data2.info()
data2.head()

print(data2['Company'].unique())
print(data2['Body Style'].unique())
print(data2['Dealer_Region'].unique())
print(data2['Color'].unique())

data2['Body Style'] = data2['Body Style'].map({'SUV':1, 'Passenger':2, 'Hatchback':3, 'Hardtop':4, 'Sedan':5})
data2['Color'] = data2['Color'].map({'Black':1, 'Red':2, 'Pale White':3})
data2['Dealer_Region'] = data2['Dealer_Region'].map({'Middletown':1, 'Aurora':2, 'Greenville':3, 'Pasco':4, 'Janesville':5, 'Scottsdale':6, 'Austin':7})
data2.head()

X = data2.drop(['Price ($)'], axis = 1) #FEATURES
Y = data2['Price ($)'] #LABEL
print(X.shape)
print(Y.shape)

Target_Encoder1 = TargetEncoder(cols=['Company']).fit(X,Y)#TARGET ENCODING
X = Target_Encoder1.transform(X)

print(X.info())
X.head()

corrs = X.corr()
figure = ff.create_annotated_heatmap(corrs.values,list(corrs.columns),list(corrs.columns), corrs.round(2).values,showscale=True)
figure.show()

X=X.drop(['Transmission'],axis=1) #FEATURE REDUCTION VIA HEAT MAP

X.info()
Y.info()

# data Scaling
X2 = StandardScaler().fit_transform(X)
DataFrame(X2)

# Linear Regression (LR)

LinearRegression1 = SGDRegressor(random_state = 1, penalty = None) # building
Hparameter1 = {'eta0': [.0001, .001, .01, .1, 1], 'max_iter':[5000,7500,9000,10000,15000,20000,25000,30000,40000]}
grid_search1 = GridSearchCV(estimator=LinearRegression1, param_grid=Hparameter1, scoring='r2', cv=5)
grid_search1.fit(X2, Y)

# results = DataFrame.from_dict(grid_search1.cv_results_)
# print("Cross-validation results:\n", results)

best_parameters = grid_search1.best_params_
print("Best parameters: ", best_parameters)
best_result = grid_search1.best_score_
print("Best result: ", best_result)
best_model = grid_search1.best_estimator_
print("Intercept β0: ", best_model.intercept_)

print(DataFrame(zip(X.columns, best_model.coef_), columns=['Features','Coefficients']))
#Best parameters:  {'eta0': 0.001, 'max_iter': 5000}
#Best result:  0.06427149098794352
#Intercept β0:  [27939.30808422]

#  Regularization # IF L1-RATIO is 1 penalty applied - PURE L1 regularization (Lasso regression)

LinearRegression2 = SGDRegressor(random_state = 1, penalty = 'l1')
parameter = {'eta0': [ 0.001, .01, .1, 1], 'max_iter':[5000,7500,9000,10000,15000,20000,25000,30000,40000],'alpha': [ 0.01, 0.1, 1,10, 100]}

grid_search = GridSearchCV(estimator=LinearRegression2, param_grid=parameter, scoring='r2', cv=5)
grid_search.fit(X2, Y)

best_parameters = grid_search.best_params_
print("Best parameters: ", best_parameters)

best_result = grid_search.best_score_
print("Best result: ", best_result)

best_model = grid_search.best_estimator_
print("Intercept β0: ", best_model.intercept_)

print(DataFrame(zip(X.columns, best_model.coef_), columns=['Features','Coefficients']))

#Best parameters:  {'alpha': 100, 'eta0': 0.01, 'max_iter': 5000}
#Best result:  0.06541542427737342
#Intercept β0:  [27881.44394453]

#  Regularization # IF L1-RATIO is 0 penalty applied - PURE L2 regularization (RIDGE regression).

LinearRegression3 = SGDRegressor(random_state = 1, penalty = 'l2')
parameter = {'eta0': [ 0.0001, .001, .01, 0.1,1], 'max_iter':[5000,7500,9000,10000,15000,20000,25000,30000,40000],'alpha': [ 0.01, .1, 1,10, 100]}

grid_search = GridSearchCV(estimator=LinearRegression3, param_grid=parameter, scoring='r2', cv=5)
grid_search.fit(X2, Y)

best_parameters = grid_search.best_params_
print("Best parameters: ", best_parameters)

best_result = grid_search.best_score_
print("Best result: ", best_result)

best_model = grid_search.best_estimator_
print("Intercept β0: ", best_model.intercept_)

print(DataFrame(zip(X.columns, best_model.coef_), columns=['Features','Coefficients']))

#Best parameters:  {'alpha': 0.1, 'eta0': 0.01, 'max_iter': 5000}
#Best result:  0.06434287402237178
#Intercept β0:  [28068.57659731]

# Regularization

LinearRegression4 = SGDRegressor(random_state = 1, penalty = 'elasticnet')
parameter = {'eta0': [ 0.001, .01, .1, 1], 'max_iter':[5000,7500,9000,10000,15000,20000,25000,30000,40000],'alpha': [ 0.01, .1, 1,10, 100], 'l1_ratio': [0,0.25,0.5,0.75,1]}

grid_search = GridSearchCV(estimator=LinearRegression4, param_grid=parameter, scoring='r2', cv=5)
grid_search.fit(X2, Y)

best_parameters = grid_search.best_params_
print("Best parameters: ", best_parameters)

best_result = grid_search.best_score_
print("Best result: ", best_result)

best_model = grid_search.best_estimator_
print("Intercept β0: ", best_model.intercept_)

print(DataFrame(zip(X.columns, best_model.coef_), columns=['Features','Coefficients']))

#Best parameters:  {'alpha': 100, 'eta0': 0.01, 'l1_ratio': 1, 'max_iter': 5000}
#Best result:  0.06541542427737342
#Intercept β0:  [27881.44394453]

# Support Vector Regression WITHOUT "C"

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
SVRegressor = SVR()
cv=5

parameters = {'kernel':['linear','poly','rbf','sigmoid'],'epsilon': [50,100,500,750,1000,1500]}
grid_search1 = GridSearchCV(estimator=SVRegressor, param_grid=parameters, scoring='r2')
grid_search1.fit(X2, Y)

best_parameters = grid_search1.best_params_
print("Best parameters: ", best_parameters)

best_result = grid_search1.best_score_
print("Best result: ", best_result)

#Best parameters:  {'epsilon': 1500, 'kernel': 'linear'}
#Best result:  -0.07765343204000122

#Support Vector Regression WITH "C"

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
SVRegressor2 = SVR()
cv=5

parameters = {'kernel':['linear','poly','rbf','sigmoid'], 'C': [50,100,500,1000,5000,10000], 'epsilon': [50,100,500,1000,5000]}
grid_search1 = GridSearchCV(estimator=SVRegressor2, param_grid=parameters, scoring='r2')
grid_search1.fit(X2, Y)

best_parameters = grid_search1.best_params_
print("Best parameters: ", best_parameters)

best_result = grid_search1.best_score_
print("Best result: ", best_result)

#Best parameters:  {'C': 5000, 'epsilon': 5000, 'kernel': 'rbf'}
#Best result:  0.041934324761546106

#Modified mean square error

r, c=X2.shape
print(X2.shape)
print(r,c)
print(4/5*r,c)
modified_r2 = 1-(1-best_result)*(4/5*r-1)/(4/5*r-c-1) # 4/5*r is number of rows in training set, c is number of columns
print("modified_r2: ", modified_r2)

# (3906, 11)
# 3906 11
# 3124.8 11
# modified_r2:  0.038548716168760544

from sklearn.ensemble import RandomForestRegressor
from pandas import Series

RF_Regressor1 = RandomForestRegressor(criterion='squared_error', max_features='sqrt', random_state=1)
no_Trees = {'n_estimators': [10,20,30,40,50,100]}
r, c=X2.shape
print(r,c)

grid_search3 = GridSearchCV(estimator=RF_Regressor1, param_grid=no_Trees, scoring='r2', cv=5)
grid_search3.fit(X2, Y)

best_parameters = grid_search3.best_params_
print("Best parameters: ", best_parameters)

best_result = grid_search3.best_score_
print("best_score: ", best_result)

modified_r2 = 1-(1-best_result)*(4/5*r-1)/(4/5*r-c-1)
print("modified_r2: ", modified_r2)

Important_feature = Series(grid_search3.best_estimator_.feature_importances_, index=list(X)).sort_values(ascending=False) # Getting feature importances list for the best model
print(Important_feature)

best_model = grid_search3.best_estimator_
print(best_model)

#3906 11
#Best parameters:  {'n_estimators': 100}
#best_score:  0.11682598310467898
#modified_r2:  0.11370502635003732
#RandomForestRegressor(max_features='sqrt', random_state=1)

import joblib

joblib.dump(best_model, "Sales_model.pkl")

My_model = joblib.load("Sales_model.pkl")

x=[[0.52858,	2.109840,	-0.387078,	0.945662,	0.985087,	-1.270394,	-1.550933,	0.900005,	1.272238,	1.793974,	1.392819]]

predict=My_model.predict(x)[0]
predict=round(My_model.predict(x)[0],2)
print(predict)