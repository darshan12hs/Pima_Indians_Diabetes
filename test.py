# #since u have created the model using joblib u have to load the model
# #using same library joblib
# import joblib
import joblib
import pickle

# load the model using joblib
model=joblib.load('../pythonProject4/model_file.pkl')

# Loading the model using pickle
# model=pickle.load(open('model_file_pickle.pkl',"rb"))

output=model.predict([[1,1,1,1,1,1,1,1,]]) #Takes 2 dimension data
print(output) # 0 indicates person is non-diabetic

if output[0]==1:
    print("Take care of yourself, You are diabetic")
else:
    print("You are healthy & perfectly fine")

print(__name__)