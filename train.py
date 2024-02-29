import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import pickle

# url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
url="train.csv"
columns=["preg","plas","pres","skin","test","mass","pedi","age","class"]
# Load Data
df=pd.read_csv(url,names=columns)
# print(df)
data=df.values
# print(data)

X=data[:,:-1]
# print(X)
y=data[:,-1]
# print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=101)
model=LogisticRegression()
model.fit(X_train,Y_train)

result=model.score(X_test,Y_test)
print(result)

# Saving the model using joblib
joblib.dump(model,"../pythonProject4/model_file.pkl")

# Saving the model using pickle
pickle.dump(model,open("../pythonProject4/model_file_pickle.pkl","wb"))